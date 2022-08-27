async () => {
  const database = require('./db');
  const Teste = require('./teste');
  await database.sync();

  const primeiroTeste = await Teste.create({
    x: 'Lorem',
    y: 100,
    z: 'Ipsum',
  });
  console.log(primeiroTeste);

  const testes = await Teste.findAll();
  console.log(testes);

  try {
    await sequelize.authenticate();
    console.log('Connection has been established successfully.');
  } catch (error) {
    console.error('Unable to connect to the database:', error);
  }
};
