Algoritmo "ImparesInsertionSort"

Var
lo: vetor[0..10] de inteiro
a, p, aux:  inteiro

Inicio
Para a <-1 at� 10 faca
     Escreva ("digite o ", a, "o. Valor? ")
     Leia (lo[a])
Fimpara

Para a <-1 at� 9 faca
     para p <- a+1 ate 10 faca
          Se (lo[a] > lo[p]) entao
             aux <- lo[a]
             lo[a] <- lo[p]
             lo[p] <- aux
          Fimse
     Fimpara
Fimpara

Para a <-1 at� 10 faca
Escreva ("{", lo[a], "}")
Fimpara


Fimalgoritmo
