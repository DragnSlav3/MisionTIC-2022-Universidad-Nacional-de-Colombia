

package paquete;

import java.util.Arrays;


public class TrikiPrueba {
    
    public static void main (String [] args){
        
        
        /*
        Aquí estoy tratando de construír el tablero de triki del ejercicio        
        */
        
        
        char[][] juego2 = new char [3][3];
        
        for (int i=0;i<juego2.length;i++){
            for (int j=0;j<juego2[0].length;j++){
                juego2[i][j]='a';
            }
        }
        
        
        
        for (int i=0;i<juego2.length;i++){
            System.out.println(Arrays.toString(juego2[i]));
            }
        }
        
        
        
        
    }


