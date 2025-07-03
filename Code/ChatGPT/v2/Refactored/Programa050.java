package ChatGPTCodes.v2.Refactored;

public class Programa050 {
    public static void main(String[] args) {
        int a = 50;
        int b = 52;
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