package Code.ChatGPT.v2.Refactored;

public class Programa003 {
    public static void main(String[] args) {
        int n = 13;
        System.out.println("¿Es primo? " + esPrimo(n));
    }

    public static boolean esPrimo(int n) {
        if (n <= 1) return false;
        for (int i = 2; i < n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}