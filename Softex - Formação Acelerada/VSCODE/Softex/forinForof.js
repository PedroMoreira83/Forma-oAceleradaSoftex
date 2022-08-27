let objeto = {
  a: 1,
  b: 2,
  c: 3,
};

listaprop = function () {
  for (var prop in objeto) {
    console.log('objeto.' + prop + ' = ' + objeto[prop]);
  }
};

listaelem = function () {
  for (const value of Object.entries(objeto)) {
    console.log(value);
  }
};

listaelem();
listaprop();
