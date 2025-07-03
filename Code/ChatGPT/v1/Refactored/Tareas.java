package Code.Java.Refactored;

//import java.util.Scanner;

public class Tareas {

    private static final int LIMITE_TAREAS = 5;

    public static void main(String[] args) {
        //Scanner scanner = new Scanner(System.in);
        String[] tareas = new String[LIMITE_TAREAS];

        mostrarMenu();
        int contador = leerTareas(tareas);
        mostrarTareas(tareas, contador);

        //scanner.close();
    }

    private static void mostrarMenu() {
        System.out.println("Gestor de Tareas");
    }

    private static int leerTareas(String[] tareas) {
        int contador = 0;
        while (contador < LIMITE_TAREAS) {
            System.out.print("Ingrese una tarea (o 'salir' para terminar): ");
            String tarea = "tarea" + contador;

            if (tarea.equalsIgnoreCase("salir")) {
                break;
            }

            tareas[contador++] = tarea;
        }
        return contador;
    }

    private static void mostrarTareas(String[] tareas, int cantidad) {
        System.out.println("\nTareas guardadas:");
        for (int i = 0; i < cantidad; i++) {
            System.out.println((i + 1) + ". " + tareas[i]);
        }
    }
}