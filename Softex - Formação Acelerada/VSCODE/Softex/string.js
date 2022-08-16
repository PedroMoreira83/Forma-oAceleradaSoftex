const num = 500;
console.log(num.toString()); //'500'
console.log(typeof num);
console.log(typeof num.toString());

// concatenando

let nome = 'Pedro ';
let sobreNome = 'Moreira';
let nomeCompleto = 'Meu nome completo é : ' + nome + sobreNome;
console.log(nomeCompleto);

// interpolando

let nome1 = 'Pedro ';
let saudacoes = `Seja bem-vindo, ${nome1}!`;
console.log(saudacoes);

// Métodos

const palavra = 'A tuma de back da softex das segundas manhã é massa';
console.log(palavra.length);
console.log(palavra.charAt(3));
console.log(palavra[3]);
console.log(palavra.indexOf('a'));
console.log(palavra.toUpperCase());
console.log(palavra.toLowerCase());
console.log(palavra.slice(0, 11));
console.log(palavra.replace('back', 'front'));
console.log(palavra.split(' '));
console.log(palavra.trim());
