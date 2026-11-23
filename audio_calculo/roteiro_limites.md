# Roteiro falado: Aula de Limites (Cálculo I)

> Como ler este arquivo. Títulos com "##" separam os blocos e NÃO são falados.
> As etiquetas entre chaves no título dizem em qual áudio o bloco entra:
> {principal} = aula_limites.mp3, {extra} = aula_limite_infinito.mp3. Sem etiqueta = só principal.
> Cada linha comum é uma frase falada (700 ms de pausa entre linhas).
> PERGUNTA: é falada, seguida de 5 s de silêncio e do "plim". RESPOSTA: é falada logo depois.
> Linhas que começam com ">" são notas e não são faladas.

## Abertura {principal}

Olá! Esta é a aula falada de limites, de Cálculo um.
Vamos ver substituição, zero sobre zero, número sobre zero, limites laterais, continuidade e, com bastante calma, limite no infinito.
Depois de cada pergunta você tem cinco segundos para responder de cabeça. Depois do sinal, eu falo a resposta.
Vamos começar.

## O que é limite e o passo um {principal}
Limite responde a uma pergunta: para onde a função vai quando x chega perto de um número.
O passo um é sempre o mesmo: substitua x pelo número.
Aí aparecem três casos. Deu um número, é a resposta. Deu zero sobre zero, fatore. Deu número sobre zero, vai para infinito.
Exemplo: limite quando x tende a dois de x ao quadrado mais três x.
Substituo x por dois. Dois ao quadrado dá quatro, e três vezes dois dá seis. Quatro mais seis dá dez.
Não apareceu divisão por zero, então a resposta é dez.
PERGUNTA: Qual é sempre o primeiro passo para calcular um limite?
RESPOSTA: Substituir x pelo número. Só depois você sabe em qual caso está.
PERGUNTA: Calcule o limite quando x tende a dois de três x mais um.
RESPOSTA: Sete. Substituindo, três vezes dois mais um dá sete.
Guarde: limite é para onde a função vai, e o primeiro passo é sempre substituir.

## Caso um: deu um número {principal}
Agora o caso em que a substituição dá um número. Pronto: esse número é o limite.
Pegadinha: zero dividido por um número dá zero, e zero é resposta válida. Só é problema quando o zero está embaixo.
Exemplo: limite quando x tende a dois de x ao quadrado menos quatro, tudo dividido por x mais dois.
Em cima, quatro menos quatro dá zero. Embaixo, dois mais dois dá quatro.
Zero sobre quatro é zero. O limite é zero, e não precisa fatorar.
PERGUNTA: Calcule o limite quando x tende a um de x ao quadrado menos um, tudo dividido por x mais três.
RESPOSTA: Zero. Em cima dá um menos um, que é zero, e embaixo dá quatro. Zero sobre quatro é zero.
PERGUNTA: Calcule o limite quando x tende a dois de x mais seis, tudo dividido por x mais dois.
RESPOSTA: Dois. Em cima dá oito, embaixo dá quatro, e oito dividido por quatro é dois.
Ideia-chave: deu número, é a resposta, e zero sobre um número é zero.

