/* Sistema de Banco

Os seus métodos devem ser: buscar saldo, depósito, saque e número da conta. 
Observações:
- buscar saldo deve retornar o valor atual do saldo;
- para o depósito, você deverá passar um valor como parâmetro
 e adicioná-lo no saldo final do objeto;
- para o saque, você deverá passar um valor como parâmetro 
e subtraí-lo no saldo final do objeto;
- o número da conta deve retornar o número da conta.*/

var contaBanco = {
  agencia: '0001',
  numConta: '5555',
  saldo: 200,
  tipoConta: 'Conta Corrente',
};

var buscaSaldo = function () {
  console.log(`Seu saldo agora é ${contaBanco.saldo}.`);
};
var checarNumConta = function () {
  console.log(`O número da sua conta é ${contaBanco.numConta}.`);
};
var depositoConta = function (valor) {
  contaBanco.saldo = contaBanco.saldo + valor;
  console.log(
    `Seu depósito foi de R$ ${valor}. Seu saldo agora é R$ ${contaBanco.saldo}.`
  );
};
var saqueConta = function (valor) {
  contaBanco.saldo = contaBanco.saldo - valor;
  console.log(
    `Seu saque foi de R$ ${valor}. Seu saldo agora é R$ ${contaBanco.saldo}.`
  );
};

checarNumConta();
depositoConta(100);
saqueConta(50);
buscaSaldo();
