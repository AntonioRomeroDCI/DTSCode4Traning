package ChatGPTCodes.v2.Refactored;

public class Programa070 {
    public static void main(String[] args) {
        int a = 70;
        int b = 72;
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