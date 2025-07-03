import lizard
import csv
import os

# DIR_CODE = "../../../Code/Java/Rare"
# DATA_CODE = "../../../Data/rare"

DIR_CODE = "../../../Code/Java/Refactored"
DATA_CODE = "../../../Data/refactored"

def analizar_carpeta_java(ruta_directorio, salida_csv):
    resultados_totales = []

    for root, _, files in os.walk(ruta_directorio):
        for archivo in files:
            if archivo.endswith(".java"):
                ruta_archivo = os.path.join(root, archivo)
                try:
                    resultados = lizard.analyze_file(ruta_archivo)
                    for funcion in resultados.function_list:
                        resultados_totales.append({
                            "archivo": resultados.filename,
                            "funcion": funcion.name,
                            "linea_inicio": funcion.start_line,
                            "complejidad_mccabe": funcion.cyclomatic_complexity,
                            "lineas_codigo": funcion.length
                        })
                except Exception as e:
                    print(f"Error analizando {ruta_archivo}: {e}")

    # Escribir CSV
    with open(salida_csv, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["archivo", "funcion", "linea_inicio", "complejidad_mccabe", "lineas_codigo"])
        writer.writeheader()
        writer.writerows(resultados_totales)

    print(f"\n✅ Análisis completado. Resultados guardados en: {salida_csv}")

if __name__ == "__main__":
    directorio_entrada = DIR_CODE       # Cambia esto a tu carpeta con archivos Java
    archivo_salida = f"{DATA_CODE}/complejidad_mccabe.csv"      # Archivo de salida CSV
    analizar_carpeta_java(directorio_entrada, archivo_salida)
