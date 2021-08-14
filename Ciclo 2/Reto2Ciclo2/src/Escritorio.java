/**
 *
 * @author Germán García Polanía
 * dragnslav3@gmail.com
 * MisionTic 2022 Universidad Nacional de Colombia
 * Grupo P5
 */
public class Escritorio extends Computador {

    public String tamano;

    public Escritorio(String código, String procesador, String memoria, String disco, String tamano) {
        super(código, procesador, memoria, disco);
        this.tamano = tamano;
    }
    
    @Override
    public String toString(){
        String salida= "\tComputador escritorio - Código: "+this.codigo+"\n"
                +"\tprocesador: "+this.procesador+" MHz"+"\n"
                +"\tmemoria: "+this.memoria+" GB"+"\n"
                +"\tdisco: "+this.disco+" GB"+"\n"
                +"\ttamaño pantalla: "+this.tamano+"'";
        return salida;

    }
}

