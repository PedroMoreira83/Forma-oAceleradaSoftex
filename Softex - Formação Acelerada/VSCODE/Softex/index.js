//import express from "express";

var express = require('express');

var app = express();

app.listen(8080);

app.get('/', (req, res) => {
  return res.send('Recebi uma solicitação HTTP GET');
});

app.post('/', function (req, res) {
  return res.send('Recebi uma solicitação HTTP POST');
});

app.put('/', function (req, res) {
  res.send('Recebi uma solicitação HTTP PUT');
});

app.delete('/', function (req, res) {
  res.send('Recebi uma solicitação HTTP DELETE');
});
