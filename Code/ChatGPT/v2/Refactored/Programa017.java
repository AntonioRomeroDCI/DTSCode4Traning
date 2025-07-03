package Code.ChatGPT.v2.Refactored;

public class Programa017 {
    public static void main(String[] args) {
        String palabra = "ejemplo17";
        System.out.println("Vocales: " + contarVocales(palabra));
    }

    public static int contarVocales(String texto) {
        int contador = 0;
        texto = texto.toLowerCase();
        for (int i = 0; i < texto.length(); i++) {
            char c = texto.charAt(i);
            if ("aeiou".indexOf(c) != -1) {
                contador++;
            }
        }
        return contador;
    }
}