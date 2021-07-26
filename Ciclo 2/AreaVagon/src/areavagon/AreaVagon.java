package areavagon;

public class AreaVagon {

    public static double areaVagon(double radio, double base, double altura) {
        double areaRectangulo = base * altura;
        double areaCirculos = (Math.PI * Math.pow(radio, 2)) * 2;
        double areaTotal = areaRectangulo + areaCirculos;
        return areaTotal;

    }

    public static void main(String[] args) {
        // TODO code application logic here

        double base = 10;
        double altura = 20;
        double radio = 5.5;

        double salida = areaVagon(radio, base, altura);

        System.out.println(salida);

    }

}
