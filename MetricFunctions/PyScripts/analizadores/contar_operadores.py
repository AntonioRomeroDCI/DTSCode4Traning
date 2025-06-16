import re
import sys
from collections import Counter

# Lista de operadores en C
operadores_c = [
    '++', '--', '==', '!=', '>=', '<=', '->', '&&', '||', '<<', '>>',
    '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '<<=', '>>=','*',
    '+', '-', '/', '%', '=', '>', '<', '&', '|', '!', '^', '~', '?', ':',';', '.','{','if','while','break','return'
]

# Ordenar por longitud descendente para evitar que operadores más cortos coincidan primero
operadores_c.sort(key=lambda x: -len(x))

def obtener_operadores(codigo):
    # Eliminar comentarios de línea y de bloque
    codigo = re.sub(r'//.*?$', '', codigo, flags=re.MULTILINE)
    codigo = re.sub(r'/\*.*?\*/', '', codigo, flags=re.DOTALL)

    # Crear una lista de todos los operadores encontrados
    encontrados = []

    i = 0
    while i < len(codigo):
        encontrado = False
        for op in operadores_c:
            if codigo[i:i+len(op)] == op:
                encontrados.append(op)
                i += len(op)
                encontrado = True
                break
        if not encontrado:
            i += 1

    return encontrados

def main():
    if len(sys.argv) != 2:
        print("Uso: python contar_operadores.py <archivo.c>")
        sys.exit(1)

    archivo = sys.argv[1]

    try:
        with open(archivo, 'r') as f:
            codigo = f.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'")
        sys.exit(1)

    lista_operadores = obtener_operadores(codigo)
    conteo = Counter(lista_operadores)

    print(f"Número de operadores distintos: {len(conteo)}")
    print(f"Número total de operadores: {sum(conteo.values())}")
    print("Detalle de operadores encontrados:")
    for op, cantidad in sorted(conteo.items()):
        print(f"  '{op}': {cantidad}")

if __name__ == "__main__":
    main()
