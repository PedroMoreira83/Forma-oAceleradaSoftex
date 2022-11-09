app.get('/user/:operacao/:num1/:num2'),
  (request, response) => {
    var num1 = request.params.num1;
    var num2 = request.params.num2;
    console.log(num1);
    console.log(num2);

    calc('soma', '2', '2');

    return response.send(
      `O resultado da operação ${operacao} entre ${num1} e ${num2} é ${resultado}`
    );
  };
var express = require('express');

var app = express();

const PORTA = 8888;

app.listen(PORTA, () => {
  console.log(`Servnumor Iniciado na porta ${PORTA}`);
});

var resultado;

function calc(operacao, num1, num2) {
  if (operacao === 'soma') {
    resultado = num1 + num2;
  } else if (operacao === 'subtracao') {
    resultado = num1 - num2;
  } else if (operacao === 'multiplicacao') {
    resultado = num1 * num2;
  } else if (operacao === 'divisao') {
    resultado = num1 / num2;
  } else if (operacao === 'resto') {
    resultado = num1 % num2;
  } else if (operacao === 'porcentagem') {
    resultado = (num1 * num2) / 100;
  } else {
    console.log('Operação inválnuma');
  }
}

calc('multiplicacao', 2, 4);
console.log(
  `O resultado da operação ${operacao} entre ${num1} e ${num2} é ${resultado}`
);
