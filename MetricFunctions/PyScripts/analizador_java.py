import re
import sys
from collections import Counter

# -------- Operadores comunes de Java --------
operadores_java = [
    '++', '--', '==', '!=', '>=', '<=', '&&', '||', '<<', '>>',
    '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '<<=', '>>=',
    '+', '-', '*', '/', '%', '=', '>', '<', '&', '|', '!', '^', '~', '?', ':', '.', '::'
]
operadores_java.sort(key=lambda x: -len(x))  # Priorizar operadores largos

# -------- Palabras clave de Java --------
palabras_clave_java = {
    'abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class',
    'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extends', 'final',
    'finally', 'float', 'for', 'goto', 'if', 'implements', 'import', 'instanceof', 'int',
    'interface', 'long', 'native', 'new', 'package', 'private', 'protected', 'public',
    'return', 'short', 'static', 'strictfp', 'super', 'switch', 'synchronized', 'this',
    'throw', 'throws', 'transient', 'try', 'void', 'volatile', 'while', 'var', 'true',
    'false', 'null'
}

# -------- Expresiones regulares --------
patron_identificadores = re.compile(r'\b[_a-zA-Z][_a-zA-Z0-9]*\b')
patron_literales_char = re.compile(r"'(\\.|[^\\'])'")
patron_literales_string = re.compile(r'"(\\.|[^"\\])*"')
patron_numeros = re.compile(r'\b\d+(\.\d+)?\b')

# -------- Funciones --------

def limpiar_codigo(codigo):
    codigo = re.sub(r'//.*?$', '', codigo, flags=re.MULTILINE)     # Comentarios de línea
    codigo = re.sub(r'/\*.*?\*/', '', codigo, flags=re.DOTALL)     # Comentarios multilínea
    return codigo

def obtener_operadores(codigo):
    encontrados = []
    i = 0
    while i < len(codigo):
        encontrado = False
        for op in operadores_java:
            if codigo[i:i+len(op)] == op:
                encontrados.append(op)
                i += len(op)
                encontrado = True
                break
        if not encontrado:
            i += 1
    return encontrados

def obtener_operandos(codigo):
    operandos = []

    # Literales
    operandos += patron_literales_char.findall(codigo)
    operandos += patron_literales_string.findall(codigo)

    # Números
    numeros = patron_numeros.findall(codigo)
    operandos += [n if isinstance(n, str) else n[0] for n in numeros]

    # Identificadores
    tokens = patron_identificadores.findall(codigo)
    for t in tokens:
        if t not in palabras_clave_java:
            operandos.append(t)

    return operandos

# -------- Programa principal --------

def main():
    if len(sys.argv) != 2:
        print("Uso: python analizador_java.py <archivo.java>")
        sys.exit(1)

    archivo = sys.argv[1]

    try:
        with open(archivo, 'r') as f:
            codigo = f.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'")
        sys.exit(1)

    codigo = limpiar_codigo(codigo)

    # Análisis de operadores
    lista_operadores = obtener_operadores(codigo)
    conteo_op = Counter(lista_operadores)

    # Análisis de operandos
    lista_operandos = obtener_operandos(codigo)
    conteo_od = Counter(lista_operandos)

    # Mostrar resultados
    print("===== Análisis de Operadores (Java) =====")
    print(f"Operadores distintos: {len(conteo_op)}")
    print(f"Total de operadores: {sum(conteo_op.values())}")
    for op, c in sorted(conteo_op.items()):
        print(f"  '{op}': {c}")

    print("\n===== Análisis de Operandos (Java) =====")
    print(f"Operandos distintos: {len(conteo_od)}")
    print(f"Total de operandos: {sum(conteo_od.values())}")
    for od, c in sorted(conteo_od.items()):
        print(f"  '{od}': {c}")

if __name__ == "__main__":
    main()
