public class Persona {

    String nombre;
    int edad;
    char genero;
    double peso;
    double altura;

  
    public Persona(String nombre, int edad, char genero, double peso, double altura) {
        this.nombre = nombre;
        this.edad = edad;
        this.genero = genero;
        this.peso = peso;
        this.altura = altura;
    }

    public double calcularIMC(){
        double alturaEnMt = altura / 100;
        double imc = peso / (alturaEnMt * alturaEnMt);
        return imc;
    }
    
    public boolean esMayorDeEdad (){
        boolean esMayor = edad >= 18;
        return esMayor;
    }
    
    @Override
    public String toString (){
        String cadena = "Nombre: " + nombre + 
                "\nEdad: " + edad + " años" +
                "\nGénero: " + ((genero == 'H')? "Hombre":"Mujer") + 
                "\nPeso: " + peso + " kilos" + 
                "\nAltura: " + altura + " centímetros";
        return cadena;
    }
}
