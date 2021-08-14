/*
Aquí estuve probando cómo reconocer las columnas para el ejercicio de triki
 */

package paquete;

import java.util.Arrays;





/**
 *
 * @author Germán y Lady
 */
public class generadorColumnas {
    
    
    public static void main (String[] args){
        
        int[][] tablero = new int[3][3];
        
        int numero = 1;
        for (int i=0; i< tablero.length; i++){
            for (int j=0; j<tablero[0].length; j++){
                tablero[i][j] = numero;
                numero++;
            }
        }
        
        
        for (int i=0; i< tablero.length; i++){
            System.out.println(Arrays.toString(tablero[i]));    
        }
        
        // COLUMNAS
        
        int[] letra = new int [3];
        int indiceColumnas = 0;
        
        for (int i = 0; i < tablero.length; i++){
            for (int j = 0; j < tablero[i].length; j++){
                letra[j] = tablero[j][indiceColumnas];
                }
            indiceColumnas++;
            System.out.println("Columnas, ciclo "+i+": "+ Arrays.toString(letra));
        }
        
        
        
        
        
        
    }

}
