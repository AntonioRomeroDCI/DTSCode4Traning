public class Programa096 {
    public static void main(String[] args) {
        System.out.print("Ingresa una palabra: ");
        String palabra = "ejemplo96";
        palabra = palabra.toLowerCase();
        int contador = 0;
        for (int i = 0; i < palabra.length(); i++) {
            char c = palabra.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                contador++;
            }
        }
        System.out.println("Vocales: " + contador);
    }
}