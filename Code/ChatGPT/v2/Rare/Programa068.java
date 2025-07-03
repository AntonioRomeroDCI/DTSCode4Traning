package Code.ChatGPT.v2.Rare;

public class Programa068 {
    public static void main(String[] args) {
        System.out.print("Ingresa un número: ");
        int n = 18;
        int suma = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                suma += i;
            }
        }
        System.out.println("Suma de pares hasta " + n + ": " + suma);
    }
}