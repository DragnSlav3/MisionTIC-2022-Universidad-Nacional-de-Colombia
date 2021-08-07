public class Main {


    public static void main(String[] args) {
        
        /*
        Construyendo Password sin atributos asignados por usuario
        */
        Password pass1 = new Password();
        System.out.println(pass1);
        
        System.out.println();
        pass1.changePassword("DragnSlav3"); //Usando método changePassword
        System.out.println(pass1);
        
        /*
        Construyendo Password con atributo de longitud asignado por usuario
        */
        System.out.println();
        Password pass2 = new Password(30);
        System.out.println(pass2);
        
        System.out.println();
        System.out.print(pass2.esFuerte()); //Usando método esFuerte por separado
        System.out.println();
        
        /*
        Construyendo Password con atributo pass asignado por usuario
        */
        System.out.println();
        Password pass3 = new Password("PassWord012345");
        System.out.println(pass3);
    }
    
}