## Caso dois: zero sobre zero {principal}
Agora o caso mais comum na prova: a substituição dá zero sobre zero.
Zero sobre zero não é resposta. É um aviso: existe um fator x menos a escondido em cima e embaixo, onde a é o número para onde x tende.
Você abre as expressões, corta esse fator e substitui de novo. Pode cortar porque x chega perto de a, mas não é igual a a.
Três jeitos de abrir. Primeiro, diferença de quadrados: x ao quadrado menos nove é igual a x menos três, vezes x mais três.
Segundo, fator comum: x ao quadrado menos três x é igual a x vezes x menos três.
Terceiro, trinômio por soma e produto: dois números que somam o do meio e multiplicam o do final.
Atalho: se x tende a dois, um fator é x menos dois, e o outro número é o termo final dividido por menos dois.
Por exemplo, x ao quadrado mais x menos seis: menos seis dividido por menos dois dá três. Então fica x menos dois, vezes x mais três.
Cuidado: x ao quadrado mais nove nunca dá zero, porque x ao quadrado nunca é negativo. Ele nunca é o culpado do zero sobre zero. Nele, só substitua.
Com raiz quadrada e zero sobre zero, a técnica é o conjugado. Só guarde o nome.
Exemplo: limite quando x tende a três de x ao quadrado menos nove, tudo dividido por x menos três.
Substituindo, deu zero sobre zero. Abro em cima: x menos três, vezes x mais três.
Corto o x menos três de cima com o de baixo, e sobra x mais três.
Substituo de novo: três mais três dá seis. O limite é seis.
PERGUNTA: Calcule o limite quando x tende a três de x ao quadrado menos três x, tudo dividido por x menos três.
RESPOSTA: Três. Pelo fator comum, fica x vezes x menos três. Corta o x menos três e sobra x, que vale três.
PERGUNTA: Calcule o limite quando x tende a dois de x ao quadrado menos cinco x mais seis, tudo dividido por x menos dois.
RESPOSTA: Menos um. Fatora em x menos dois, vezes x menos três. Corta e sobra dois menos três.
PERGUNTA: Quanto vale x ao quadrado mais nove quando x é três? E por que ele nunca zera?
RESPOSTA: Dezoito. Ele nunca zera porque x ao quadrado nunca é negativo, então o menor valor é nove.
Ideia-chave: zero sobre zero significa fator escondido. Fatore, corte e substitua de novo.

## Caso três: número sobre zero {principal}
Agora o terceiro caso: a substituição dá um número diferente de zero, dividido por zero. Por exemplo, cinco sobre zero.
Número fixo dividido por algo minúsculo fica gigante. Falta só descobrir o sinal.
Teste os dois lados: a menos zero vírgula zero um, e a mais zero vírgula zero um. Sinais iguais dão positivo, sinais diferentes dão negativo.
Se os dois lados dão o mesmo infinito, o limite é esse infinito. Se dão sinais diferentes, o limite não existe.
Atalho: denominador ao quadrado é sempre positivo, então o sinal depende só do de cima.
E onde o denominador zera, existe uma assíntota vertical.
Exemplo: limite quando x tende a quatro de três, tudo dividido por x menos quatro. Substituindo, dá três sobre zero.
Pela esquerda, com três vírgula noventa e nove, o de baixo dá menos zero vírgula zero um. Positivo sobre negativo: menos infinito.
Pela direita, com quatro vírgula zero um, o de baixo dá zero vírgula zero um. Positivo sobre positivo: mais infinito.
Os lados são diferentes. O limite não existe, e a assíntota vertical é x igual a quatro.
PERGUNTA: Calcule o limite quando x tende a um de cinco, tudo dividido por x menos um.
RESPOSTA: Pela esquerda dá menos infinito e pela direita dá mais infinito. O limite não existe, e a assíntota vertical é x igual a um.
PERGUNTA: Calcule o limite quando x tende a dois de três, tudo dividido por x menos dois, com esse x menos dois elevado ao quadrado.
RESPOSTA: Mais infinito dos dois lados. O de baixo, ao quadrado, é sempre positivo.
Ideia-chave: número sobre zero vai para infinito. Teste o sinal dos dois lados.

