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

Primeiro, a ideia de limite.
O limite pergunta uma coisa simples: para onde a função vai quando x chega perto de um número.
Quando você lê limite quando x tende a três, pense assim: x está chegando cada vez mais perto de três. Para que valor a função está indo?
Repare que o limite fala de chegar perto. Não importa tanto o que acontece exatamente em cima do número.
Na prática, o passo um é sempre o mesmo: substitua x pelo número.
Depois de substituir, só existem três casos possíveis.
Caso um: deu um número. Esse número é a resposta.
Caso dois: deu zero sobre zero. Aí é preciso fatorar.
Caso três: deu um número diferente de zero, dividido por zero. Aí a função vai para o infinito.
Vamos fazer um exemplo. Limite quando x tende a dois de x ao quadrado mais três x.
Passo um: substituo x por dois. Dois ao quadrado dá quatro.
Três vezes dois dá seis.
Quatro mais seis dá dez. Deu um número, então a resposta é dez.
Por que posso substituir direto? Porque não apareceu nenhuma divisão por zero. A função está bem comportada perto de dois.
PERGUNTA: Qual é sempre o primeiro passo para calcular um limite?
RESPOSTA: Substituir x pelo número. Só depois de substituir você descobre em qual dos três casos está.
PERGUNTA: Calcule o limite quando x tende a dois de três x mais um.
RESPOSTA: Sete. Substituindo, três vezes dois mais um dá sete, que é um número, então é a resposta.
Guarde a ideia: limite é para onde a função vai, e o primeiro passo é sempre substituir.

## Caso um: deu um número {principal}

Agora vamos ver com calma o caso em que a substituição dá um número.
Se você substituiu e apareceu um número normal, pronto. Esse é o limite.
Isso vale também para frações, desde que o de baixo não dê zero.
Tem uma pegadinha aqui. Zero dividido por um número dá zero, e zero é uma resposta válida.
Por exemplo, zero sobre quatro dá zero. Não confunda com zero sobre zero. Zero só em cima não é problema.
O problema só aparece quando o zero está embaixo.
Exemplo: limite quando x tende a dois de x ao quadrado menos quatro, tudo dividido por x mais dois.
Substituo x por dois. Em cima: dois ao quadrado dá quatro, menos quatro dá zero.
Embaixo: dois mais dois dá quatro.
Ficou zero sobre quatro. O zero está só em cima, e embaixo tem um número.
Zero dividido por quatro é zero. Então o limite é zero, e acabou. Não precisa fatorar.
PERGUNTA: Calcule o limite quando x tende a um de x ao quadrado menos um, tudo dividido por x mais três.
RESPOSTA: Zero. Em cima dá um menos um, que é zero, e embaixo dá quatro. Zero sobre quatro é zero, caso um.
PERGUNTA: Calcule o limite quando x tende a dois de x mais seis, tudo dividido por x mais dois.
RESPOSTA: Dois. Em cima dá oito, embaixo dá quatro, e oito dividido por quatro é dois.
Ideia-chave: deu número, é a resposta. E zero sobre um número é zero, resposta válida.

## Caso dois: zero sobre zero {principal}

