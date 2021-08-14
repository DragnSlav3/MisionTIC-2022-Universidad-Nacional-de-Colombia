/**
 *
 * @author Germán García Polanía
 * dragnslav3@gmail.com
 * MisionTic 2022 Universidad Nacional de Colombia
 * Grupo P5
 */
public abstract class Computador {
    
    String codigo; 
    String procesador;
    String memoria;
    String disco;

    public Computador(String codigo, String procesador, String memoria, String disco) {
        this.codigo = codigo;
        this.procesador = procesador;
        this.memoria = memoria;
        this.disco = disco;
    }

}
