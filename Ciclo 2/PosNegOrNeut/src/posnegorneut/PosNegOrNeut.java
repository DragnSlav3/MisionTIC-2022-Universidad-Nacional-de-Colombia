/*
Dado un número real x, construya una función que permita
determinar si el número es positivo, negativo o cero. Para cada caso
se debe imprimir el texto que se especifica a continuación:
Positivo: "El número x es positivo"
Negativo: "El número x es negativo"
Cero (0): "El número x es el neutro para la suma"
 */
package posnegorneut;

import java.util.Scanner;

public class PosNegOrNeut {

    public static void main(String[] args) {
        float numero;
        Scanner input = new Scanner(System.in);
        System.out.print("Ingrese un número: ");
        numero = input.nextFloat();
        System.out.printf("El número %f es ", numero);

        if (numero == 0) {
            System.out.println("el neutro para la suma.");
        }
        else if (numero > 0)
        {
            System.out.println("positivo.");
        }
        else System.out.println("negativo.");
     

    }

}
