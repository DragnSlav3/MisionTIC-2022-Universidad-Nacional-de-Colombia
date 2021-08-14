/**
 * @author Germán García Polanía
 * dragnslav3@gmail.com
 * MisionTic 2022 Universidad Nacional de Colombia
 * Grupo P5
 */
import java.util.*;

public class NuevoInventario {
    
    public static void procesarComandos() {
        Scanner sc = new Scanner(System.in);
        ArrayList<Computador> lista = new ArrayList<>();
        Computador nuevo;

        while (true) {
            String ingreso = sc.nextLine();

            if (ingreso.charAt(0) == '1') {
                String[] ingresoSeparados = ingreso.split("&");

                if (ingresoSeparados[1].equalsIgnoreCase("portatil")) {
                    nuevo = new Portatil(ingresoSeparados[2],
                                         ingresoSeparados[3],
                                         ingresoSeparados[4],
                                         ingresoSeparados[5],
                                         ingresoSeparados[6]);
                    lista.add(nuevo);
                }

                if (ingresoSeparados[1].equalsIgnoreCase("escritorio")) {
                    nuevo = new Escritorio(ingresoSeparados[2],
                                           ingresoSeparados[3],
                                           ingresoSeparados[4],
                                           ingresoSeparados[5],
                                           ingresoSeparados[6]);
                    lista.add(nuevo);
                }
            }

            if (ingreso.charAt(0) == '2') {
                System.out.println("***Inventario de computadores***");
                for (Computador computador : lista) {
                    System.out.println(computador);
                }
            }

            if (ingreso.charAt(0) == '3') {
                break;
            }
        }
    }

    public static void main(String[] args) {
        procesarComandos();
    }
}