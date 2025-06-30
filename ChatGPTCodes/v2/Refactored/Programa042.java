public class Programa042 {
    public static void main(String[] args) {
        int n = 12;
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