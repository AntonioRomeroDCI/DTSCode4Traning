import java.util.Random;

public class Adivina {

    public static void main(String[] args) {
        int numeroSecreto = generarNumeroSecreto();
        int intento = obtenerIntento();

        mostrarResultado(intento, numeroSecreto);
    }

    private static int generarNumeroSecreto() {
        return new Random().nextInt(10) + 1;
    }

    private static int obtenerIntento() {
        // Valor fijo para pruebas; puede cambiarse por entrada de usuario
        int intento = 5;
        System.out.println("Adivina el número (entre 1 y 10): ");
        System.out.println("Intento seleccionado: " + intento);
        return intento;
    }

    private static void mostrarResultado(int intento, int numeroSecreto) {
        if (intento == numeroSecreto) {
            System.out.println("¡Correcto! Adivinaste el número.");
        } else {
            System.out.println("Incorrecto, el número era: " + numeroSecreto);
        }
    }
}
