package reto3ciclo2;

import java.util.*;
//MÉTODO 2 ADAPTADO DE SERGIO
public class LaminasSergio {

    public static ArrayList<Integer> identificarCategoriaLaminasFaltantes(
                                    ArrayList<Integer> listaLaminasFaltantes, 
                                    ArrayList<Integer> listaCategorias, 
                                    int categoria) {
        
        ArrayList<Integer> salida = new ArrayList<>();
        
        for (int i = 0; i < listaLaminasFaltantes.size(); i++) {
            for (int j = 0; j < listaCategorias.size(); j++) {
                if (listaCategorias.get(listaLaminasFaltantes.get(i)) == categoria) {
                    salida.add(listaLaminasFaltantes.get(i));
                    break;         
            }
        }
    }
        return salida;
    }
}