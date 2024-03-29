package calc;

import javax.jws.WebService;

// SIB - Service Implementation Bean

// A propriedade endpointInterface faz com que a classe atual, a SIB, ligue-se com a SEI
// especificada anteriormente (calc.CalculadoraServer).
@WebService(endpointInterface = "calc.calculadoraServer")
public class calculadoraServerImpl implements calculadoraServer {

  public float soma(float num1, float num2) {
    return num1 + num2;
  }

  public float subtracao(float num1, float num2) {
    return num1 - num2;
  }

  public float multiplicacao(float num1, float num2) {
    return num1 * num2;
  }

  public float divisao(float num1, float num2) {
    return num1 / num2;
  }

}