Agora vamos ver o caso mais comum na prova: quando a substituição dá zero sobre zero.
Zero sobre zero não é resposta. É um aviso.
O aviso diz: existe um fator x menos a escondido em cima e embaixo. O a é o número para onde x tende.
Se x tende a três, o fator escondido é x menos três. Se x tende a quatro, é x menos quatro.
O trabalho é abrir as expressões, achar esse fator, cortar em cima e embaixo, e depois substituir de novo.
Por que posso cortar? Porque x está chegando perto de três, mas não é igual a três. Então x menos três não é zero, e pode ser cancelado.
Existem três jeitos de abrir.
Primeiro jeito: diferença de quadrados. x ao quadrado menos nove é igual a x menos três, vezes x mais três.
A regra é: um quadrado menos outro quadrado vira a diferença vezes a soma.
Segundo jeito: fator comum. x ao quadrado menos três x é igual a x vezes x menos três. Coloquei o x em evidência.
Terceiro jeito: trinômio, por soma e produto.
Procure dois números que somam o número do meio e multiplicam o número do final.
Tem um atalho. Se x tende a dois, você já sabe que um fator é x menos dois. O outro número é o termo final dividido por menos dois.
Por exemplo, x ao quadrado mais x menos seis, com x tendendo a dois. Um fator é x menos dois. O outro número é menos seis dividido por menos dois, que dá três. Então fica x menos dois, vezes x mais três.
Um cuidado importante: x ao quadrado mais nove nunca dá zero.
x ao quadrado nunca é negativo. Somando nove, o resultado é sempre pelo menos nove.
Então x ao quadrado mais nove nunca é o culpado do zero sobre zero. Nele, você só substitui.
E se aparecer raiz quadrada e der zero sobre zero, a técnica tem outro nome: conjugado. Por enquanto, só guarde o nome.
Exemplo resolvido: limite quando x tende a três de x ao quadrado menos nove, tudo dividido por x menos três.
Passo um: substituo. Em cima, nove menos nove dá zero. Embaixo, três menos três dá zero. Deu zero sobre zero.
Então o fator x menos três está escondido. Em cima tenho diferença de quadrados.
x ao quadrado menos nove vira x menos três, vezes x mais três.
Agora corto o x menos três de cima com o x menos três de baixo. Sobra só x mais três.
Substituo de novo: três mais três dá seis. O limite é seis.
PERGUNTA: Calcule o limite quando x tende a três de x ao quadrado menos três x, tudo dividido por x menos três.
RESPOSTA: Três. Pelo fator comum, em cima fica x vezes x menos três. Corta o x menos três e sobra x, que vale três.
PERGUNTA: Calcule o limite quando x tende a dois de x ao quadrado menos cinco x mais seis, tudo dividido por x menos dois.
RESPOSTA: Menos um. Fatora em x menos dois, vezes x menos três. Corta o x menos dois e sobra dois menos três, que é menos um.
PERGUNTA: Quanto vale x ao quadrado mais nove quando x é três? E por que ele nunca zera?
RESPOSTA: Dezoito, porque nove mais nove dá dezoito. Ele nunca zera porque x ao quadrado nunca é negativo, então o menor valor possível é nove.
Ideia-chave: zero sobre zero significa fator x menos a escondido. Fatore, corte e substitua de novo.

## Caso três: número sobre zero {principal}

Agora vamos ver o terceiro caso: quando a substituição dá um número diferente de zero, dividido por zero.
Por exemplo, cinco sobre zero. Isso não é zero sobre zero, e não tem fator para cortar.
Quando o de baixo fica minúsculo e o de cima é um número fixo, a divisão fica gigante. A função vai para o infinito.
A única dúvida é o sinal: mais infinito ou menos infinito?
Para descobrir, teste um número um pouquinho menor e um pouquinho maior que o a.
Pela esquerda, use a menos zero vírgula zero um. Pela direita, use a mais zero vírgula zero um.
Depois aplique a regra de sinais.
Positivo dividido por positivo dá positivo. Positivo dividido por negativo dá negativo. Negativo dividido por negativo dá positivo.
Se os dois lados derem o mesmo infinito, o limite é esse infinito. Se derem sinais diferentes, o limite não existe.
Um atalho: se o de baixo está ao quadrado, ele é sempre positivo, porque qualquer número ao quadrado é positivo. Então o sinal depende só do de cima.
E onde o denominador zera, mas o de cima não, existe uma assíntota vertical. É uma reta vertical da qual o gráfico chega cada vez mais perto, subindo ou descendo sem parar.
Exemplo: limite quando x tende a quatro de três, tudo dividido por x menos quatro.
Substituo: três sobre quatro menos quatro, ou seja, três sobre zero. É o caso três.
Pela esquerda, testo três vírgula noventa e nove. Três vírgula noventa e nove menos quatro dá menos zero vírgula zero um, que é negativo.
Três, positivo, dividido por um negativo dá negativo. Pela esquerda vai para menos infinito.
Pela direita, testo quatro vírgula zero um. Quatro vírgula zero um menos quatro dá zero vírgula zero um, positivo.
Positivo sobre positivo dá positivo. Pela direita vai para mais infinito.
Os lados são diferentes, então o limite não existe. E a assíntota vertical é x igual a quatro.
PERGUNTA: Calcule o limite quando x tende a um de cinco, tudo dividido por x menos um.
RESPOSTA: Pela esquerda dá menos infinito e pela direita dá mais infinito. Então o limite não existe, e a assíntota vertical é x igual a um.
PERGUNTA: Calcule o limite quando x tende a dois de três, tudo dividido por x menos dois, com esse x menos dois elevado ao quadrado.
RESPOSTA: Mais infinito dos dois lados. O de baixo está ao quadrado, então é sempre positivo, e três positivo sobre um positivo pequenininho dá mais infinito.
Ideia-chave: número sobre zero vai para infinito. Teste o sinal dos dois lados, e onde o de baixo zera há assíntota vertical.

