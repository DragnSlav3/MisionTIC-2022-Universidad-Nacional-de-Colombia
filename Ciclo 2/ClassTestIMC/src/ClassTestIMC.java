import java.util.Scanner;

public class ClassTestIMC {

    
//    public static void createPersona (String namePersona) {
//        Scanner sc = new Scanner(System.in);
//        String name = namePersona.toUpperCase();
//        System.out.print("Edad de " + namePersona + ": ");
//        int edad = sc.nextInt();
//        System.out.print("Género de " + namePersona + " (H/M): ");
//        char genero = sc.nextLine().charAt(0);
//        System.out.print("Peso de " + namePersona + " (en kilogramos): ");
//        double peso = sc.nextDouble();
//        System.out.print("Altura de " + namePersona + " (en centímetros): ");
//        double altura = sc.nextDouble();
//        
//        Persona name1 = new Persona (name, edad, genero, peso, altura);
//        
//}
    
    
    
    
    
    
    
    
    public static void main(String[] args) {
        // TODO code application logic here
        
        Persona german = new Persona ("Germán", 39, 'H', 62, 180);
        
        System.out.println(german.esMayorDeEdad());
        System.out.println(german.calcularIMC());
        System.out.println(german.toString());
        
        System.out.println();
        System.out.println(german);
        System.out.println();
        
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Nombre: ");
        String name = sc.nextLine();
        System.out.print("Edad de " + name + ": ");
        int edad = sc.nextInt();
        System.out.print("Género de " + name + " (H/M): ");
        char genero = sc.next().charAt(0);
        System.out.print("Peso de " + name + " (en kilogramos): ");
        double peso = sc.nextDouble();
        System.out.print("Altura de " + name + " (en centímetros): ");
        double altura = sc.nextDouble();
        
      
        
        
        Persona name1 = new Persona (name, edad, genero, peso, altura);
        
        System.out.println("*****");
        System.out.println(name1.esMayorDeEdad());
        System.out.println(name1.calcularIMC());
        System.out.println(name1.toString());
        
        
        
        
        
        
    }
    
}
