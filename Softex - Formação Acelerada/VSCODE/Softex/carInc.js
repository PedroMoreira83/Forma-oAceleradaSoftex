/* - implemente uma classe abstrata Veículo com um construtor padrão 
e os métodos clone e represent;
- o construtor da classe Veículo deve receber modelo, marca, 
cor e numeroRodas como parâmetros;
- crie pelo menos duas subclasses da classe Veículo, que acrescentem um ou mais atributos, 
por exemplo: carro que tem dois campos a mais, como numeroRodas e numPortas;
- desenvolva uma classe Aplicação que deve criar um array com seis veículos 
com dois tipos de veículos diferentes (subclasses), utilizando 
o método clone dos objetos para preencher o array;
- na classe Aplicação, implemente um método que retorne um array 
com o mesmo tamanho do array de veículos, onde cada elemento deve ser 
um clone dos elementos do array veículos;
- no final, deve imprimir na tela o retorno da função represent de cada elemento
 desse novo array de clones de veículos. */

let Veiculo = class {
  constructor(modelo, marca, cor, numeroRodas) {
    this.modelo = modelo;
    this.cor = cor;
    this.marca = marca;
    this.numeroRodas = numeroRodas;
  }
  clone(obj) {
    obj.__proto__;
  }

  represent() {
    console.log(`Modelo: ${this.modelo} || Marca: ${this.marca} || 
    Cor: ${this.cor} || Rodas: ${this.rodas}`);
  }
};

let carro = class extends Veiculo {
  constructor(modelo, marca, cor, numRodas, numPortas) {
    super(modelo, marca, cor, numRodas);
    this.numPortas = numPortas;

    let veiculoProtomodelo = {
      modelo: this.modelo,
      marca: this.marca,
      cor: this.cor,
      numeroRodas: this.numeroRodas,
      numeroDePortas: this.numPortas,
    };
    Veiculo.prototype.clone = function (obj) {
      obj.prototype = cloneCarro;
    };
    Veiculo.prototype.represent = function () {
      console.log(
        `Modelo: ${this.modelo} || Marca: ${this.marca} || Cor: ${this.cor} 
        || Rodas: ${this.numeroRodas} || Portas: ${this.numPortas}`
      );
    };
  }
};

function addInfoVeiculo() {
  Veiculo.call(this);
  (this.tipo = 'carro'), (this.numPortas = 4);
}

var fit = new carro('EXL', 'Honda', 'Vermelho', 4, 4);
fit.represent();