## Função com duas regras e limites laterais {principal}
Agora, funções com duas regras: uma fórmula para x menor que um número, e outra para x maior ou igual a ele.
No ponto de troca, a esquerda usa a regra do menor que. A direita usa a regra do maior ou igual.
Se os laterais forem iguais, o limite existe. Se forem diferentes, não existe.
Exemplo: g de x vale dois x mais um para x menor que um, e vale x mais dois para x maior ou igual a um.
Pela esquerda: dois vezes um, mais um, dá três. Pela direita: um mais dois dá três. São iguais, então o limite é três.
PERGUNTA: S de x vale x mais três quando x é menor que dois, e vale x ao quadrado quando x é maior ou igual a dois. Quanto dão os laterais em dois, e o limite existe?
RESPOSTA: Pela esquerda dá cinco, pela direita dá quatro. Como são diferentes, o limite não existe.
PERGUNTA: Os dois limites laterais deram sete. O limite existe?
RESPOSTA: Existe e vale sete, porque os laterais são iguais.
Ideia-chave: esquerda usa o menor que, direita usa o maior ou igual. Iguais, o limite existe.

## Continuidade {principal}
Agora, continuidade: desenhar o gráfico sem tirar o lápis do papel.
Na prova, faça três perguntas. Um: f de a existe? Dois: o limite existe? Três: f de a é igual ao limite?
Três vezes sim, é contínua. Qualquer não, não é contínua.
Para tornar a função contínua, defina f de a igual ao valor do limite.
Exemplo: f de x é x ao quadrado menos nove, tudo dividido por x menos três, para x diferente de três. E f de três vale cinco.
f de três existe, vale cinco. O limite existe, já vimos que é seis. Mas cinco é diferente de seis.
Então não é contínua. Para ser, f de três deveria valer seis.
PERGUNTA: Uma função F tem limite dois quando x tende a um, mas F de um vale três. F é contínua em um? Quanto F de um deveria valer?
RESPOSTA: Não é contínua, porque três é diferente do limite dois. F de um deveria valer dois.
PERGUNTA: Aquela função S, que vale x mais três antes de dois e x ao quadrado a partir de dois, é contínua em dois?
RESPOSTA: Não. Os laterais dão cinco e quatro, então o limite não existe.
Ideia-chave: contínua é quando f de a existe, o limite existe, e os dois são iguais.

## Abertura do áudio extra {extra}

Olá! Este é o áudio extra só de limite no infinito, para você repetir quantas vezes quiser.
Depois de cada pergunta você tem cinco segundos para responder de cabeça. Depois do sinal, eu falo a resposta.

