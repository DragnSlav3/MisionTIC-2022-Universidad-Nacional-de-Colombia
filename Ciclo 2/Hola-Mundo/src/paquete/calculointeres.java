/*
Ayudando en un ejercicio a mi compañera @Leiza. Requería presentar
el Valor cuota en enteros
*/

package paquete;

import java.util.Scanner;

public class calculointeres {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese cantidad prestada: $ ");
        double v = sc.nextDouble();
        System.out.println("Ingrese cuotas: ");
        double p = sc.nextDouble();
        System.out.println("Ingrese interes (sin el %): ");
        double i = sc.nextDouble();

        double totalcr;
        double inter;
        double vcuota;

        inter = (v * i / 100) * p;
        totalcr = v * inter;
        vcuota = (v / p) + (v * i / 100);
        System.out.println("Total deuda: " + (int)totalcr);
        System.out.println("Valor cuota :" + (int)vcuota);
    }
}