## Função com duas regras e limites laterais {principal}

Agora vamos ver funções definidas com duas regras.
É aquela função com uma chave: uma fórmula para x menor que um número, e outra fórmula para x maior ou igual a esse número.
Nesse número de troca, você precisa calcular os dois limites laterais.
O limite pela esquerda vem de números menores que a. Então ele usa a regra do menor que.
O limite pela direita vem de números maiores que a. Então ele usa a regra do maior ou igual.
Em cada lado, você substitui o número na fórmula daquele lado.
Se os dois laterais forem iguais, o limite existe e vale esse número. Se forem diferentes, o limite não existe.
Exemplo: g de x vale dois x mais um quando x é menor que um, e vale x mais dois quando x é maior ou igual a um. Qual é o limite quando x tende a um?
Pela esquerda, uso a regra do menor que: dois vezes um, mais um, dá três.
Pela direita, uso a regra do maior ou igual: um mais dois dá três.
Os dois deram três. Os laterais são iguais, então o limite existe e vale três.
PERGUNTA: S de x vale x mais três quando x é menor que dois, e vale x ao quadrado quando x é maior ou igual a dois. Quanto dão os laterais em dois, e o limite existe?
RESPOSTA: Pela esquerda dá cinco, pela direita dá quatro. Como são diferentes, o limite não existe.
PERGUNTA: Numa função de duas regras, o limite pela esquerda deu sete e o pela direita também deu sete. O limite existe?
RESPOSTA: Existe e vale sete, porque os dois laterais são iguais.
Ideia-chave: a esquerda usa a regra do menor que, a direita usa a do maior ou igual. Se forem iguais, o limite existe.

## Continuidade {principal}

Agora vamos falar de continuidade.
Uma função é contínua em um ponto quando você desenha o gráfico ali sem tirar o lápis do papel.
Na prova, você verifica isso com três perguntas.
Primeira: f de a existe? Ou seja, a função tem valor no ponto?
Segunda: o limite quando x tende a a existe? Lembre: os laterais precisam ser iguais.
Terceira: o valor f de a é igual ao limite?
Se as três respostas forem sim, a função é contínua. Se qualquer uma for não, ela não é contínua.
E quando pedem para tornar a função contínua, a resposta é: defina f de a igual ao valor do limite.
Exemplo: f de x é x ao quadrado menos nove, tudo dividido por x menos três, quando x é diferente de três. E f de três vale cinco. A função é contínua em três?
Primeira pergunta: f de três existe? Sim, vale cinco.
Segunda: o limite existe? Já calculamos esse limite. Fatorando, dá seis. Existe.
Terceira: são iguais? f de três é cinco, e o limite é seis. Não são iguais.
Então f não é contínua em três. Para tornar contínua, f de três deveria valer seis, que é o valor do limite.
PERGUNTA: Uma função F tem limite dois quando x tende a um, mas F de um vale três. F é contínua em um? Quanto F de um deveria valer?
RESPOSTA: Não é contínua, porque o valor três é diferente do limite dois. Para ser contínua, F de um deveria valer dois.
PERGUNTA: Aquela função S, que vale x mais três antes de dois e x ao quadrado a partir de dois, é contínua em dois?
RESPOSTA: Não. Os laterais dão cinco e quatro, então o limite não existe, e a segunda pergunta já falha.
Ideia-chave: contínua é quando f de a existe, o limite existe, e os dois são iguais.

