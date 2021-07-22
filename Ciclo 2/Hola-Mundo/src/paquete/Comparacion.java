/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package paquete;

import java.util.Scanner;

/**
 *
 * @author Germán y Lady
 */
public class Comparacion {

    public static void main(String[] args) {

        int num1, num2;

        System.out.print("Ingrese el primer número: ");

        Scanner input = new Scanner(System.in);

        num1 = input.nextInt();

        System.out.print("Ingrese el segundo número: ");

        num2 = input.nextInt();

        if (num1 == num2) {
            System.out.println(num1 + " == " + num2);
        }

        if (num1 != num2) {
            System.out.println(num1 + " != " + num2);
        }

        if (num1 > num2) {
            System.out.println(num1 + " > " + num2);
        }

        if (num1 >= num2) {
            System.out.println(num1 + " >= " + num2);
        }

        if (num1 < num2) {
            System.out.println(num1 + " < " + num2);
        }

        if (num1 <= num2) {
            System.out.println(num1 + " <= " + num2);
        }
    }

}
