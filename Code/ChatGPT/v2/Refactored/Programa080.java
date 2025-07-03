package Code.ChatGPT.v2.Refactored;

public class Programa080 {
    public static void main(String[] args) {
        int n = 10;
        System.out.println("Suma de pares hasta " + n + ": " + sumarPares(n));
    }

    public static int sumarPares(int n) {
        int suma = 0;
        for (int i = 2; i <= n; i += 2) {
            suma += i;
        }
        return suma;
    }
}