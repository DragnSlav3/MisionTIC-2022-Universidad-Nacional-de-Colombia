/**
 *
 * @author Germán García Polanía
 * dragnslav3@gmail.com
 * MisionTic 2022 Universidad Nacional de Colombia
 * Grupo P5
 */
import java.util.*;

public class Inventario {
    // Métodos o funciones

      
            
    public static void main(String[] args) {
        // Código

        Scanner sc = new Scanner(System.in);

        ArrayList<Computador> lista = new ArrayList<>();

        String ingreso = "0";

        Computador nuevo;

        while (ingreso.charAt(0) != '3') {
            ingreso = sc.nextLine();

            if (ingreso.length() > 1) {
                String[] ingresoSeparados = ingreso.split("&");

                String codigo = ingresoSeparados[2];
                String procesador = ingresoSeparados[3];
                String memoria = ingresoSeparados[4];
                String disco = ingresoSeparados[5];
                String colorOrPantalla = ingresoSeparados[6];

                if (ingreso.charAt(0) == '1') {
                    if (ingresoSeparados[1].equalsIgnoreCase("portatil")) {
                        nuevo = new Portatil(codigo, procesador, memoria, disco, colorOrPantalla);
                        lista.add(nuevo);
                        
                    }
                    if (ingresoSeparados[1].equalsIgnoreCase("escritorio")) {
                        nuevo = new Escritorio(codigo, procesador, memoria, disco, colorOrPantalla);
                        lista.add(nuevo);
                        }
                }

            }

            if (ingreso.charAt(0) == '2') {
                System.out.println("***Inventario de computadores***");
                for (Computador computador:lista){
                    System.out.println(computador);
                }
                }

        }
    }

}