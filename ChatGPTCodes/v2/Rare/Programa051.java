package ChatGPTCodes.v2.Rare;

public class Programa051 {
    public static void main(String[] args) {
        System.out.print("Ingresa un número: ");
        int n = 61;
        boolean esPrimo = true;
        if (n <= 1) {
            esPrimo = false;
        } else {
            for (int i = 2; i < n; i++) {
                if (n % i == 0) {
                    esPrimo = false;
                    break;
                }
            }
        }
        System.out.println("¿Es primo? " + esPrimo);
    }
}