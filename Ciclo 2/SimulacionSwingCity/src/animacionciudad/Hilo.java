/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package animacionciudad;

import ciudad.Ciudad;
import ciudad.ParametrosDibujo;
import ciudad.Posicion;
import ciudad.Sitio;
import java.util.ArrayList;
import java.util.List;
import vehiculo.Automovil;
import vehiculo.Deportivo;
import vehiculo.Furgon;
import vehiculo.Platon;
import vehiculo.Vehiculo;

/**
 * Hilo utilizado para iniciar un proceso independiente
 * @author Camiku
 */
public class Hilo extends Thread {
    
    private PanelControles panelControles;
    // Práctica en clase, agregar botón parar
    private boolean parar;
    
    public Hilo(PanelControles panelControles) {
        this.panelControles = panelControles;
    }

    // Práctica en clase, agregar botón parar
    public void setParar(boolean parar) {
        this.parar = parar;
    }
    /**
     * Inicializa la ejecución de la aplicación de forma independiente
     */
    @Override
    public void run() {
        Automovil automovil = new Automovil(new Posicion(), 5);
        Deportivo deportivo = new Deportivo(new Posicion(), 5);
        Platon camioneta = new Platon(new Posicion(), 3, 4);
        camioneta.llevar(ParametrosDibujo.CONTENIDO_CARGA);
        Furgon furgon = new Furgon(new Posicion(2, 50), 3, 4);
        furgon.llevar(panelControles.getjTextFieldCarga().getText());

        List<Vehiculo> listaVehiculos = new ArrayList<Vehiculo>();

        if (panelControles.getjCheckBoxVehiculosCarga().isSelected()) {
            listaVehiculos.add(camioneta);
            listaVehiculos.add(furgon);
        }

        List<Sitio> listaSitios = new ArrayList<Sitio>();
        for (int i = 0; i < ParametrosDibujo.NUMERO_SITIOS; i++) {
            listaSitios.add(new Sitio(new Posicion()));
        }

        Ciudad ciudad = new Ciudad(listaVehiculos, listaSitios);
        
        // Práctica en clase, agregar botón parar
        parar = false;

        for (int i = 0; i < ParametrosDibujo.ITERACIONES_CIUDAD; i++) {
            if (panelControles.getjRadioButtonAdelante().isSelected()) {
                ciudad.mover();
            }
            panelControles.getjTextArea().setText(ciudad.pintar());
            try {
                sleep((Integer) panelControles.getjSpinnerDormir().getValue());
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            // Práctica en clase, agregar botón parar
            if(parar){
                i = ParametrosDibujo.ITERACIONES_CIUDAD;
            }
        }
        // Reactiva el boton de ejecución
        panelControles.getjButtonIniciar().setEnabled(true);
    }

    
}
