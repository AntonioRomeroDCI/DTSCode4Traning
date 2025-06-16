import java.util.Scanner;

public class Tareas {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] tareas = new String[5]; // Permite hasta 5 tareas
        int contador = 0;

        System.out.println("Gestor de Tareas");
        while (contador < 5) {
            System.out.print("Ingrese una tarea (o 'salir' para terminar): ");
            String tarea = scanner.nextLine();

            if (tarea.equalsIgnoreCase("salir")) {
                break;
            }

            tareas[contador] = tarea;
            contador++;
        }

        System.out.println("\nTareas guardadas:");
        for (int i = 0; i < contador; i++) {
            System.out.println((i + 1) + ". " + tareas[i]);
        }

        scanner.close();
    }
}
