public class Main {


    public static void main(String[] args) {
        // TODO code application logic here
        
        Password pass1 = new Password();
        System.out.println(pass1);
        
        System.out.println();
        pass1.changePassword("DragnSlav3");
        System.out.println(pass1);
        
        System.out.println();
        Password pass2 = new Password(30);
        System.out.println(pass2);
        
        System.out.println();
        System.out.print(pass2.esFuerte());
        System.out.println();
        
        
    }
    
}
