public class Suma {

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Uso: java Suma <numero1> <numero2>");
            return;
        }

        try {
            int num1 = Integer.parseInt(args[0]);
            int num2 = Integer.parseInt(args[1]);

            mostrarNumeros(num1, num2);
            int resultado = sumar(num1, num2);
            mostrarResultado(resultado);

        } catch (NumberFormatException e) {
            System.out.println("Error: Ambos argumentos deben ser números enteros.");
        }
    }

    private static void mostrarNumeros(int num1, int num2) {
        System.out.println("Primer número: " + num1);
        System.out.println("Segundo número: " + num2);
    }

    private static int sumar(int a, int b) {
        return a + b;
    }

    private static void mostrarResultado(int suma) {
        System.out.println("La suma es: " + suma);
    }
}