## Limite no infinito {principal, extra}
Agora o assunto mais importante: limite no infinito. Vamos com calma.
Aqui x não chega perto de um número. Ele cresce sem parar: mil, um milhão, um bilhão.
A ideia base: um número fixo dividido por algo gigante vira quase zero.
Um dividido por dez dá zero vírgula um. Um dividido por mil dá zero vírgula zero zero um.
Um dividido por um milhão é praticamente nada.
Por isso, cinco sobre x, ou três sobre x ao quadrado, vão para zero quando x vai para infinito.
A segunda ideia: olhe só o maior expoente. Com x gigante, o termo de maior expoente manda, e os outros ficam desprezíveis.
Com x igual a mil, x ao quadrado dá um milhão, enquanto três x dá só três mil. Quase nada perto de um milhão.
O maior expoente se chama grau. Numa fração, compare o grau de cima com o grau de baixo. São três regras.
Regra um: grau de cima igual ao de baixo. O limite é a divisão dos números que acompanham os maiores expoentes.
Por quê? Os x ao quadrado de cima e de baixo se cancelam, e sobram os números da frente.
Regra dois: grau de cima maior. Vai para mais ou menos infinito, porque o de cima cresce muito mais rápido.
Regra três: grau de cima menor. Vai para zero, porque o de baixo cresce muito mais rápido.
Por exemplo, doze, tudo dividido por t mais três, vai para zero. E cinco x mais um, tudo dividido por x ao quadrado mais quatro, também vai para zero.
Decore: Igual, divide os da frente. Cima maior, infinito. Baixo maior, zero.
De novo: Igual, divide os da frente. Cima maior, infinito. Baixo maior, zero.
Primeiro exemplo: limite quando x tende a infinito de seis x ao quadrado mais x, tudo dividido por dois x ao quadrado mais três.
Grau de cima: dois. Grau de baixo: dois. Graus iguais, regra um.
O x sozinho e o três ficam desprezíveis. Sobra seis x ao quadrado sobre dois x ao quadrado.
Os x ao quadrado se cancelam, e fica seis dividido por dois, que dá três. A assíntota horizontal é y igual a três.
Segundo exemplo: limite quando x tende a infinito de x ao cubo menos oito, tudo dividido por x ao quadrado mais um.
Grau três em cima, grau dois embaixo. O de cima é maior, regra dois.
Os termos que mandam, x ao cubo e x ao quadrado, são positivos. Então vai para mais infinito, e não há assíntota horizontal.
Terceiro exemplo, com um número somado do lado de fora: limite quando t tende a infinito de dois mais seis, tudo dividido por t mais um.
O dois de fora não muda. A fração tem número fixo em cima e algo gigante embaixo, então vai para zero.
Fica dois mais zero, que é dois.
Assíntota horizontal: se o limite no infinito dá um número L, a assíntota é y igual a L. Se dá infinito, não tem assíntota horizontal.
Com x indo para menos infinito e graus iguais, a resposta é a mesma: divide os da frente.
Por exemplo, três x ao quadrado menos dois x, tudo dividido por x ao quadrado mais quatro, com x tendendo a menos infinito, dá três dividido por um, que é três.
Os números da frente podem ser negativos. Menos quatro x ao quadrado mais um, tudo dividido por dois x ao quadrado menos x, dá menos quatro dividido por dois, que é menos dois.
Na prova, escreva: Para x muito grande, os termos de maior grau dominam. O limite é seis x ao quadrado sobre dois x ao quadrado, que é três. Logo, a assíntota horizontal é y igual a três.
Agora, as perguntas.
PERGUNTA: Calcule o limite quando x tende a infinito de quatro x ao quadrado menos três x mais um, tudo dividido por dois x ao quadrado mais cinco.
RESPOSTA: Dois. Graus iguais, então quatro dividido por dois dá dois.
PERGUNTA: Calcule o limite quando x tende a infinito de sete x ao cubo mais dois, tudo dividido por x ao cubo menos cinco x.
RESPOSTA: Sete. Graus iguais, e sete dividido por um dá sete.
PERGUNTA: Calcule o limite quando t tende a infinito de doze, tudo dividido por t mais três.
RESPOSTA: Zero. Número fixo em cima e algo gigante embaixo.
PERGUNTA: Calcule o limite quando t tende a infinito de cinco mais dez, tudo dividido por t mais dois. E qual é a assíntota horizontal?
RESPOSTA: Cinco, e a assíntota horizontal é y igual a cinco. A fração vai para zero e sobra o cinco.
PERGUNTA: O grau de cima é dois e o grau de baixo é três. Para onde vai o limite no infinito?
RESPOSTA: Para zero, porque o grau de baixo é maior.
PERGUNTA: O grau de cima é três e o grau de baixo é dois. Tem assíntota horizontal?
RESPOSTA: Não. O grau de cima é maior, então o limite vai para infinito, e infinito não dá assíntota horizontal.
PERGUNTA: O limite no infinito deu quatro. Qual é a assíntota horizontal?
RESPOSTA: y igual a quatro, porque limite no infinito igual a L dá assíntota y igual a L.
Ideia-chave: olhe só os maiores expoentes. Igual, divide os da frente. Cima maior, infinito. Baixo maior, zero.

## Encerramento do áudio extra {extra}

Fim do áudio de limite no infinito. Volte ao começo e repita até as respostas saírem rápido. Bons estudos!

