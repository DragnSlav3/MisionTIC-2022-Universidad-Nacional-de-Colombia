
/**
 * @author Germán García Polanía
 * dragnslav3@gmail.com
 * MisionTic 2022 Universidad Nacional de Colombia
 * Grupo P5
 */
import java.util.*;

public class NuevoInventario1 {

    private static ArrayList<Computador> computadores = new ArrayList<>();
    private static String ingreso = "0";

    public static void adicionarComputador() {
        Computador nuevo;
        String[] ingresoSeparados = ingreso.split("&");

        if (ingresoSeparados[1].equalsIgnoreCase("portatil")) {
            nuevo = new Portatil(ingresoSeparados[2],
                                 ingresoSeparados[3],
                                 ingresoSeparados[4],
                                 ingresoSeparados[5],
                                 ingresoSeparados[6]);
            computadores.add(nuevo);
        }

        if (ingresoSeparados[1].equalsIgnoreCase("escritorio")) {
            nuevo = new Escritorio(ingresoSeparados[2],
                                   ingresoSeparados[3],
                                   ingresoSeparados[4],
                                   ingresoSeparados[5],
                                   ingresoSeparados[6]);
            computadores.add(nuevo);
        }
    }

    public static void listarComputadores() {
        System.out.println("***Inventario de computadores***");
        computadores.forEach(computador -> {
            System.out.println(computador);
        });
    }

    public static void procesarComandos() {
        Scanner sc = new Scanner(System.in);

        while (ingreso.charAt(0) != '3') {
            ingreso = sc.nextLine();

            if (ingreso.charAt(0) == '1') {
                adicionarComputador();
            }

            if (ingreso.charAt(0) == '2') {
                listarComputadores();
            }
        }
    }

    public static void main(String[] args) {

        procesarComandos();
    }
}
