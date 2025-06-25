package Code.Java.Refactored;

public class Conversor {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Uso: java Conversor <temperatura_en_Celsius>");
            return;
        }

        try {
            double celsius = Double.parseDouble(args[0]);
            double fahrenheit = convertirAFahrenheit(celsius);
            mostrarResultado(celsius, fahrenheit);
        } catch (NumberFormatException e) {
            System.out.println("Error: debe ingresar un número válido como argumento.");
        }
    }

    private static double convertirAFahrenheit(double celsius) {
        return (celsius * 9 / 5) + 32;
    }

    private static void mostrarResultado(double celsius, double fahrenheit) {
        System.out.println("Temperatura en Celsius: " + celsius);
        System.out.println("Equivalente en Fahrenheit: " + fahrenheit);
    }
}