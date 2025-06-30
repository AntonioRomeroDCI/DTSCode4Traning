public class Programa063 {
    public static void main(String[] args) {
        System.out.print("Ingresa un número: ");
        int n = 13;
        int suma = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                suma += i;
            }
        }
        System.out.println("Suma de pares hasta " + n + ": " + suma);
    }
}