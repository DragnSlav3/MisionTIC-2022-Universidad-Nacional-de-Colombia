package stringstests;

import java.util.Scanner;

public class StringsTests {
    
    public static void cuentaLetras (char letra, String cadena){
        System.out.println("La cadena ingresada tiene " + cadena.length() + 
                " caracteres en total.");
        
        int contador = 0;
        
        for (int i = 0; i < cadena.length(); i++){
            if (cadena.charAt(i) == letra){
                contador++;            
            }
        }
        System.out.println("El caracter " + letra + " aparece " + contador + " veces en la cadena de texto.");
    }
    
    public static void soloLetras (String cadena){
        int contador = 1; //contador inicia en 1 porque cadena.lengt siempre va a ser -1
        for (int i = 0; i < cadena.length(); i++){ 
            if (cadena.charAt(i) >65 && cadena.charAt(i) <90
                    || cadena.charAt(i) >97 && cadena.charAt(i) <122){
                contador++;
            }
        }
        
        if (contador == cadena.length()){
            System.out.println("Todos los símbolos de la cadena corresponden a letras.");
            }
        else {
            System.out.println("Algunos de los símbolos de la cadena no son letras. Los espacios y puntos no cuentan como letras ;)");
        }
    }
    
    
    public static int cuentaConsonantes (String cadena){
        int contador = 1; //contador inicia en 1 porque cadena.lengt siempre va a ser -1
        for (int i = 0; i < cadena.length(); i++){ 
            if (cadena.charAt(i) >65 && cadena.charAt(i) <90
                    || cadena.charAt(i) >97 && cadena.charAt(i) <122){
                contador++;
            }
            if (cadena.charAt(i) == 'a' ||
                cadena.charAt(i) == 'e' ||
                cadena.charAt(i) == 'i' ||    
                cadena.charAt(i) == 'o' ||    
                cadena.charAt(i) == 'u'){
                    contador--;
            }
        }
        return contador;              
    }
    
    public static String invertirCadena (String cadena){
        String nuevaCadena = "";
        for (int i = cadena.length()-1; i >= 0 ; i--){
            nuevaCadena += (cadena.charAt(i));
        }
        return nuevaCadena;
    }
    
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);
        
        System.out.println("*** CADENA ***");
        String cadena = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.";
        //String cadena = "loremipsumdolorsitamet";
        System.out.println(cadena);
        
        System.out.println();
        System.out.println("cuentaLetras");
        System.out.print("Ingrese la letra a buscar: ");
        char letra = input.nextLine().charAt(0);
        cuentaLetras(letra, cadena);
        
        System.out.println();        
        System.out.println("soloLetras");
        soloLetras(cadena);
        
        System.out.println();        
        System.out.println("cuentaConsonantes");
        System.out.println("Total de consonantes de la cadena: " + cuentaConsonantes(cadena));
        
        System.out.println();        
        System.out.println("invertirCadena");
        String newString = invertirCadena(cadena);
        System.out.println(newString);
    }
    
}
