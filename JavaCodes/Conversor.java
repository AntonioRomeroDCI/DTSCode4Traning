//import java.util.Scanner;

public class Conversor {
    public static void main(String[] args) {
        //Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese la temperatura en Celsius: " + args[0]);
        double celsius = Double.parseDouble(args[0]);//scanner.nextDouble();

        double fahrenheit = (celsius * 9/5) + 32;
        System.out.println("Equivalente en Fahrenheit: " + fahrenheit);

        //scanner.close();
    }
}