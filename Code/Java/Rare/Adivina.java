package Code.Java.Rare;

import java.util.Random;

public class Adivina {
    public static void main(String[] args) {
        Random random = new Random();
        int numeroSecreto = random.nextInt(10) + 1;
        //Scanner scanner = new Scanner(System.in);
        int intento=0;

        System.out.println("Adivina el número (entre 1 y 10): ");
        intento = 5; //scanner.nextInt();

        if (intento == numeroSecreto) {
            System.out.println("¡Correcto! Adivinaste el número.");
        } else {
            System.out.println("Incorrecto, el número era: " + numeroSecreto);
        }

        //scanner.close();
    }
}
