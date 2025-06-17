import math
import re
import sys
import os
from collections import Counter
import pandas as pd

DIRECTORIO_JAVA = "../../../Code/Java/Refactored"
DIRECTORIO_DATA = "../../../Data/"

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

def getVocabulary(n1,n2):
    """
    Vocabulary(n)
    n1 : Número de operadores distintos
    n2 : Número de operandos distintos
    returns n
    """
    return n1+n2

def getLength(N1,N2):
    """
    Length(N)
    N1 : Número total de operadores
    N2 : Número total de operandos
    returns N 
    """
    return N1+N2

def getVolume(N,n):
    return N*(math.log(n, 2))

def getLevel(n1,n2,N2):
    return (2/n1)*(n2/N2)

def getDifficulty(n1,n2,N2):
    return (n1/2)*(N2/n2)

def getEffort(V,L):
    """
    V : Volume
    L : Level
    returns E 
    """
    return V/L

def getFaults(V,S):
    """
    V : Volume
    S : Mean number of mental discriminations (decisions) 
    between errors (S* is 3000 according to Halstead)
    returns B
    """
    return V/S


def getHalsteadMetrics(directory_file, code_metrics):

    with open(directory_file, 'r') as file:
        #Lee el archivo 
        code = file.read()
        #Limpia el archivo eliminando los comentarios y elemementos especiales
        code = limpiar_codigo(code)

        #Analisis de operadores
        lista_operadores = obtener_operadores(code)
        conteo_op = Counter(lista_operadores)

        #Analisis de operandos
        lista_operandos = obtener_operandos(code)
        conteo_od = Counter(lista_operandos)

        #Asignacion de variables a usar en métricas
        n1 = len(conteo_op)     #Operadores distintos
        n2 = len(conteo_od)     #Operandos distintos

        N1 = sum(conteo_op.values())    #Numero total de ocurrencias de operadores
        N2 = sum(conteo_od.values())    #Numero total de ocurrencias de operandos

        n = getVocabulary(n1,n2)
        N = getLength(N1,N2)
        V = getVolume(N,n)
        L = getLevel(n1,n2,N2)
        D = getDifficulty(n1,n2,N2)
        E = getEffort(V,L)
        B = getFaults(V,3000)

        # print(f"n1 = {n1}")
        # print(f"n2 = {n2}")
        # print(f"N1 = {N1}")
        # print(f"N2 = {N2}")

        # print(f"Vocabulary (n) = {n}")
        # print(f"Length (N) = {N}")
        # print(f"Volume (V) = {V}")
        # print(f"Level (L) = {L}")
        # print(f"Difficulty (D) = {D}")
        # print(f"Effort (E) = {E}")
        # print(f"Faults (B) = {B}")

        code_metrics.append(n1)
        code_metrics.append(n2)
        code_metrics.append(N1)
        code_metrics.append(N2)
        code_metrics.append(n)
        code_metrics.append(N)
        code_metrics.append(V)
        code_metrics.append(L)
        code_metrics.append(D)
        code_metrics.append(E)
        code_metrics.append(B)

        return code_metrics

def getLOC(directory_file):
    loc = 0
    en_comentario_multilinea = False

    with open(directory_file, 'r') as file:
        for linea in file:
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

# -------- Programa principal --------
def main():

    # Crear un DataFrame vacío con columnas definidas
    df = pd.DataFrame(columns=["LOC","n1", "n2", "N1", "N2", "n", "N", "V", "L", "D", "E", "B"])

    try:
        for file in os.listdir(DIRECTORIO_JAVA):
            if file.endswith('.java'):
                directory_file = os.path.join(DIRECTORIO_JAVA, file)
                code_metrics = []
                
                #Adding LOC
                loc = getLOC(directory_file)
                code_metrics.append(loc)

                #Adding Halstead metrics
                code_metrics = getHalsteadMetrics(directory_file,code_metrics)

                #Agrega el contenido de las metricas en un Dataframe
                df.loc[len(df)] = code_metrics

                # Guardar en CSV
                df.to_csv(DIRECTORIO_DATA+'code_metrics_ref.csv', index=False, encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{directory_file}'")
        sys.exit(1)

if __name__ == "__main__":
    main()
