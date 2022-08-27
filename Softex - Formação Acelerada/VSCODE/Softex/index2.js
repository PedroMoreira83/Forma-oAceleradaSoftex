var express = require('express');

var app = express();

app.listen(8888);

app.get('/user', (request, response) => {
  return response.send('Olá, Mundo!');
});

app.post('/', function (req, res) {
  return res.send('Obteve uma solicitação "POST"');
});

app.put('/user', function (req, res) {
  res.send('Obteve uma solicitação "PUT" em /user');
});

app.delete('/user', function (req, res) {
  res.send('Obteve uma solicitação "DELETE" em /user');
});
