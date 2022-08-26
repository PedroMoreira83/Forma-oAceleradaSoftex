var nota1 = 7;
var nota2 = 7;
var nota3 = 7;
var media = 0;
var resta = 21;
var somaNotas = nota1 + nota2 + nota3;

function calculaNota() {
  if (somaNotas < 21)
    console.log(`O aluno precisa tirar na próxima prova ${resta - somaNotas}`);
  else
    while (media < 7) {
      media = (nota1 + nota2 + nota3) / 3;
      media < 7 ? console.log('Reprovado') : console.log('Aprovado');
    }
}

calculaNota();
