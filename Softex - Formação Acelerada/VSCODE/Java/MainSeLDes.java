package VSCODE.Java;

import java.io.*;

public class Main {
  public static void main(String[] args) throws IOException, ClassNotFoundException {
    Atributos empresa = new Atributos();
    
    empresa.cliente = "Pedro"; 
    empresa.produto = "Plano Mensal";

    System.out.println(Atributos);

    ObjectOutputStream objectOutput = new ObjectOutputStream(new FileOutputStream(cliente: "teste"));
    Atributos empresa = objectOutput.writeObject(empresa);
    objectOutput.close();

    ObjectInputStream objectInput = new ObjectInputStream(new FileInputStream(cliente: "teste"));
    Atributos empresa = (Atributos) ObjectInputStream.readObject();
    objectInput.close();
  }
} 