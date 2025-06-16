import sys

def contar_loc_java(ruta_archivo):
    loc = 0
    en_comentario_multilinea = False

    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea_strip = linea.strip()

            # Ignorar líneas vacías
            if not linea_strip:
                continue

            # Comprobación de comentarios multilínea
            if en_comentario_multilinea:
                if '*/' in linea_strip:
                    en_comentario_multilinea = False
                continue

            if linea_strip.startswith("/*") or linea_strip.startswith("/**"):
                en_comentario_multilinea = True
                continue

            # Ignorar comentarios de una sola línea
            if linea_strip.startswith("//"):
                continue

            # Ignorar líneas que contienen solo cierre de comentario
            if linea_strip.endswith("*/"):
                continue

            # Si pasó todos los filtros, cuenta como LOC
            loc += 1

    return loc

# Ejemplo de uso
filename = sys.argv[1]
archivo_java = '../ChatGPTCodes/' + filename
print("LOC:", contar_loc_java(archivo_java))