## Abertura do áudio extra {extra}

Olá! Este é o áudio extra só de limite no infinito, para você repetir quantas vezes quiser.
Depois de cada pergunta você tem cinco segundos para responder de cabeça. Depois do sinal, eu falo a resposta.

## Limite no infinito {principal, extra}

Agora vamos para o assunto mais importante: limite no infinito. Vamos com calma.
Até agora, x chegava perto de um número. Agora, x vai crescer sem parar. Dez, mil, um milhão, um bilhão.
A pergunta é: quando x fica gigante, para onde vai a função?
Tudo começa com uma ideia base: um número fixo dividido por algo gigante vira quase zero.
Veja em voz alta. Um dividido por dez dá zero vírgula um.
Um dividido por mil dá zero vírgula zero zero um.
Um dividido por um milhão dá zero vírgula zero zero zero zero zero um. Praticamente nada.
Quanto maior o de baixo, menor o resultado. Ele vai encostando no zero.
Por isso, cinco sobre x vai para zero quando x vai para infinito. Três sobre x ao quadrado também vai para zero.
Número fixo em cima, coisa gigante embaixo: zero.
A segunda ideia é: olhe só o maior expoente.
Quando x é gigante, o termo de maior expoente manda, e os outros ficam desprezíveis.
Veja com x igual a mil. x ao quadrado dá um milhão. Três x dá só três mil.
Três mil perto de um milhão é quase nada. É como uma moeda perto de uma pilha de dinheiro.
E quanto maior o x, mais o termo de maior expoente domina.
Chamamos o maior expoente de grau. x ao quadrado tem grau dois. x ao cubo tem grau três. Cinco x tem grau um. Um número sozinho tem grau zero.
Numa fração, compare o grau de cima com o grau de baixo. São três regras.
Regra um: grau de cima igual ao grau de baixo. O limite é a divisão dos números que acompanham os maiores expoentes.
Por quê? Porque os termos de maior grau dominam, e os x ao quadrado de cima e de baixo se cancelam. Sobram só os números da frente.
Por exemplo, seis x ao quadrado mais x, tudo dividido por dois x ao quadrado mais três: seis dividido por dois, dá três.
Regra dois: grau de cima maior. O limite vai para mais infinito ou para menos infinito.
Por quê? Porque o de cima cresce muito mais rápido que o de baixo. A divisão fica cada vez maior.
Regra três: grau de cima menor. O limite vai para zero.
Por quê? Porque o de baixo cresce muito mais rápido. Fica parecido com um número fixo dividido por algo gigante.
Por exemplo, doze, tudo dividido por t mais três. Em cima o grau é zero, embaixo é um. Vai para zero.
E cinco x mais um, tudo dividido por x ao quadrado mais quatro. Grau um em cima, grau dois embaixo. Vai para zero.
Decore esta frase: Igual, divide os da frente. Cima maior, infinito. Baixo maior, zero.
Vou repetir: Igual, divide os da frente. Cima maior, infinito. Baixo maior, zero.
Primeiro exemplo resolvido. Limite quando x tende a infinito de seis x ao quadrado mais x, tudo dividido por dois x ao quadrado mais três.
Passo um: acho o grau de cima. O maior expoente em cima é dois, por causa do seis x ao quadrado.
Passo dois: acho o grau de baixo. Também é dois, por causa do dois x ao quadrado.
Graus iguais. Então uso a regra um: divido os números da frente.
O x sozinho em cima e o três embaixo ficam desprezíveis quando x é gigante.
Sobra seis x ao quadrado sobre dois x ao quadrado. Os x ao quadrado se cancelam, e fica seis dividido por dois, que dá três.
O limite é três. E isso quer dizer que a assíntota horizontal é y igual a três.
Segundo exemplo. Limite quando x tende a infinito de x ao cubo menos oito, tudo dividido por x ao quadrado mais um.
Grau de cima: três. Grau de baixo: dois. O de cima é maior.
Pela regra dois, vai para infinito. Mas qual infinito? O termo que manda em cima é x ao cubo, positivo. Embaixo manda x ao quadrado, positivo. Positivo sobre positivo.
Então vai para mais infinito, porque o de cima cresce muito mais rápido que o de baixo.
Como deu infinito, essa função não tem assíntota horizontal.
Agora um caso que aparece muito: um número somado do lado de fora da fração.
Terceiro exemplo. Limite quando t tende a infinito de dois mais seis, tudo dividido por t mais um.
Separo as partes. O dois está do lado de fora, sozinho. Ele não muda, continua dois.
A fração seis sobre t mais um tem número fixo em cima e algo gigante embaixo. Ela vai para zero.
Então fica dois mais zero, que é dois. O limite é dois.
Agora, a assíntota horizontal. Se o limite no infinito dá um número L, a assíntota horizontal é y igual a L.
No primeiro exemplo, y igual a três. No terceiro, y igual a dois. Se o limite dá infinito, não existe assíntota horizontal.
E se x for para menos infinito? Com graus iguais, a resposta é a mesma: divide os da frente.
Por exemplo, três x ao quadrado menos dois x, tudo dividido por x ao quadrado mais quatro, com x tendendo a menos infinito. Graus iguais, três dividido por um, dá três.
Isso funciona porque os x ao quadrado continuam se cancelando, mesmo com x negativo.
Último cuidado: os números da frente podem ser negativos. Mantenha o sinal.
Por exemplo, menos quatro x ao quadrado mais um, tudo dividido por dois x ao quadrado menos x. Graus iguais. Menos quatro dividido por dois dá menos dois.
Na prova, escreva assim: Para x muito grande, os termos de maior grau dominam. O limite é seis x ao quadrado sobre dois x ao quadrado, que é três. Logo, a assíntota horizontal é y igual a três.
Agora, as perguntas sobre limite no infinito.
PERGUNTA: Calcule o limite quando x tende a infinito de quatro x ao quadrado menos três x mais um, tudo dividido por dois x ao quadrado mais cinco.
RESPOSTA: Dois. Os dois lados têm grau dois, então divide os da frente: quatro dividido por dois dá dois.
PERGUNTA: Calcule o limite quando x tende a infinito de sete x ao cubo mais dois, tudo dividido por x ao cubo menos cinco x.
RESPOSTA: Sete. Grau três em cima e grau três embaixo. O número da frente embaixo é um, e sete dividido por um dá sete.
PERGUNTA: Calcule o limite quando t tende a infinito de doze, tudo dividido por t mais três.
RESPOSTA: Zero. Número fixo em cima e algo gigante embaixo, porque o grau de baixo é maior.
PERGUNTA: Calcule o limite quando t tende a infinito de cinco mais dez, tudo dividido por t mais dois. E qual é a assíntota horizontal?
RESPOSTA: Cinco, e a assíntota horizontal é y igual a cinco. A fração vai para zero e sobra o cinco de fora.
PERGUNTA: O grau de cima é dois e o grau de baixo é três. Para onde vai o limite no infinito?
RESPOSTA: Para zero, porque o grau de baixo é maior, e o de baixo cresce mais rápido.
PERGUNTA: O grau de cima é três e o grau de baixo é dois. Tem assíntota horizontal?
RESPOSTA: Não tem. O grau de cima é maior, então o limite vai para infinito, e infinito não dá assíntota horizontal.
PERGUNTA: O limite no infinito deu quatro. Qual é a assíntota horizontal?
RESPOSTA: y igual a quatro. Quando o limite no infinito dá um número L, a assíntota horizontal é y igual a L.
Ideia-chave do limite no infinito: olhe só os maiores expoentes. Igual, divide os da frente. Cima maior, infinito. Baixo maior, zero.

