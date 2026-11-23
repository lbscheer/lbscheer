#!/usr/bin/env python3
"""Gera as aulas faladas de Cálculo I (MP3) a partir dos roteiros em Markdown.

Uso:
    python gerar_audio.py                 # verifica tudo e gera os 3 MP3
    python gerar_audio.py --so-verificar  # só confere respostas (sympy) e símbolos
    python gerar_audio.py --motor kokoro  # força um motor de voz (edge, gtts, kokoro)

Formato do roteiro (.md):
    "## Título {principal, extra}"  -> início de bloco (título NÃO é falado).
                                       Etiquetas dizem em qual áudio o bloco entra;
                                       sem etiqueta = {principal}.
    "PERGUNTA: ..."                 -> falada, 5 s de silêncio, "plim".
    "RESPOSTA: ..."                 -> falada logo após o plim.
    linha comum                     -> frase de explicação (700 ms depois).
    linhas com "#" ou ">"           -> ignoradas (título do arquivo / notas).

Motores de voz, na ordem tentada em modo automático:
    1. edge-tts, voz pt-BR-AntonioNeural (depois pt-BR-FranciscaNeural)
    2. gTTS, lang="pt", tld="com.br"
    3. Kokoro (offline, voz pt-BR "pm_alex"), baixa o modelo do GitHub se faltar.

Dependências: pip install edge-tts gTTS pydub sympy kokoro-onnx soundfile
(+ audioop-lts no Python 3.13) e ffmpeg instalado no sistema.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import re
import sys
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

PASTA = Path(__file__).resolve().parent
CACHE = PASTA / "cache_tts"
MODELOS = PASTA / "modelos"

PAUSA_FRASE_MS = 700
PAUSA_PERGUNTA_MS = 5000
PAUSA_APOS_PLIM_MS = 250
PAUSA_BLOCO_MS = 1500
BITRATE = "128k"

# (arquivo de saída, roteiro, etiqueta, (min, max) em minutos)
AUDIOS = [
    ("aula_limites.mp3", "roteiro_limites.md", "principal", (15, 20)),
    ("aula_derivadas.mp3", "roteiro_derivadas.md", "principal", (12, 18)),
    ("aula_limite_infinito.mp3", "roteiro_limites.md", "extra", (5, 7)),
]

KOKORO_URLS = {
    "kokoro-v1.0.onnx": "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx",
    "voices-v1.0.bin": "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin",
}


# --------------------------------------------------------------------------
# Leitura do roteiro
# --------------------------------------------------------------------------
@dataclass
class Item:
    tipo: str  # "fala", "pergunta", "resposta"
    texto: str


@dataclass
class Bloco:
    titulo: str
    etiquetas: set[str]
    itens: list[Item] = field(default_factory=list)


def ler_roteiro(caminho: Path) -> list[Bloco]:
    blocos: list[Bloco] = []
    for n, bruta in enumerate(caminho.read_text(encoding="utf-8").splitlines(), 1):
        linha = bruta.strip()
        if not linha:
            continue
        if linha.startswith("## "):
            m = re.match(r"##\s+(.*?)\s*(\{([^}]*)\})?\s*$", linha)
            titulo = m.group(1)
            etiquetas = {e.strip() for e in (m.group(3) or "principal").split(",") if e.strip()}
            blocos.append(Bloco(titulo, etiquetas))
            continue
        if linha.startswith("#") or linha.startswith(">"):
            continue
        if not blocos:
            raise ValueError(f"{caminho.name}:{n}: texto antes do primeiro bloco")
        if linha.startswith("PERGUNTA:"):
            blocos[-1].itens.append(Item("pergunta", linha[len("PERGUNTA:"):].strip()))
        elif linha.startswith("RESPOSTA:"):
            anterior = blocos[-1].itens[-1] if blocos[-1].itens else None
            if not anterior or anterior.tipo != "pergunta":
                raise ValueError(f"{caminho.name}:{n}: RESPOSTA sem PERGUNTA antes")
            blocos[-1].itens.append(Item("resposta", linha[len("RESPOSTA:"):].strip()))
        else:
            blocos[-1].itens.append(Item("fala", linha))
    for b in blocos:
        for i, it in enumerate(b.itens):
            if it.tipo == "pergunta" and (i + 1 >= len(b.itens) or b.itens[i + 1].tipo != "resposta"):
                raise ValueError(f"{caminho.name}: pergunta sem resposta no bloco '{b.titulo}'")
    return blocos


def blocos_do_audio(roteiro: str, etiqueta: str) -> list[Bloco]:
    return [b for b in ler_roteiro(PASTA / roteiro) if etiqueta in b.etiquetas]


def perguntas(blocos: list[Bloco]) -> list[tuple[str, str]]:
    saida = []
    for b in blocos:
        for i, it in enumerate(b.itens):
            if it.tipo == "pergunta":
                saida.append((it.texto, b.itens[i + 1].texto))
    return saida


# --------------------------------------------------------------------------
# Verificação 1: respostas numéricas com sympy
# --------------------------------------------------------------------------
def checagens():
    """Cada item: (roteiro, descrição, valor calculado pelo sympy, valor esperado,
    trecho que precisa aparecer no roteiro com esse valor por extenso)."""
    import sympy as sp

    x, t = sp.symbols("x t", real=True)
    oo = sp.oo
    L = sp.limit
    D = sp.diff

    def lado(expr, a, d):
        return L(expr, x, a, dir=d)

    def solucoes(expr, var):
        return sorted(sp.solve(sp.Eq(expr, 0), var))

    lim, der = "roteiro_limites.md", "roteiro_derivadas.md"
    S_esq, S_dir = (x + 3).subs(x, 2), (x**2).subs(x, 2)
    c = [
        # ---------------- LIMITES ----------------
        (lim, "lim x->2 de x^2+3x", L(x**2 + 3 * x, x, 2), 10, "a resposta é dez"),
        (lim, "lim x->2 de 3x+1", L(3 * x + 1, x, 2), 7, "RESPOSTA: Sete. Substituindo"),
        (lim, "lim x->2 de (x^2-4)/(x+2)", L((x**2 - 4) / (x + 2), x, 2), 0, "O limite é zero, e não precisa fatorar"),
        (lim, "lim x->1 de (x^2-1)/(x+3)", L((x**2 - 1) / (x + 3), x, 1), 0, "RESPOSTA: Zero. Em cima dá um menos um"),
        (lim, "lim x->2 de (x+6)/(x+2)", L((x + 6) / (x + 2), x, 2), 2, "RESPOSTA: Dois. Em cima dá oito"),
        (lim, "fatoração x^2-9 = (x-3)(x+3)", sp.expand((x - 3) * (x + 3)), x**2 - 9, "x ao quadrado menos nove é igual a x menos três, vezes x mais três"),
        (lim, "fatoração x^2-3x = x(x-3)", sp.expand(x * (x - 3)), x**2 - 3 * x, "x ao quadrado menos três x é igual a x vezes x menos três"),
        (lim, "atalho x^2+x-6 = (x-2)(x+3)", sp.expand((x - 2) * (x + 3)), x**2 + x - 6, "Então fica x menos dois, vezes x mais três"),
        (lim, "lim x->3 de (x^2-9)/(x-3)", L((x**2 - 9) / (x - 3), x, 3), 6, "três mais três dá seis. O limite é seis"),
        (lim, "lim x->3 de (x^2-3x)/(x-3)", L((x**2 - 3 * x) / (x - 3), x, 3), 3, "Corta o x menos três e sobra x, que vale três"),
        (lim, "lim x->2 de (x^2-5x+6)/(x-2)", L((x**2 - 5 * x + 6) / (x - 2), x, 2), -1, "RESPOSTA: Menos um. Fatora em x menos dois, vezes x menos três. Corta e sobra dois menos três"),
        (lim, "fatoração x^2-5x+6 = (x-2)(x-3)", sp.expand((x - 2) * (x - 3)), x**2 - 5 * x + 6, "Fatora em x menos dois, vezes x menos três"),
        (lim, "x^2+9 em x=3", (x**2 + 9).subs(x, 3), 18, "RESPOSTA: Dezoito"),
        (lim, "x^2+9 sem raiz real", len(sp.solve(x**2 + 9, x)), 0, "x ao quadrado mais nove nunca dá zero"),
        (lim, "lim x->4- de 3/(x-4)", lado(3 / (x - 4), 4, "-"), -oo, "Positivo sobre negativo: menos infinito"),
        (lim, "lim x->4+ de 3/(x-4)", lado(3 / (x - 4), 4, "+"), oo, "Positivo sobre positivo: mais infinito"),
        (lim, "lim x->1- de 5/(x-1)", lado(5 / (x - 1), 1, "-"), -oo, "Pela esquerda dá menos infinito e pela direita dá mais infinito"),
        (lim, "lim x->1+ de 5/(x-1)", lado(5 / (x - 1), 1, "+"), oo, "assíntota vertical é x igual a um"),
        (lim, "lim x->2- de 3/(x-2)^2", lado(3 / (x - 2) ** 2, 2, "-"), oo, "Mais infinito dos dois lados"),
        (lim, "lim x->2+ de 3/(x-2)^2", lado(3 / (x - 2) ** 2, 2, "+"), oo, "Mais infinito dos dois lados"),
        (lim, "g(x) esquerda em 1 (2x+1)", (2 * x + 1).subs(x, 1), 3, "dois vezes um, mais um, dá três"),
        (lim, "g(x) direita em 1 (x+2)", (x + 2).subs(x, 1), 3, "um mais dois dá três"),
        (lim, "S(x) esquerda em 2 (x+3)", S_esq, 5, "Pela esquerda dá cinco, pela direita dá quatro"),
        (lim, "S(x) direita em 2 (x^2)", S_dir, 4, "Pela esquerda dá cinco, pela direita dá quatro"),
        (lim, "S(x): limite existe? (0=não)", int(S_esq == S_dir), 0, "Como são diferentes, o limite não existe"),
        (lim, "f contínua em 3 se f(3)=6", L((x**2 - 9) / (x - 3), x, 3), 6, "f de três deveria valer seis"),
        (lim, "lim x->oo (6x^2+x)/(2x^2+3)", L((6 * x**2 + x) / (2 * x**2 + 3), x, oo), 3, "seis dividido por dois, que dá três"),
        (lim, "lim x->oo (x^3-8)/(x^2+1)", L((x**3 - 8) / (x**2 + 1), x, oo), oo, "Então vai para mais infinito"),
        (lim, "lim t->oo 2+6/(t+1)", L(2 + 6 / (t + 1), t, oo), 2, "dois mais zero, que é dois"),
        (lim, "lim t->oo 12/(t+3)", L(12 / (t + 3), t, oo), 0, "RESPOSTA: Zero. Número fixo em cima"),
        (lim, "lim x->oo (5x+1)/(x^2+4)", L((5 * x + 1) / (x**2 + 4), x, oo), 0, "RESPOSTA: Zero. O grau de baixo, dois"),
        (lim, "lim x->-oo (3x^2-2x)/(x^2+4)", L((3 * x**2 - 2 * x) / (x**2 + 4), x, -oo), 3, "a resposta no menos infinito é a mesma: três dividido por um"),
        (lim, "lim x->oo (-4x^2+1)/(2x^2-x)", L((-4 * x**2 + 1) / (2 * x**2 - x), x, oo), -2, "RESPOSTA: Menos dois. Graus iguais"),
        (lim, "lim x->oo (4x^2-3x+1)/(2x^2+5)", L((4 * x**2 - 3 * x + 1) / (2 * x**2 + 5), x, oo), 2, "quatro dividido por dois dá dois"),
        (lim, "lim x->oo (7x^3+2)/(x^3-5x)", L((7 * x**3 + 2) / (x**3 - 5 * x), x, oo), 7, "sete dividido por um dá sete"),
        (lim, "lim t->oo 5+10/(t+2)", L(5 + 10 / (t + 2), t, oo), 5, "Cinco, e a assíntota horizontal é y igual a cinco"),
        (lim, "grau 2 sobre grau 3 -> 0", L((x**2) / (x**3), x, oo), 0, "RESPOSTA: Para zero, porque o grau de baixo é maior"),
        (lim, "grau 3 sobre grau 2 -> oo", L((x**3) / (x**2), x, oo), oo, "o limite vai para infinito, e infinito não dá assíntota horizontal"),
        (lim, "lim x->4 (x^2-16)/(x-4)", L((x**2 - 16) / (x - 4), x, 4), 8, "RESPOSTA: Oito. Deu zero sobre zero"),
        (lim, "zero do denominador x+5", sp.solve(x + 5, x)[0], -5, "x igual a menos cinco"),
        (lim, "lim x->3 (x^2+9)/(x+3)", L((x**2 + 9) / (x + 3), x, 3), 3, "dezoito sobre seis, que é três"),
        (lim, "h esquerda em 2 (x+1)", (x + 1).subs(x, 2), 3, "Os dois laterais dão três"),
        (lim, "h direita em 2 (3x-3)", (3 * x - 3).subs(x, 2), 3, "Os dois laterais dão três"),
        # ---------------- DERIVADAS ----------------
        (der, "d/dx 4x^3-5x^2+3x-8", D(4 * x**3 - 5 * x**2 + 3 * x - 8, x), 12 * x**2 - 10 * x + 3, "doze x ao quadrado menos dez x mais três"),
        (der, "d/dt -4,9t^2", D(sp.Rational(-49, 10) * t**2, t), sp.Rational(-98, 10) * t, "menos nove vírgula oito t"),
        (der, "d/dx 5x^3", D(5 * x**3, x), 15 * x**2, "RESPOSTA: Quinze x ao quadrado"),
        (der, "d/dx 2x^2-7x+4", D(2 * x**2 - 7 * x + 4, x), 4 * x - 7, "RESPOSTA: Quatro x menos sete"),
        (der, "d/dx 20", D(sp.Integer(20), x), 0, "RESPOSTA: Zero. Número sozinho"),
        (der, "s=t^2+5t: v(3)", D(t**2 + 5 * t, t).subs(t, 3), 11, "A velocidade é onze metros por segundo"),
        (der, "s=t^2+5t: aceleração", D(t**2 + 5 * t, t, 2), 2, "A aceleração é dois metros por segundo ao quadrado"),
        (der, "s=3t^2+2t: v(4)", D(3 * t**2 + 2 * t, t).subs(t, 4), 26, "RESPOSTA: Vinte e seis metros por segundo"),
        (der, "T'(5) com T'=6-2t", (6 - 2 * t).subs(t, 5), -4, "seis menos dez, que dá menos quatro"),
        (der, "tangente x^2+1 em 2: y0", (x**2 + 1).subs(x, 2), 5, "O ponto é dois, cinco"),
        (der, "tangente x^2+1 em 2: m", D(x**2 + 1, x).subs(x, 2), 4, "m igual a quatro"),
        (der, "tangente x^2+1 em 2: reta", sp.expand(5 + 4 * (x - 2)), 4 * x - 3, "y igual a quatro x menos três"),
        (der, "tangente x^2-4x+3 em 3: y0", (x**2 - 4 * x + 3).subs(x, 3), 0, "RESPOSTA: O ponto três, zero"),
        (der, "tangente x^2-4x+3 em 3: m", D(x**2 - 4 * x + 3, x).subs(x, 3), 2, "A inclinação é dois"),
        (der, "tangente x^2-4x+3 em 3: reta", sp.expand(0 + 2 * (x - 3)), 2 * x - 6, "a reta é y igual a dois x menos seis"),
        (der, "h=20t-5t^2: t do máximo", solucoes(D(20 * t - 5 * t**2, t), t), [2], "t igual a dois segundos"),
        (der, "h=20t-5t^2: h(2)", (20 * t - 5 * t**2).subs(t, 2), 20, "A altura máxima é vinte metros"),
        (der, "v=12-4t para em", solucoes(12 - 4 * t, t), [3], "RESPOSTA: Em t igual a três segundos"),
        (der, "15-10t=0", solucoes(15 - 10 * t, t), [sp.Rational(3, 2)], "RESPOSTA: Um vírgula cinco segundo"),
        (der, "h=15t-5t^2: derivada", D(15 * t - 5 * t**2, t), 15 - 10 * t, "a derivada da altura é quinze menos dez t"),
        (der, "h(1,5) = altura máxima", (15 * t - 5 * t**2).subs(t, sp.Rational(3, 2)), sp.Rational(45, 4), "RESPOSTA: Onze vírgula vinte e cinco metros"),
        (der, "h(1,5): 15*1,5", 15 * sp.Rational(3, 2), sp.Rational(45, 2), "vinte e dois vírgula cinco menos onze vírgula vinte e cinco"),
        (der, "h(1,5): 5*1,5^2", 5 * sp.Rational(3, 2) ** 2, sp.Rational(45, 4), "vinte e dois vírgula cinco menos onze vírgula vinte e cinco"),
        (der, "3t^2-12t+9=0", solucoes(3 * t**2 - 12 * t + 9, t), [1, 3], "t igual a um e t igual a três"),
        (der, "3t^2-6t=0", solucoes(3 * t**2 - 6 * t, t), [0, 2], "t igual a zero e t igual a dois"),
        (der, "L'(x) de -2x^2+40x-50", D(-2 * x**2 + 40 * x - 50, x), -4 * x + 40, "L linha é menos quatro x mais quarenta"),
        (der, "L'(x)=0", solucoes(D(-2 * x**2 + 40 * x - 50, x), x), [10], "x igual a dez, com lucro de cento e cinquenta"),
        (der, "L(10)", (-2 * x**2 + 40 * x - 50).subs(x, 10), 150, "L de dez na original dá cento e cinquenta"),
        (der, "A=x^2: A'(5)", D(x**2, x).subs(x, 5), 10, "RESPOSTA: Dez. Perto de cinco centímetros"),
        (der, "aceleração de 3t^2-18t+24", D(3 * t**2 - 18 * t + 24, t), 6 * t - 18, "a de t igual a seis t menos dezoito"),
    ]
    return c


def verificar_respostas() -> bool:
    import sympy as sp

    textos = {r: (PASTA / r).read_text(encoding="utf-8") for r in ("roteiro_limites.md", "roteiro_derivadas.md")}
    linhas = []
    ok_geral = True
    for roteiro, desc, calc, esperado, trecho in checagens():
        if isinstance(esperado, list):
            ok_valor = list(calc) == esperado
        else:
            ok_valor = sp.simplify(sp.sympify(calc) - sp.sympify(esperado)) == 0 if not sp.sympify(esperado).is_infinite else calc == esperado
        ok_texto = trecho in textos[roteiro]
        ok = ok_valor and ok_texto
        ok_geral &= ok
        obs = "" if ok else ("valor diferente" if not ok_valor else "trecho não encontrado no roteiro")
        linhas.append(("OK" if ok else "ERRO", roteiro.replace("roteiro_", "").replace(".md", ""), desc, str(calc), str(esperado), obs))
    larg = [max(len(l[i]) for l in linhas + [("STATUS", "AULA", "CONTA", "SYMPY", "ESPERADO", "OBS")]) for i in range(6)]
    cab = ("STATUS", "AULA", "CONTA", "SYMPY", "ESPERADO", "OBS")
    print("\n=== Verificação das respostas com sympy ===")
    print("  ".join(c.ljust(w) for c, w in zip(cab, larg)))
    print("  ".join("-" * w for w in larg))
    for l in linhas:
        print("  ".join(c.ljust(w) for c, w in zip(l, larg)))
    n_ok = sum(1 for l in linhas if l[0] == "OK")
    print(f"Total: {n_ok}/{len(linhas)} OK\n")
    return ok_geral


# --------------------------------------------------------------------------
# Verificação 2: símbolos que a voz leria errado
# --------------------------------------------------------------------------
PROIBIDOS = [
    (r"\^", "^"), (r"/", "/"), (r"[²³⁴]", "expoente sobrescrito"), (r"√", "√"),
    (r"→|->", "seta"), (r"∞", "∞"), (r"[A-Za-z]'", "linha com apóstrofo (f')"),
    (r"=", "="), (r"\+", "+"), (r"\*", "*"), (r"[−–]", "sinal de menos unicode"),
    (r"(?<![A-Za-zÀ-ú])-|-(?![A-Za-zÀ-ú])", "hífen solto (menos)"), (r"[()\[\]{}]", "parênteses/colchetes"),
    (r"\d", "algarismo (escreva por extenso)"), (r"[<>≤≥]", "comparação"), (r"%", "%"),
]


def verificar_simbolos() -> bool:
    print("=== Verificação de símbolos no texto falado ===")
    problemas = 0
    for roteiro in ("roteiro_limites.md", "roteiro_derivadas.md"):
        for b in ler_roteiro(PASTA / roteiro):
            for it in b.itens:
                for padrao, nome in PROIBIDOS:
                    if re.search(padrao, it.texto):
                        problemas += 1
                        print(f"  ERRO [{roteiro} / {b.titulo}] '{nome}': {it.texto}")
    print("  Nenhum símbolo problemático encontrado.\n" if problemas == 0 else f"  {problemas} problema(s).\n")
    return problemas == 0


# --------------------------------------------------------------------------
# Motores de voz
# --------------------------------------------------------------------------
class Motor:
    nome = "?"

    def sintetizar(self, texto: str, destino: Path) -> None:  # pragma: no cover
        raise NotImplementedError

    @property
    def ext(self) -> str:
        return "mp3"


class MotorEdge(Motor):
    def __init__(self, voz: str):
        import edge_tts  # noqa: F401

        self.voz = voz
        self.nome = f"edge-tts ({voz})"

    def sintetizar(self, texto, destino):
        import edge_tts

        async def _run():
            await edge_tts.Communicate(texto, self.voz, rate="-5%").save(str(destino))

        asyncio.run(asyncio.wait_for(_run(), timeout=60))


class MotorGTTS(Motor):
    nome = "gTTS (pt, com.br)"

    def __init__(self):
        import gtts  # noqa: F401

    def sintetizar(self, texto, destino):
        from gtts import gTTS

        gTTS(texto, lang="pt", tld="com.br").save(str(destino))


class MotorKokoro(Motor):
    def __init__(self, voz: str = "pm_alex", velocidade: float = 1.05):
        from kokoro_onnx import Kokoro

        MODELOS.mkdir(exist_ok=True)
        for arq, url in KOKORO_URLS.items():
            alvo = MODELOS / arq
            if not alvo.exists() or alvo.stat().st_size == 0:
                print(f"  baixando {arq} ...")
                urllib.request.urlretrieve(url, alvo)
        self.k = Kokoro(str(MODELOS / "kokoro-v1.0.onnx"), str(MODELOS / "voices-v1.0.bin"))
        self.voz, self.vel = voz, velocidade
        self.nome = f"Kokoro offline ({voz}, pt-br, velocidade {velocidade})"

    @property
    def ext(self):
        return "wav"

    def sintetizar(self, texto, destino):
        import soundfile as sf

        amostras, taxa = self.k.create(texto, voice=self.voz, speed=self.vel, lang="pt-br")
        sf.write(str(destino), amostras, taxa)


def escolher_motor(preferencia: str) -> Motor:
    candidatos = []
    if preferencia in ("auto", "edge"):
        candidatos += [lambda: MotorEdge("pt-BR-AntonioNeural"), lambda: MotorEdge("pt-BR-FranciscaNeural")]
    if preferencia in ("auto", "gtts"):
        candidatos += [MotorGTTS]
    if preferencia in ("auto", "kokoro"):
        candidatos += [MotorKokoro]
    teste = CACHE / "_teste_motor"
    CACHE.mkdir(exist_ok=True)
    for fabrica in candidatos:
        try:
            motor = fabrica()
            destino = teste.with_suffix("." + motor.ext)
            motor.sintetizar("Teste de voz.", destino)
            if destino.stat().st_size > 1000:
                destino.unlink()
                print(f"Motor de voz escolhido: {motor.nome}")
                return motor
            raise RuntimeError("arquivo vazio")
        except Exception as e:  # tenta o próximo
            print(f"  motor indisponível: {getattr(fabrica, '__name__', 'edge-tts')} -> {type(e).__name__}: {str(e)[:100]}")
    sys.exit("Nenhum motor de voz funcionou.")


def falar(motor: Motor, texto: str):
    from pydub import AudioSegment

    chave = hashlib.sha1(f"{motor.nome}|{texto}".encode()).hexdigest()[:16]
    arq = CACHE / f"{chave}.{motor.ext}"
    if not arq.exists():
        motor.sintetizar(texto, arq)
    seg = AudioSegment.from_file(arq)
    return seg.set_frame_rate(24000).set_channels(1)


# --------------------------------------------------------------------------
# Montagem
# --------------------------------------------------------------------------
def montar(motor: Motor, blocos: list[Bloco]):
    from pydub import AudioSegment
    from pydub.effects import normalize
    from pydub.generators import Sine

    def silencio(ms):
        return AudioSegment.silent(duration=ms, frame_rate=24000)

    plim = Sine(880).to_audio_segment(duration=150).apply_gain(-12).fade_in(5).fade_out(20)
    plim = plim.set_frame_rate(24000).set_channels(1)

    audio = AudioSegment.empty()
    for nb, b in enumerate(blocos):
        if nb > 0:
            audio += silencio(PAUSA_BLOCO_MS)
        for i, it in enumerate(b.itens):
            voz = normalize(falar(motor, it.texto), headroom=1.0)
            audio += voz
            ultimo = i == len(b.itens) - 1
            if it.tipo == "pergunta":
                audio += silencio(PAUSA_PERGUNTA_MS) + plim + silencio(PAUSA_APOS_PLIM_MS)
            elif not ultimo:
                audio += silencio(PAUSA_FRASE_MS)
    return audio


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--so-verificar", action="store_true", help="só roda as verificações")
    ap.add_argument("--motor", default="auto", choices=["auto", "edge", "gtts", "kokoro"])
    args = ap.parse_args()

    ok1 = verificar_respostas()
    ok2 = verificar_simbolos()
    if not (ok1 and ok2):
        sys.exit("Corrija os erros acima antes de gerar o áudio.")
    if args.so_verificar:
        return

    motor = escolher_motor(args.motor)
    resumo = []
    for saida, roteiro, etiqueta, (mn, mx) in AUDIOS:
        blocos = blocos_do_audio(roteiro, etiqueta)
        print(f"Gerando {saida} ({len(blocos)} blocos) ...", flush=True)
        audio = montar(motor, blocos)
        audio.export(PASTA / saida, format="mp3", bitrate=BITRATE,
                     tags={"title": saida.replace(".mp3", "").replace("_", " "), "album": "Cálculo I em áudio"})
        minutos = len(audio) / 60000
        resumo.append((saida, minutos, mn, mx, perguntas(blocos)))

    print("\n=== Resumo ===")
    fora = False
    for saida, minutos, mn, mx, qs in resumo:
        dentro = mn <= minutos <= mx
        fora |= not dentro
        m, s = divmod(round(minutos * 60), 60)
        print(f"{saida}: {m} min {s:02d} s (faixa {mn}-{mx} min: {'OK' if dentro else 'FORA'}) | {len(qs)} perguntas")
    if fora:
        sys.exit("Algum áudio ficou fora da faixa de duração: ajuste o roteiro.")


if __name__ == "__main__":
    main()
