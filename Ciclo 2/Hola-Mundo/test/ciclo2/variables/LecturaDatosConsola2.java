/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ciclo2.variables;

// Se importa el paquete donde se encuentra Scanner
import java.util.Scanner;

/**
 *
 * @author Alejandro Sánchez, jasanchez@unal.edu.co
 */
public class LecturaDatosConsola2 {

    public static void main(String[] args) {
        // instancia del objeto Scanner
        Scanner sc = new Scanner(System.in);
        // leer datos de tipo long
        long l = Long.parseLong(sc.nextLine());
        // leer datos de tipo float
        float f = Float.parseFloat(sc.nextLine());
        // leer datos de tipo double
        double d = Double.parseDouble(sc.nextLine());
        // leer datos de tipo boolean
        boolean b = Boolean.parseBoolean(sc.nextLine());
        // leer datos de tipo char
        char c = sc.nextLine().charAt(0);
    }

}