## Encerramento do áudio extra {extra}

Fim do áudio de limite no infinito. Volte ao começo e repita até as respostas saírem rápido. Bons estudos!

## Como escrever na prova {principal}

Para fechar o conteúdo, vamos ver como escrever as respostas na prova.
Não basta o número. Escreva uma frase que diga o que o limite significa.
Num problema com contexto, use as unidades. Por exemplo: Quando t se aproxima de quatro minutos, a temperatura se aproxima de oito graus.
Quando os laterais são diferentes, escreva: O limite não existe, pois os limites laterais são diferentes.
Quando vai para infinito: Quando x se aproxima de um pela direita, a função cresce sem limitação, e x igual a um é uma assíntota vertical.
Na continuidade: A função não é contínua em dois, pois o limite não existe. Ou então: não é contínua, pois f de um é diferente do limite.
No infinito: Quando x cresce sem parar, a função se aproxima de três, logo a assíntota horizontal é y igual a três.
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
Denominador ao quadrado é sempre positivo.
Onde o denominador zera, há assíntota vertical.
Função com duas regras: a esquerda usa o menor que, a direita usa o maior ou igual. Se forem iguais, o limite existe.
Contínua: f de a existe, o limite existe, e os dois são iguais.
No infinito: Igual, divide os da frente. Cima maior, infinito. Baixo maior, zero.
Número somado do lado de fora continua lá.
Limite no infinito igual a L dá assíntota horizontal y igual a L.

