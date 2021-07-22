/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ciclo2.variables;

/**
 *
 * @author Alejandro Sánchez, jasanchez@unal.edu.co
 */
public class ExpresionesAritmeticasCorrectas {
    
    public static void main(String[] args) {   
        int m1 = 10;
        int m2 = 5;
        int r = 3;
        double F = 6.67384E-11 * ((m1 * m2) / (r * r));
        //double F = 6.67384e-11 * m1 * m2 / (r * r);
        //double F = (6.67384e-11 * m1 * m2) / (r * r);
        //double F = 6.67384E-11 * (m1 * m2) * (1 / (r * r));
        System.out.println("Fuerza gravitacional con m1=10, m2=5 y r=3 es: " + F);
    }
    
}
