package trikitest;

public class Main {

    public static void main(String[] args) {

        Triki juego1 = new Triki();
        
        juego1.marcarCasilla("X", 0, 0);
        juego1.marcarCasilla("X", 0, 1);
        juego1.marcarCasilla("X", 0, 2);
                
        System.out.println(juego1);
        
        System.out.println(juego1.verificarCasilla(1, 0));
        
        System.out.println(juego1.verificarGanador());

  

    }

        

}
