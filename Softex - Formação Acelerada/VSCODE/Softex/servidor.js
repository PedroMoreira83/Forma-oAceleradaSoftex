const http = require('http');
const url = require('url');
const PORTA = process.PORT || 8080;

const servidor = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  if (req.url == '/') {
    res.write('<h1>Olá, Mundo!</h1>');
  } else if (req.url == '/teste1') {
    res.write('<h1>Teste 1</h1>');
  }
  if (req.url == '/teste2') {
    res.write('<h1>Teste 2</h1>');
  }

  const q = url.parse(req.url, true).query;
  res.write('<br/>' + q.nome);
  res.write('<br/>' + q.apelido);

  res.end();
});

servidor.listen(PORTA, () => {
  console.log(`Servidor Iniciado na porta ${PORTA}`);
});
