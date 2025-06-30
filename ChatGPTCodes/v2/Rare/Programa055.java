public class Programa055 {
    public static void main(String[] args) {
        System.out.print("Ingresa el primer número: ");
        int a = 55;
        System.out.print("Ingresa el segundo número: ");
        int b = 57;
        int resultado = 0;
        for (int i = 0; i < b; i++) {
            resultado += a;
        }
        System.out.println("Resultado: " + resultado);
    }
}