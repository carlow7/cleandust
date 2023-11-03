# cleandust


Turma: SIS201N01;
Participantes:
Carleson Kalebe da Silva Saquiray,
João Gabriel Ferreira Aguiar,
Carlos Eduardo dos Santos Cavalcante,
Vinicius Gabriel Oliveira Pontes,


*PEAS para o Sistema do Agente Aspirador com Interface Gráfica:*

*Medida de Desempenho:*
- *Limpeza eficiente:* Medida pela quantidade total de sujeira aspirada pelo agente. O desempenho ideal é manter o ambiente completamente limpo, com zero sujeira.
- *Capacidade da Bolsa de Sujeira:* O agente deve esvaziar a bolsa quando estiver cheia (com 10 unidades de sujeira) para continuar aspirando.

*Ambiente:*
- O ambiente é um grid 4x4 (16 locais) onde cada local pode estar limpo (0) ou sujo (1). A sujeira é distribuída aleatoriamente no início.
- O ambiente é dinâmico, pois o agente limpa a sujeira, alterando o estado do ambiente.

*Atuadores:*
- *Motores de movimentação:* Permitem que o agente se mova para cima, para baixo, para a esquerda ou para a direita no grid.
- *Mecanismo de sucção:* Permite que o agente aspire a sujeira presente no local atual.

*Sensores:*
- *Sensores de posição:* Informam a posição atual do agente no grid 4x4.
- *Sensores de sujeira:* Informam se o local atual está limpo ou sujo.
- *Nível de energia:* Indica a quantidade de energia restante para o agente.
- *Contador de Bolsa:* Indica quantas unidades de sujeira o agente coletou na bolsa.
