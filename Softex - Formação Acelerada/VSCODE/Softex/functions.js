num1 = 2;
num2 = 4;

function semparametro() {}

function soma() {
  num1 + num2;
}

const calculo = (subtrai, [num3, num4] = [10, 5]) =>
  `Resultado é ${num3} ${subtrai} ${num4}`;

console.log(calculo('-'));
