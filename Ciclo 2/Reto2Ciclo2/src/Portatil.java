/**
 *
 * @author Germán García Polanía
 * dragnslav3@gmail.com
 * MisionTic 2022 Universidad Nacional de Colombia
 * Grupo P5
 */
public class Portatil extends Computador {
    
    public String color;

    public Portatil(String código, String procesador, String memoria, String disco, String color) {
        super(código, procesador, memoria, disco);
        this.color = color;
    }

    @Override
    public String toString(){
        String salida = "\tComputador portatil - Código: " + this.codigo+"\n"
                +"\tprocesador: "+this.procesador+" MHz"+"\n"
                +"\tmemoria: "+this.memoria+" GB"+"\n"
                +"\tdisco: "+this.disco+" GB"+"\n"
                +"\tcolor: "+this.color;
        return salida;
    }
    
}
