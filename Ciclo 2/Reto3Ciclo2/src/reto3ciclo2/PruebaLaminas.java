package reto3ciclo2;

import java.util.*;

public class PruebaLaminas {

    public static ArrayList<Integer> array2aList(int[] lista) {
        ArrayList<Integer> salida = new ArrayList<>();
        for (int numero : lista) {
            salida.add(numero);
        }
        return salida;
    }

    public static void main(String[] args) {
        
        //**********************************************************************
        System.out.println("identificarCategorias");
        int[] arrayListaCategorias = {1, 2, 2, 2, 3, 3, 1, 5, 4, 7, 2, 2, 2, 4};
        ArrayList<Integer> listaCategorias = array2aList(arrayListaCategorias);
        System.out.println(Laminas.identificarCategorias(listaCategorias));
        System.out.println();

        //**********************************************************************
        System.out.println("identificarCategoriaLaminasFaltantes - Ejemplo 1");

        int[] arrayListaLaminasFaltantes1 = {1, 4, 6, 9};
        ArrayList<Integer> listaLaminasFaltantes1 = array2aList(arrayListaLaminasFaltantes1);

        int[] arrayListaCategorias1 = {1, 1, 4, 2, 6, 4, 1, 4, 5, 6, 7, 5};
        ArrayList<Integer> listaCategorias1 = array2aList(arrayListaCategorias1);

        int categoria1 = 6;

        System.out.println(Laminas.identificarCategoriaLaminasFaltantes(listaLaminasFaltantes1, listaCategorias1, categoria1));
        System.out.println();
        
        //**********************************************************************
        System.out.println("identificarCategoriaLaminasFaltantes - Ejemplo 2");

        int[] arrayListaLaminasFaltantes2 = {2, 4, 5};
        ArrayList<Integer> listaLaminasFaltantes2 = array2aList(arrayListaLaminasFaltantes2);

        int[] arrayListaCategorias2 = {3, 1, 4, 6, 5, 3, 4, 2, 1};
        ArrayList<Integer> listaCategorias2 = array2aList(arrayListaCategorias2);

        int categoria2 = 3;

        System.out.println(Laminas.identificarCategoriaLaminasFaltantes(listaLaminasFaltantes2, listaCategorias2, categoria2));
        System.out.println();
        
        //**********************************************************************
        System.out.println("identificarLaminasRelevantes");
        
        int[] arrayLaminasFamilia = {1, 5, 8, 9, 10, 12};
        ArrayList<Integer> laminasFamilia = array2aList(arrayLaminasFamilia);
        
        int[] arrayLaminasOtraFamilia = {1, 3, 4, 6, 9, 10, 11};
        ArrayList<Integer> laminasOtraFamilia = array2aList(arrayLaminasOtraFamilia);
        
        System.out.println(Laminas.identificarLaminasRelevantes(laminasFamilia, laminasOtraFamilia));
        System.out.println();
        
        //**********************************************************************
        System.out.println("identificarNumeroLaminasParaCambiar - Ejemplo 1");
        
        int[] arrayLaminasFamilia1 = {1, 5, 8, 9, 10, 12};
        ArrayList<Integer> laminasFamilia1 = array2aList(arrayLaminasFamilia1);
        
        int[] arrayLaminasOtraFamilia1 = {1, 3, 4, 6, 9, 10, 11};
        ArrayList<Integer> laminasOtraFamilia1 = array2aList(arrayLaminasOtraFamilia1);
        
        System.out.println(Laminas.identificarNumeroLaminasParaCambiar(laminasFamilia1, laminasOtraFamilia1));
        System.out.println();
        
        //**********************************************************************
        System.out.println("identificarNumeroLaminasParaCambiar - Ejemplo 2");
        
        int[] arrayLaminasFamilia2 = {3,5,7,10,15,16};
        ArrayList<Integer> laminasFamilia2 = array2aList(arrayLaminasFamilia2);
        
        int[] arrayLaminasOtraFamilia2 = {4,10,5,8};
        ArrayList<Integer> laminasOtraFamilia2 = array2aList(arrayLaminasOtraFamilia2);
        
        System.out.println(Laminas.identificarNumeroLaminasParaCambiar(laminasFamilia2, laminasOtraFamilia2));System.out.println();

        //**********************************************************************
        System.out.println("identificarCategoriaLaminasFaltantes - ERROR RETO");

        int[] arrayListaLaminasFaltantesRETO = {82, 2, 63, 257, 0, 154, 96, 71, 
            88, 270, 271, 11, 37, 279, 218, 204, 73, 193, 12, 19, 79, 274, 150, 
            315, 262, 298, 266, 247, 192, 52, 294, 316, 334, 33, 113, 118, 324, 
            326, 162, 179, 207, 16, 97, 99, 6, 176, 107, 35, 227, 76, 51, 278, 
            236, 317, 23, 160, 57, 296, 105, 292, 132, 233, 322, 28, 306, 39, 
            163, 171, 149, 286, 177, 141, 78, 98, 330, 261, 336, 3, 194, 222, 
            304, 136, 27, 83, 139, 220, 221, 229, 293, 30, 74, 125, 72, 180, 
            142, 95, 350, 339, 280, 157, 173, 343, 50, 4, 87, 159, 344, 77, 86, 
            153, 120, 251, 282, 36, 7, 66, 60, 55, 41, 62, 203, 34, 338, 24, 
            246, 166, 197, 209, 152, 254, 191, 15, 342, 277, 85, 135, 208, 249, 
            144, 186, 140, 264, 112};
        ArrayList<Integer> listaLaminasFaltantesRETO = array2aList(arrayListaLaminasFaltantesRETO);

        int[] arrayListaCategoriasRETO = {5, 3, 4, 2, 5, 3, 4, 4, 3, 4, 1, 2, 1, 4, 
1, 3, 1, 1, 4, 4, 3, 2, 5, 1, 2, 5, 5, 1, 5, 5, 2, 1, 2, 4, 2, 4, 3, 2, 1, 5, 4,
 1, 5, 2, 1, 1, 1, 3, 2, 1, 1, 2, 1, 5, 2, 3, 2, 5, 4, 5, 5, 2, 5, 1, 1, 5, 2, 1
, 4, 5, 4, 4, 3, 1, 1, 3, 4, 2, 3, 1, 4, 1, 3, 5, 2, 2, 4, 3, 4, 4, 1, 4, 3, 2, 
1, 1, 3, 3, 2, 1, 5, 1, 1, 1, 4, 2, 4, 1, 3, 3, 5, 2, 2, 2, 5, 2, 4, 5, 1, 1, 1,
 3, 3, 2, 3, 1, 3, 5, 5, 4, 5, 2, 4, 4, 1, 3, 1, 3, 1, 2, 3, 4, 4, 3, 5, 3, 3, 4
, 3, 2, 3, 3, 2, 1, 3, 3, 4, 3, 5, 3, 5, 2, 1, 3, 2, 2, 2, 4, 5, 1, 5, 2, 1, 1, 
3, 2, 1, 3, 2, 3, 1, 2, 4, 4, 3, 5, 4, 2, 1, 5, 3, 1, 4, 4, 5, 1, 1, 4, 4, 5, 5,
 1, 1, 2, 2, 3, 4, 4, 2, 4, 1, 4, 1, 4, 1, 1, 5, 5, 2, 3, 5, 1, 4, 1, 4, 4, 5, 5
, 4, 4, 4, 1, 4, 5, 2, 1, 4, 1, 1, 3, 4, 2, 3, 4, 5, 2, 5, 4, 1, 1, 1, 4, 1, 5, 
1, 1, 2, 2, 3, 3, 1, 5, 4, 5, 4, 1, 2, 4, 4, 4, 3, 2, 4, 3, 4, 2, 2, 5, 4, 4, 5,
 1, 2, 2, 3, 5, 1, 3, 3, 1, 4, 5, 3, 1, 4, 4, 2, 3, 3, 3, 4, 3, 5, 4, 5, 5, 3, 1
, 1, 2, 3, 2, 3, 1, 4, 1, 1, 1, 2, 3, 3, 4, 2, 3, 2, 1, 4, 5, 5, 2, 1, 1, 1, 2, 
5, 2, 1, 1, 2, 1, 5, 2, 2, 1, 1, 5, 3, 4, 3, 1, 4, 5};
        ArrayList<Integer> listaCategoriasRETO = array2aList(arrayListaCategoriasRETO);

        int categoriaRETO = 2;

        System.out.println(Laminas.identificarCategoriaLaminasFaltantes(listaLaminasFaltantesRETO, listaCategoriasRETO, categoriaRETO));
    }
}
