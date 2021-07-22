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
public class ConversionTiposNumericos {

    public static void main(String[] args) {
        //De entero a real
        int n1 = 1;
        double x1 = n1;
        double y1 = 0;
        double z1 = -2;
        System.out.println("n1="+ n1 + "x1=" + x1 + "y1=" + y1 + "z1=" + z1);
        //De real a entero
        double x2 = 1.0;
        double y2 = -2.5;
        int n2 = (int)x2;
        int m = (int)y2;
        int p = (int)3.14159265;
        System.out.println("x2="+ x2 + "y2=" + y2 + "n2=" + n2 + "m=" + m + "p=" + p);
        /*
        Python:
        x2 = 1.0;
        y2 = -2.5;
        n2 = int(x2);
        m = int(y2);
        p = int(3.14159265);
        print("x2="+ str(x2) + "y2=" + str(y2) + "n2=" + str(n2) + "m=" + str(m) + "p=" + str(p));
        */
    }
}
