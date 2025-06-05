public class Factorial {

    public static void main(String[] args) {
        int numero = obtenerNumero();
        mostrarNumero(numero);

        int resultado = calcularFactorial(numero);
        mostrarResultado(numero, resultado);
    }

    private static int obtenerNumero() {
        // Valor fijo para pruebas; se puede modificar para entrada desde consola
        System.out.print("Ingrese un número: ");
        int numero = 5;
        return numero;
    }

    private static void mostrarNumero(int numero) {
        System.out.println(numero);
    }

    private static int calcularFactorial(int numero) {
        int factorial = 1;
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }
        return factorial;
    }

    private static void mostrarResultado(int numero, int factorial) {
        System.out.println("El factorial de " + numero + " es: " + factorial);
    }
}