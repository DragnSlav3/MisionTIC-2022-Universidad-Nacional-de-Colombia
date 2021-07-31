/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package stringstests;

/**
 *
 *
 */
public class TwoStrings {
    
    public static String cadenaPalindrome (String cadena){
        String nuevaCadena = "";
        for (int i = cadena.length()-1; i >= 0 ; i--){
            nuevaCadena += (cadena.charAt(i));
        }
        if (cadena.equals(nuevaCadena)){
            return "Sí es palíndrome";}
        else{
            return "No es palíndrome";
        }
    }
    
    public static boolean compararCadenas (String cadena1, String cadena2){
        boolean resultado;
        if (cadena1.equals(cadena2)){
            return resultado = true;
        }
        else{
            return resultado = false;
        }
    }
    
    public static String concatenarCadenas (String cadena1, String cadena2){
        String newString = cadena1 + cadena2;
        return newString;
    }
    
public static void main(String[] args) {
    
    String cadena1 = "loremipsumdolorsitamet";
    String cadena2 = "loremipsumdolorsitamet";
    System.out.println("cadena 1: " + cadena1);
    System.out.println("cadena 2: " + cadena2);
    System.out.println();
    
    
    System.out.println("compararCadenas");
    System.out.println("El resultado de comparar las dos cadenas es: " + compararCadenas(cadena1, cadena2));
    System.out.println();
    
    System.out.println("concatenarCadenas");
    String cadena3 = (concatenarCadenas(cadena1, cadena2));
    System.out.println(cadena3);
    System.out.println();
    
    System.out.println("cadenaPalindrome");
    String cadena4 = "anita lava la tina";
    System.out.println(cadenaPalindrome(cadena4));
    
}

}
