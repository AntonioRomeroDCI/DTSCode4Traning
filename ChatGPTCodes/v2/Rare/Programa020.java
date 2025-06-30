public class Programa020 {
    public static void main(String[] args) {
        System.out.print("Ingresa un número: ");
        int n = 10;
        int suma = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                suma += i;
            }
        }
        System.out.println("Suma de pares hasta " + n + ": " + suma);
    }
}