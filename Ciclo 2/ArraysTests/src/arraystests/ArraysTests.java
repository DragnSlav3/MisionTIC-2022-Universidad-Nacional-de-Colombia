package arraystests;

import java.util.Arrays;


public class ArraysTests {
    

    public static int [] cerosAlFinal (int [] nameArray){
        int[] newArray = new int [nameArray.length];
        int cuentaNumeros = 0;
        int cuentaCeros = 0;
        
        for (int i = 0; i < nameArray.length; i++ ){
            if (nameArray[i] != 0){
                newArray[cuentaNumeros]=nameArray[i];
                cuentaNumeros++;
            }
            else{
                newArray[nameArray.length+cuentaCeros-1]=nameArray[i]; 
                // ^^ Escribe los ceros de atrás hacia adelante.
                cuentaCeros--;
            }
            
        }
        return newArray;
        
    }
    
    public static int valorMenor (int [][] A){
        int salida = 100;
        for (int i = 0; i < A.length; i++){
            for (int j=0; j < A[0].length;j++){
                if (A[i][j] < salida){
                    salida = A[i][j];
                }
            }
        }
        return salida;
    }
    
    public static int [] posicionMenor (int [][] A){
        int valorMenor = valorMenor(A);
        int iPosicionMenor = 0;
        int jPosicionMenor = 0;
        int[] salida = {iPosicionMenor, jPosicionMenor};
        
        for (int i = 0; i < A.length; i++){
            for (int j = 0; j < A[0].length; j++){
                if (A[i][j] == valorMenor){
                    salida[0] = i;
                    salida[1] = j;
                }
            }
        }
        return salida;
    }
    
    public static int valorMayor (int [][] A){
        int salida = 0;
        for (int i = 0; i < A.length; i++){
            for (int j=0; j < A[0].length;j++){
                if (A[i][j] > salida){
                    salida = A[i][j];
                }
            }
        }
        return salida;
    }
    
    public static int [] posicionMayor (int [][] A){
        int valorMayor = valorMayor(A);
        int iPosicionMenor = 0;
        int jPosicionMenor = 0;
        int[] salida = {iPosicionMenor, jPosicionMenor};
        
        for (int i = 0; i < A.length; i++){
            for (int j = 0; j < A[0].length; j++){
                if (A[i][j] == valorMayor){
                    salida[0] = i;
                    salida[1] = j;
                }
            }
        }
        return salida;
    }
    
    public static void main(String[] args) {
        
        System.out.println("*** CEROS AL FINAL ***");
        
        int[] array1 = {1, 6, 0, 7, -3, 8, 0, -2, 11};
        
        System.out.println(Arrays.toString(array1));
        System.out.println(Arrays.toString(cerosAlFinal(array1)));
        
        System.out.println();        
        
        int[] array2 = {0, 11, 36, 10, 0, 17, -23, 81, 0, 0, 12, 11, 0};
                       
        System.out.println(Arrays.toString(array2));
        System.out.println(Arrays.toString(cerosAlFinal(array2)));
        
        System.out.println();        
        
        
        
        System.out.println("Arreglo int 3 x 3 aleatorio:");
        int [][] array3x3 = new int [3][3];
        for (int i = 0; i < array3x3.length; i++){
            for (int j = 0; j < array3x3[0].length; j++){
                array3x3[i][j] = (int) (Math.random()*100);
            }
        }
        
        
        for (int i = 0; i < array3x3.length; i++){
            System.out.println(Arrays.toString(array3x3[i]));
        }
        
        System.out.println();
        System.out.println("*** MÍNIMO DE UN ARREGLO ***");
        System.out.println("Valor menor: " + valorMenor(array3x3));
        System.out.println("Posición menor: " + Arrays.toString(posicionMenor(array3x3)));
        
        System.out.println();
        System.out.println("*** MÁXIMO DE UN ARREGLO ***");
        System.out.println("Valor mayor: " + valorMayor(array3x3));
        System.out.println("Posición mayor: " + Arrays.toString(posicionMayor(array3x3)));
    }
}
