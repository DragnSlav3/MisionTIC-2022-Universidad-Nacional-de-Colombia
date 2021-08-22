package reto3ciclo2;

import java.util.*;

public class Laminas {

    public static ArrayList<Integer> identificarCategorias(ArrayList<Integer> listaCategorias) {
        ArrayList<Integer> salida = new ArrayList<>();

        for (int i = 0; i < listaCategorias.size(); i++) {
            if (!salida.contains(listaCategorias.get(i))) {
                salida.add(listaCategorias.get(i));
            }
        }
        return salida;
    }

    public static ArrayList<Integer> identificarCategoriaLaminasFaltantes(
                                    ArrayList<Integer> listaLaminasFaltantes, 
                                    ArrayList<Integer> listaCategorias, 
                                    int categoria) {
        
        ArrayList<Integer> coincidentes = new ArrayList<>();
        
        for (int i = 0; i < listaCategorias.size(); i++){
            if (listaCategorias.get(i).equals(categoria) ){
                coincidentes.add(i);
            }
        }
        
        ArrayList<Integer> salida = new ArrayList<>();
        for (int i=0; i< listaLaminasFaltantes.size(); i++){
            if (coincidentes.contains(listaLaminasFaltantes.get(i))){
                salida.add(listaLaminasFaltantes.get(i));
            }
        }
        return salida;
}

    public static ArrayList<Integer> identificarLaminasRelevantes(
                                               ArrayList<Integer> laminasFamilia,
                                               ArrayList<Integer> laminasOtraFamilia) {
        
        ArrayList<Integer> salida = new ArrayList<>();
        for (Integer lamina : laminasFamilia) {
            if (!laminasOtraFamilia.contains(lamina)) {
                salida.add(lamina);
            }
        }
        return salida;
    }

    public static Integer identificarNumeroLaminasParaCambiar(
                                           ArrayList<Integer> laminasFamilia,
                                           ArrayList<Integer> laminasOtraFamilia) {
        
        ArrayList<Integer> listaA = new ArrayList<>();
        ArrayList<Integer> listaB = new ArrayList<>();
        Integer salida;

        for (Integer lamina : laminasFamilia) {
            if (!laminasOtraFamilia.contains(lamina)) {
                listaA.add(lamina);
            }
        }

        for (Integer lamina : laminasOtraFamilia) {
            if (!laminasFamilia.contains(lamina)) {
                listaB.add(lamina);
            }
        }

        if (listaA.size() < listaB.size()) {
            salida = listaA.size();
        } else {
            salida = listaB.size();
        }
        return salida;
    }
}