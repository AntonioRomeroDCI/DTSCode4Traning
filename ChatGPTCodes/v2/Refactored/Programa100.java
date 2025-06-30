public class Programa100 {
    public static void main(String[] args) {
        int a = 100;
        int b = 102;
        System.out.println("Resultado: " + multiplicar(a, b));
    }

    public static int multiplicar(int x, int y) {
        int resultado = 0;
        for (int i = 0; i < y; i++) {
            resultado += x;
        }
        return resultado;
    }
}