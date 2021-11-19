# Parentheses Check

# Desafio:

# Tech Challenge

A **DMCard** está em busca de pessoas incríveis que integrem nosso laboratório para criarmos incríveis produtos digitais, e gostaríamos de ter você aqui conosco.

Para iniciar o processo, pedimos um teste que não vai tomar muito do seu tempo e nos dará uma perspectiva da sua forma de resolver um algoritmo. Queremos entender seu nível de habilidade na construção de um algortimo.

# Requisitos do desafio

Dada uma expressão qualquer com parênteses, indique se a quantidade de parênteses está correta ou não, sem levar em conta o restante da expressão. Por exemplo:

a+(b*c)-2-a está correto
(a+b*(2-c)-2+a)*2 está correto

*enquanto*

(a*b-(2+c)    está incorreto
2*(3-a))      está incorreto
)3+b*(2-c)(   está incorreto

Ou seja, todo parênteses que fecha deve ter um outro parênteses que abre correspondente e não pode haver parênteses que fecha sem um previo parenteses que abre e a quantidade total de parenteses que abre e fecha deve ser igual.

Entrada
Como entrada, haverá N expressões (1 <= N <= 10000), cada uma delas com até 1000 caracteres.

Saída
O arquivo de saída deverá ter a quantidade de linhas correspondente ao arquivo de entrada, cada uma delas contendo as palavras correct ou incorrect de acordo com as regras acima fornecidas.


| Exemplo de Entrada     | Exemplo de Saída                                        |
| --------- | ---------------------------------------------- |
| a+(b*c)-2-a    | correct                                      |
| (a+b*(2-c)-2+a)*2  | correct                                     |
| (a*b-(2+c) | incorrect |
| 2*(3-a)) | incorrect                        |
| )3+b*(2-c)( | incorrect           |


* O tempo de execução do código, não pode ultrapassar 1 segundo.

# Como fazer?

- Sugerimos um prazo de 3 dias para a entrega. Caso precise de mais nos avise e Justifique.
- Você deve criar este algoritmo na linguagem de sua preferência, nós achamos Python legal.


Boa sorte!

# Solução:

Como solução foi pensado um código em python, onde uma linha é dada como input, e a função parentheses_check itera carácter por carácter, em ordem, e segue um de três caminhos para chegar a resposta:

1) Caso o carácter seja um parenteses fechado, é checkado em uma lista se algum parenteses aberto já havia sido encontrado na linha, caso a lista de parenteses abertos esteja vazia, a resposta "incorrect" é dada;
2) Caso algum haja parenteses aberto na lista de checkagem, este é removido da lista, pois seu parenteses correspondente foi encontrado;
3) Finalmente, caso a linha chegue ao fim, e não tenha sido encontrado qualquer parenteses fechado, sem antes ter seu correspondente aberto, é checkado a lista de parenteses aberto - caso esteja vazia, significa que todos os parenteses abertos foram devidamente fechados, e a resposta "correct" é dada; no entanto, se a lista não estiver vazia, significa que algum parenteses foi aberto sem ter sido fechado, e, portanto, a resposta "incorrect é dada".