## Quiz final {principal}

Agora, o quiz final, misturando tudo. São oito perguntas. Lembre: cinco segundos para responder de cabeça.
PERGUNTA: Calcule o limite quando x tende a quatro de x ao quadrado menos dezesseis, tudo dividido por x menos quatro.
RESPOSTA: Oito. Deu zero sobre zero. Pela diferença de quadrados, fica x menos quatro, vezes x mais quatro. Corta e sobra quatro mais quatro, que dá oito.
PERGUNTA: Calcule o limite quando x tende a infinito de cinco x mais um, tudo dividido por x ao quadrado mais quatro.
RESPOSTA: Zero. O grau de baixo, dois, é maior que o de cima, um.
PERGUNTA: Onde fica a assíntota vertical de dois, tudo dividido por x mais cinco?
RESPOSTA: Em x igual a menos cinco, porque é onde o denominador zera e o de cima não.
PERGUNTA: Calcule o limite quando x tende a infinito de menos quatro x ao quadrado mais um, tudo dividido por dois x ao quadrado menos x.
RESPOSTA: Menos dois. Graus iguais, então divide os da frente mantendo o sinal: menos quatro dividido por dois.
PERGUNTA: Deu zero sobre zero e a expressão tem raiz quadrada. Qual técnica você usa?
RESPOSTA: O conjugado. Quando aparece raiz quadrada com zero sobre zero, multiplica pelo conjugado.
PERGUNTA: Calcule o limite quando x tende a três de x ao quadrado mais nove, tudo dividido por x mais três.
RESPOSTA: Três. Substituindo, dá dezoito sobre seis, que é três. É caso um, e x ao quadrado mais nove nunca zera.
PERGUNTA: Calcule o limite quando x tende a menos infinito de três x ao quadrado menos dois x, tudo dividido por x ao quadrado mais quatro.
RESPOSTA: Três. Com graus iguais, a resposta no menos infinito é a mesma: três dividido por um.
PERGUNTA: Uma função vale x mais um quando x é menor que dois, e vale três x menos três quando x é maior ou igual a dois. Ela é contínua em dois?
RESPOSTA: Sim. Os dois laterais dão três, então o limite é três, e o valor no ponto, pela regra do maior ou igual, também é três.

## Encerramento {principal}

Fim da aula de limites. Se errou alguma pergunta, volte no bloco dela e escute de novo. Bons estudos!
