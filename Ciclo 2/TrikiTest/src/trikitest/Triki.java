package trikitest;

import java.util.Arrays;

public class Triki {

    private char[][] tablero = this.startBoard();

    public Triki() {
    }

    private char[][] startBoard() {
        char[][] board = new char[3][3];
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                board[i][j] = 'a';
            }
        }
        return board;
    }

    public void marcarCasilla(String simbolo, int fila, int columna) {
        if (simbolo.equals("X") || simbolo.equals("O")) {
            this.tablero[fila][columna] = simbolo.charAt(0);
        } //else {
//            System.out.println("Caracter no válido");
//        }
//        System.out.println(this.toString());
    }
    
    /*
^^ Lo que está comentado arriba permite generar un aviso cuando se ingresa un caracter
diferente a X u O. Y la siguiente línea imprime el tablero en su estado actual cada vez
que se llama este método.
*/
    

    public char verificarCasilla(int fila, int columna) {
        char salida = this.tablero[fila][columna];
        return salida;
    }

    
    public char verificarGanador (){
        char ganador = 'a';
        char[] letra = new char [3];
        char[] X = {'X','X','X'};
        char[] O = {'O','O','O'};
        
        // FILAS
        for (int i = 0; i < this.tablero.length; i++){
            for (int j = 0; j < this.tablero[i].length; j++){
                letra[j] = this.tablero[i][j];
                }
            System.out.println("Filas, ciclo "+i+": "+ Arrays.toString(letra));
        }
        
        // COLUMNAS
        int indiceColumnas = 0;
        
        for (int i = 0; i < this.tablero.length; i++){
            for (int j = 0; j < this.tablero[i].length; j++){
                letra[j] = this.tablero[j][indiceColumnas];
                }
            indiceColumnas++;
            System.out.println("Columnas, ciclo "+i+": "+ Arrays.toString(letra));
            
            if (Arrays.equals(letra, X)){
            ganador = 'X';
            }
        else if (Arrays.equals(letra, O)){
            ganador = 'O';
            }
        else{
            ganador = 'a';
        }
        }
        
        
        // DIAGONALES
        // Diagonal 1
        for (int i = 0; i < this.tablero.length; i++){
            letra[i] = this.tablero[i][i];
        }
        System.out.println("Diagonal 1: " + Arrays.toString(letra));
        
        if (Arrays.equals(letra, X)){
            ganador = 'X';
            }
        else if (Arrays.equals(letra, O)){
            ganador = 'O';
            }
        else{
            ganador = 'a';
        }
        
        // Diagonal 2
        int indice1 = 0;
        int indice2 = this.tablero.length-1;
        for (int i = 0; i < this.tablero.length; i++){
            letra[i] = this.tablero[indice2][indice1];
            indice1++;
            indice2--;            
        }
        System.out.println("Diagonal 2: " + Arrays.toString(letra));
        
        if (Arrays.equals(letra, X)){
            ganador = 'X';
            }
        else if (Arrays.equals(letra, O)){
            ganador = 'O';
            }
        else{
            ganador = 'a';
        }
        

        

        
        return ganador;
        
    }
        
        
   
    
    
    @Override
    public String toString() {
        String salida = "";
        for (int i = 0; i < this.tablero.length; i++) {
            salida += Arrays.toString(this.tablero[i]) + "\n";
        }
        return salida;
    }

}