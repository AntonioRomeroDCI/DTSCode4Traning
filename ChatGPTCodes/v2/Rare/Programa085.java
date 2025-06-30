public class Programa085 {
    public static void main(String[] args) {
        System.out.print("Ingresa el primer número: ");
        int a = 85;
        System.out.print("Ingresa el segundo número: ");
        int b = 87;
        int resultado = 0;
        for (int i = 0; i < b; i++) {
            resultado += a;
        }
        System.out.println("Resultado: " + resultado);
    }
}