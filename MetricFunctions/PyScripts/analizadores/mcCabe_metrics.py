import lizard



def analizar_mccabe_java(ruta_archivo):
    resultados = lizard.analyze_file(ruta_archivo)

    print(f"Archivo analizado: {resultados.filename}")
    for funcion in resultados.function_list:
        print("--------")
        print(f"Nombre función/método: {funcion.name}")
        print(f"Línea inicio: {funcion.start_line}")
        print(f"Complejidad ciclomática (McCabe): {funcion.cyclomatic_complexity}")
        print(f"Líneas de código: {funcion.length}")

if __name__ == "__main__":
    archivo_java = "../../../Code/Java/Adivina.java"  # Cambia esto por la ruta real
    analizar_mccabe_java(archivo_java)
