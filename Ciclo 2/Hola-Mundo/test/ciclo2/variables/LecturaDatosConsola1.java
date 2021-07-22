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
public class LecturaDatosConsola1 {

    public static void main(String[] args) {

        // instancia del objeto Scanner
        Scanner sc = new Scanner(System.in);
        // leer datos de tipo byte
        byte b = Byte.parseByte(sc.nextLine());
        // leer datos de tipo short
        short s = Short.parseShort(sc.nextLine());
        // leer datos de tipo int
        int i = Integer.parseInt(sc.nextLine());
    }

}
