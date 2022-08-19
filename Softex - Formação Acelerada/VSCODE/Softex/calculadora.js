operacao = 'multiplicacao';
num1 = 2;
num2 = 4;
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
    console.log('Operação inválida');
  }
}

calc('multiplicacao', 2, 4);
console.log(
  `O resultado da operação ${operacao} entre ${num1} e ${num2} é ${resultado}`
);