## Como escrever na prova {principal}
Para fechar, como escrever na prova. Não basta o número: escreva uma frase com o significado e a unidade.
Por exemplo: Quando t se aproxima de quatro minutos, a temperatura se aproxima de oito graus.
Laterais diferentes: O limite não existe, pois os limites laterais são diferentes.
PERGUNTA: Os limites laterais deram cinco e quatro. Como você escreve a conclusão?
RESPOSTA: O limite não existe, pois os limites laterais são diferentes.
PERGUNTA: O limite da temperatura quando t tende a quatro minutos é oito graus. Como escrever isso em uma frase?
RESPOSTA: Quando t se aproxima de quatro minutos, a temperatura se aproxima de oito graus.
Ideia-chave: sempre feche com uma frase completa, com o significado e a unidade.

## Revisão rápida {principal}

Agora, uma revisão rápida das regras principais.
Limite é para onde a função vai quando x chega perto de um número.
Primeiro passo: sempre substituir.
Deu número: é a resposta. Zero sobre um número é zero.
Deu zero sobre zero: tem um fator x menos a escondido. Fatore e corte.
Para fatorar: diferença de quadrados, fator comum, ou soma e produto.
x ao quadrado mais nove nunca zera. Nele, só substitua.
Zero sobre zero com raiz quadrada: a técnica é o conjugado.
Deu número sobre zero: vai para infinito. Teste o sinal com a menos zero vírgula zero um, e a mais zero vírgula zero um.
Denominador ao quadrado é sempre positivo, e onde o denominador zera há assíntota vertical.
Função com duas regras: a esquerda usa o menor que, a direita usa o maior ou igual. Se forem iguais, o limite existe.
Contínua: f de a existe, o limite existe, e os dois são iguais.
No infinito: Igual, divide os da frente. Cima maior, infinito. Baixo maior, zero.
Limite no infinito igual a L dá assíntota horizontal y igual a L.

## Quiz final {principal}

Agora, o quiz final, com oito perguntas misturando tudo.
PERGUNTA: Calcule o limite quando x tende a quatro de x ao quadrado menos dezesseis, tudo dividido por x menos quatro.
RESPOSTA: Oito. Deu zero sobre zero. Fatora em x menos quatro, vezes x mais quatro, corta e sobra quatro mais quatro.
PERGUNTA: Calcule o limite quando x tende a infinito de cinco x mais um, tudo dividido por x ao quadrado mais quatro.
RESPOSTA: Zero. O grau de baixo, dois, é maior que o de cima, um.
PERGUNTA: Onde fica a assíntota vertical de dois, tudo dividido por x mais cinco?
RESPOSTA: Em x igual a menos cinco, porque é onde o denominador zera e o de cima não.
PERGUNTA: Calcule o limite quando x tende a infinito de menos quatro x ao quadrado mais um, tudo dividido por dois x ao quadrado menos x.
RESPOSTA: Menos dois. Graus iguais, então divide os da frente mantendo o sinal: menos quatro dividido por dois.
PERGUNTA: Deu zero sobre zero e a expressão tem raiz quadrada. Qual técnica você usa?
RESPOSTA: O conjugado.
PERGUNTA: Calcule o limite quando x tende a três de x ao quadrado mais nove, tudo dividido por x mais três.
RESPOSTA: Três. Substituindo, dá dezoito sobre seis, que é três. É caso um, e x ao quadrado mais nove nunca zera.
PERGUNTA: Calcule o limite quando x tende a menos infinito de três x ao quadrado menos dois x, tudo dividido por x ao quadrado mais quatro.
RESPOSTA: Três. Com graus iguais, a resposta no menos infinito é a mesma: três dividido por um.
PERGUNTA: Uma função vale x mais um quando x é menor que dois, e vale três x menos três quando x é maior ou igual a dois. Ela é contínua em dois?
RESPOSTA: Sim. Os dois laterais dão três, e o valor no ponto também é três.

## Encerramento {principal}

Fim da aula de limites. Se errou alguma pergunta, escute o bloco dela de novo. Bons estudos!
