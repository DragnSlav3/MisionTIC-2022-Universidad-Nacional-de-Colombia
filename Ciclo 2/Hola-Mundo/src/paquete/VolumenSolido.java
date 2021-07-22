package paquete;

import java.util.Scanner;

public class VolumenSolido {

    public static float volumenSolido(float r1, float h, float r2) {
        double esfera = (Math.PI * ((float) 4 / 3) * Math.pow(r1, 3));
        double cono = ((Math.PI * Math.pow(r2, 2)) * h) / 3;
        return (float) (esfera + cono);
    }

    public static void main(String[] args) {

        /**
         * ********** Ingresando datos por consola
         *
         * Scanner input = new Scanner(System.in);
         *
         * System.out.print("Ingrese el radio de la esfera: ");
         *
         * float r1 = input.nextFloat();
         *
         * System.out.print("Ingrese la altura h del cono: "); float h =
         * input.nextFloat();
         *
         * System.out.print("Ingrese el radio r2 del cono: "); float r2 =
         * input.nextFloat();
         *
         * float volumen = volumenSolido(r1, h, r2);
         * System.out.println(volumen);
         */
        float r1 = 3;
        float h = (float) 9 / 2;
        float r2 = 4;

// volumen sólido
        System.out.print("Sólido: ");
        System.out.println(volumenSolido(r1, h, r2));

// Volumen esfera
        System.out.print("Esfera: ");
        System.out.println((Math.PI * ((float) 4 / 3)) * (Math.pow(3, 3)));

// Volumen Cono     ((pi * (r2 ** 2)) * h) / 3
        System.out.print("Cono: ");
        System.out.println((Math.PI * Math.pow(4, 2) * ((float) 9 / 2) / 3));
        
        System.out.println("Hola mundo");

    }
}
