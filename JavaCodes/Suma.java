//import java.util.Scanner;

public class Suma {
    public static void main(String[] args) {
        //Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese el primer número: " + args[0]);
        int num1 = Integer.parseInt(args[0]);//scanner.nextInt();

        System.out.println("Ingrese el segundo número: "+ args[1]);
        int num2 = Integer.parseInt(args[1]);//scanner.nextInt();

        int suma = num1 + num2;
        System.out.println("La suma es: " + suma);

        //scanner.close();
    }
}
