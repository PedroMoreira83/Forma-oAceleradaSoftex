//Objeto
var obj = { a: 1, b: 2, c: 3 };

//Para prop (propriedade) in obj (objeto) faça
for (var prop in obj) {
  // ctrl+shift+k (para abrir o console no mozilla firefox)
  console.log('obj.' + prop + ' = ' + obj[prop]);
}
