package ciclo2.variables;

import java.util.Scanner;

/**
 *
 * @author Alejandro Sánchez, jasanchez@unal.edu.co
 */
public class EsMayorQue18 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese su edad: ");
        int edad = scanner.nextInt();

        if (edad >= 18) {
            System.out.println("Ud. es mayor de edad !");
        } else {
            System.out.println("Ud. es es menor de edad");
        }
    }
}
