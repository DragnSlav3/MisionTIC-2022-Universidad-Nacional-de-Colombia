/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package reto1ciclo2;

import java.util.Scanner;

/**
 *
 * @author Germán y Lady
 */
public class Reto1Ciclo2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here

        Scanner input = new Scanner(System.in);
        int riesgo1 = input.nextInt();
        int riesgo2 = (riesgo1 * 2) + 4;
        int riesgo3 = (riesgo1 + riesgo2) / 5;

        System.out.println(riesgo1 + " " + riesgo2 + " " + riesgo3);

        if (riesgo3 >= 0 && riesgo3 <= 20) {
            System.out.println("uno");
        } else if (riesgo3 < 30) {
            System.out.println("dos");
        } else if (riesgo3 < 50) {
            System.out.print("tres");
        } else {
            System.out.println("cuatro");
        }

    }

}
