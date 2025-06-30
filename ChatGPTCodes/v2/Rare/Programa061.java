public class Programa061 {
    public static void main(String[] args) {
        System.out.print("Ingresa el primer número: ");
        int a = 61;
        System.out.print("Ingresa el segundo número: ");
        int b = 63;
        int resultado = 0;
        for (int i = 0; i < b; i++) {
            resultado += a;
        }
        System.out.println("Resultado: " + resultado);
    }
}