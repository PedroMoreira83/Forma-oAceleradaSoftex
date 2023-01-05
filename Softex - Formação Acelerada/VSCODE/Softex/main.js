//import express from "express";

var express = require('express');

var app = express();

app.listen(8080);

app.get('/', (request, response) => {
  return response.send('Olá Mundo!');
});

app.post('/', function (req, res) {
  return res.send('Solicitação Recebida!');
});
