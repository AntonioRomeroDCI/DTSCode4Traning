package ChatGPTCodes.v2.Refactored;

public class Programa094 {
    public static void main(String[] args) {
        int a = 94;
        int b = 96;
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