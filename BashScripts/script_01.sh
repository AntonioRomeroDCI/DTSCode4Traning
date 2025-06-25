#!/bin/bash

# Archivo de salida
output_file="Times/resultados_Adivina_RF.csv"
CLASE="Code.Java.Refactored.Adivina"

# Crear encabezado del CSV
echo "Iteración,Tiempo(s),Memoria(KB)" > "$output_file"
echo "Ejecutando clase Java: $CLASE (100 veces)..."
echo

for i in {1..100}
do
    # Ejecutar clase y capturar salida y métricas
    output_and_metrics=$( { /usr/bin/time -f "%e,%M" java "$CLASE"; } 2>&1 )

    # Separar salida del programa y métricas
    program_output=$(echo "$output_and_metrics" | head -n -1)   # Todas menos la última línea
    metrics_line=$(echo "$output_and_metrics" | tail -n 1)      # Última línea con %e,%M

    tiempo=$(echo "$metrics_line" | cut -d',' -f1)
    memoria=$(echo "$metrics_line" | cut -d',' -f2)

    # Mostrar en pantalla
    echo "Iteración $i:"
    echo "$program_output"
    echo "Tiempo = ${tiempo}s, Memoria = ${memoria}KB"
    echo "-----------------------------"

    # Guardar métricas en CSV
    echo "$i,$tiempo,$memoria" >> "$output_file"
done

echo
echo "✅ Ejecuciones completadas. Resultados guardados en: $output_file"
