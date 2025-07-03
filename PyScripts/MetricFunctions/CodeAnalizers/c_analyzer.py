import re
import sys
from collections import Counter

# -------- Configuración de operadores --------
operadores_c = [
    '++', '--', '==', '!=', '>=', '<=', '->', '&&', '||', '<<', '>>',
    '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '<<=', '>>=',
    '+', '-', '*', '/', '%', '=', '>', '<', '&', '|', '!', '^', '~', '?', ':', ',', '.'
]
operadores_c.sort(key=lambda x: -len(x))  # ordenar por longitud descendente

# -------- Palabras clave de C para excluir --------
palabras_clave_c = {
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double',
    'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'inline', 'int', 'long',
    'register', 'restrict', 'return', 'short', 'signed', 'sizeof', 'static', 'struct',
    'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while', '_Alignas',
    '_Alignof', '_Atomic', '_Bool', '_Complex', '_Generic', '_Imaginary', '_Noreturn',
    '_Static_assert', '_Thread_local'
}

# -------- Expresiones regulares --------
patron_identificadores = re.compile(r'\b[_a-zA-Z][_a-zA-Z0-9]*\b')
patron_constantes_char = re.compile(r"'(\\.|[^\\'])'")
patron_numeros = re.compile(r'\b\d+(\.\d+)?\b')

# -------- Funciones --------

def limpiar_codigo(codigo):
    # Elimina comentarios línea y bloque
    codigo = re.sub(r'//.*?$', '', codigo, flags=re.MULTILINE)
    codigo = re.sub(r'/\*.*?\*/', '', codigo, flags=re.DOTALL)
    return codigo

def obtener_operadores(codigo):
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

def obtener_operandos(codigo):
    operandos = []

    # Literales de tipo char
    operandos += patron_constantes_char.findall(codigo)

    # Números
    numeros = patron_numeros.findall(codigo)
    operandos += [n if isinstance(n, str) else n[0] for n in numeros]

    # Identificadores
    tokens = patron_identificadores.findall(codigo)
    for t in tokens:
        if t not in palabras_clave_c:
            operandos.append(t)

    return operandos

# -------- Programa principal --------

def main():
    if len(sys.argv) != 2:
        print("Uso: python analizador_c.py <archivo.c>")
        sys.exit(1)

    archivo = sys.argv[1]

    try:
        with open(archivo, 'r') as f:
            codigo = f.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'")
        sys.exit(1)

    codigo = limpiar_codigo(codigo)

    # Operadores
    lista_operadores = obtener_operadores(codigo)
    conteo_op = Counter(lista_operadores)

    # Operandos
    lista_operandos = obtener_operandos(codigo)
    conteo_od = Counter(lista_operandos)

    # Resultados
    print("===== Análisis de Operadores =====")
    print(f"Operadores distintos: {len(conteo_op)}")
    print(f"Total de operadores: {sum(conteo_op.values())}")
    for op, c in sorted(conteo_op.items()):
        print(f"  '{op}': {c}")

    print("\n===== Análisis de Operandos =====")
    print(f"Operandos distintos: {len(conteo_od)}")
    print(f"Total de operandos: {sum(conteo_od.values())}")
    for od, c in sorted(conteo_od.items()):
        print(f"  '{od}': {c}")

if __name__ == "__main__":
    main()
