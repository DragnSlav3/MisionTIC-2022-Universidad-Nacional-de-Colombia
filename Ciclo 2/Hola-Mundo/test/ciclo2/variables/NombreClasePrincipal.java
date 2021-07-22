/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ciclo2.variables;

/**
 *
 * @author Alejandro Sánchez, jasanchez@unal.edu.co
 */
import java.util.Scanner;

public class NombreClasePrincipal {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un número:");
        int n = sc.nextInt();
        int m = n * 2;
        System.out.println("Resultado: " + m);

    }
}
