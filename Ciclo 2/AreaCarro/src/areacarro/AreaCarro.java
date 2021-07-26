package areacarro;

import java.util.Scanner;

public class AreaCarro {

    public static double areaRectangulo(double base, double altura) {
        double area = base * altura;
        return area;
    }

    public static double areaCirculo(double radio) {
        double area = Math.PI * Math.pow(radio, 2);
        return area;
    }

    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);

        System.out.print("Ingrese la base b1 del primer rectángulo: ");
        double b1 = input.nextDouble();
        System.out.print("Ingrese la altura a1 del primer rectángulo: ");
        double a1 = input.nextDouble();
        System.out.print("Ingrese la base b2 del segundo rectángulo: ");
        double b2 = input.nextDouble();
        System.out.print("Ingrese la altura a2 del segundo rectángulo: ");
        double a2 = input.nextDouble();
        System.out.print("Ingrese el radio r1 de la primera rueda: ");
        double r1 = input.nextDouble();
        System.out.print("Ingrese el radio r2 de la primera rueda: ");
        double r2 = input.nextDouble();

        double rectangulo1 = areaRectangulo(b1, a1);
        double rectangulo2 = areaRectangulo(b2, a2);
        double circulo1 = areaCirculo(r1);
        double circulo2 = areaCirculo(r2);

        double areaTotal = rectangulo1 + rectangulo2 + circulo1 + circulo2;
        
        System.out.println(areaTotal);

    }

}
