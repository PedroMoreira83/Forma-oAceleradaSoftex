package VSCODE.Java;

import java.io.*;

public class Main {
  public static void main(String[] args) throws IOException, ClassNotFoundException {
    Atributos empresa = new Atributos( id: "9999999", cliente: "Pedro", documento: "55.555.555/0005-55", produto: "Plano Mensal", data: "05/08/2022");
    
    System.out.printf("O cliente %s tem o %s.", empresa.cliente, empresa.produto);

  }
} 