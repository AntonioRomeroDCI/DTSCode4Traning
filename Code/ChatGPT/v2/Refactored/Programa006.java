package Code.ChatGPT.v2.Refactored;

public class Programa006 {
    public static void main(String[] args) {
        int a = 6;
        int b = 8;
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