public class Programa033 {
    public static void main(String[] args) {
        System.out.print("Ingresa el primer número: ");
        int a = 33;
        System.out.print("Ingresa el segundo número: ");
        int b = 35;
        int resultado = 0;
        for (int i = 0; i < b; i++) {
            resultado += a;
        }
        System.out.println("Resultado: " + resultado);
    }
}