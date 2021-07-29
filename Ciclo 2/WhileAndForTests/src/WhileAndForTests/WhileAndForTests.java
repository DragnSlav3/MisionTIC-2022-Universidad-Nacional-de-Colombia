package WhileAndForTests;

import java.util.Scanner;

public class WhileAndForTests {

    public static void numerosAlCuadradoWhile() {
        int valorInicial = 1;
        while (valorInicial <= 100) {
            System.out.println(valorInicial + " - " + Math.pow(valorInicial, 2));
            valorInicial += 1;
        }

    }
    
    public static void numerosAlCuadradoFor(){
        for (int i = 1; i <= 100; i++ ){
            System.out.println(i + " - " + ((int)Math.pow(i, 2)));
        }
    }

    public static void tablasMultiplicarWhile() {
        int numeroA = 0;
        while (numeroA < 9) {
            numeroA += 1;
            int numeroB = 1;
            while (numeroB < 11) {
            int numeroC = numeroA*numeroB;
            System.out.println(numeroA + " x " + numeroB + " = " + numeroC);
            numeroB += 1;
            }
        }
    }

    public static void tablasMultiplicarFor(){
        for (int i=1; i<=10;i++){
            for (int j=1; j<=10; j++){
                System.out.println(i+" x "+j+" = "+i*j);               
            }
        }
    }
    
    
    public static void main(String[] args) {


System.out.println("numerosAlCuadradoWhile");
numerosAlCuadradoWhile();

System.out.println("\nnumerosAlCuadradoFor");
numerosAlCuadradoFor();

System.out.println("\ntablasMultiplicarWhile");
tablasMultiplicarWhile();

System.out.println("\ntablasMultiplicarFor");
tablasMultiplicarFor();
       
    }

}
