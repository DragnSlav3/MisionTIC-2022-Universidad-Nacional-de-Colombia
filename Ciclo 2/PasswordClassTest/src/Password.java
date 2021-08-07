
public class Password {

    int len;
    String pass;

    /*
    Constructor con un valor de atributo asignado por el usuario
     */
    public Password(int len) {
        this.len = len;
        this.pass = this.startPass(len);
    }

/*
    Constructor con un valor de atributo asignado por el usuario
     */
    public Password(String pass) {
        this.len = pass.length();
        this.pass = pass;
    }

    /*
    Constructor con valores de atributo predeterminados
    */
    public Password() {
        this.len = 8;
        this.pass = this.startPass(len);
    }

    /*
    Método privado que permite inicializar el atributo pass con caracteres aleatorios
     */
    private String startPass(int len) {
        this.len = len;
        String chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        String pass = "";
        for (int i = 0; i < len; i++) {
            pass += (chars.charAt((int) (Math.random() * chars.length())));
        }
        return pass;
    }

    /*
    Método público que permite cambiar la contraseña y establece el valor de len consecuentemente
     */
    public String changePassword(String newPassword) {
        this.pass = newPassword;
        this.len = newPassword.length();
        return pass;
    }

    /*
    Método que sobreescribe el método heredado de Object
     */
    @Override
    public String toString() {
        String strongOrNot;
        if (this.esFuerte() == false){
            strongOrNot = "Es una contraseña débil";
        }
        else {
            strongOrNot = "Es una contraseña fuerte";
        }
        
        return "Contraseña: " + pass
                + "\nLongitud: " + len
                + "\n" + strongOrNot;
    }

    public boolean esFuerte() {
        boolean strong;
        int upper = 0;
        int lower = 0;
        int number = 0;
        for (int i = 0; i < this.len; i++) {
            if ((int) this.pass.charAt(i) >= 65 && (int) this.pass.charAt(i) <= 90) {
                upper++;
            }
            if ((int) this.pass.charAt(i) >= 97 && (int) this.pass.charAt(i) <= 122) {
                lower++;
            }
            if ((int) this.pass.charAt(i) >= 48 && (int) this.pass.charAt(i) <= 57) {
                number++;
            }
        }

        if (upper >= 1 && lower >= 1 && number > 5) {
            strong = true;
        } else {
            strong = false;
        }

        return strong;
    }

}
