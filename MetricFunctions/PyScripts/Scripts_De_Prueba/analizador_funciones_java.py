import os
import re
import math
from collections import defaultdict, Counter
import sys

# Lista básica de operadores en Java (puedes expandirla)
JAVA_OPERATORS = [
    "+", "-", "*", "/", "=", "==", "!=", ">", "<", ">=", "<=", "&&", "||", "!", "%",
    "++", "--", "+=", "-=", "*=", "/=", "%=", "<<", ">>", "&", "|", "^", "~", ">>>",
    "instanceof", "new", "return", "throw", "try", "catch", "finally"
]

def extract_methods(code):
    """Extrae métodos de un archivo Java usando una expresión regular simplificada."""
    pattern = re.compile(r'(public|private|protected)?\s+\w+\s+\w+\s*\([^)]*\)\s*\{[^{}]*\}', re.DOTALL)
    return pattern.findall(code), pattern.finditer(code)

def analyze_halstead(code_block):
    # Eliminar comentarios y strings para reducir ruido
    code = re.sub(r'//.*|/\*[\s\S]*?\*/|"(.*?)"', '', code_block)

    # Contar operadores
    operators_found = [op for op in JAVA_OPERATORS if op in code]
    op_counts = Counter(re.findall(r'|'.join(re.escape(op) for op in JAVA_OPERATORS), code))

    # Quitar operadores para obtener operandos aproximados (simples palabras no reservadas)
    code_no_ops = re.sub(r'|'.join(re.escape(op) for op in JAVA_OPERATORS), ' ', code)
    tokens = re.findall(r'\b[A-Za-z_][A-Za-z_0-9]*\b', code_no_ops)
    reserved_words = set([
        "public", "private", "protected", "static", "void", "int", "float", "double",
        "boolean", "char", "if", "else", "for", "while", "do", "switch", "case", "break", "continue"
    ])
    operands = [t for t in tokens if t not in reserved_words]
    opnd_counts = Counter(operands)

    # Halstead metrics
    η1 = len(op_counts)
    η2 = len(opnd_counts)
    N1 = sum(op_counts.values())
    N2 = sum(opnd_counts.values())
    η = η1 + η2
    N = N1 + N2
    V = N * math.log2(η) if η > 0 else 0
    D = (η1 / 2) * (N2 / η2) if η2 > 0 else 0
    E = D * V
    T = E / 18
    B = (E ** (2/3)) / 3000 if E > 0 else 0

    return {
        'η1': η1, 'η2': η2, 'N1': N1, 'N2': N2,
        'η': η, 'N': N,
        'V': V, 'D': D, 'E': E, 'T': T, 'B': B
    }

def analyze_java_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()

    _, matches = extract_methods(code)
    for i, match in enumerate(matches, 1):
        method_code = match.group()
        print(f"\n🧪 Método #{i}")
        print(method_code.split('{')[0].strip())  # Firma del método
        metrics = analyze_halstead(method_code)
        for k, v in metrics.items():
            print(f"{k}: {v:.2f}")

# === Uso ===
# Guarda tu archivo Java como ejemplo, por ejemplo "MiPrograma.java"
# y luego llama esta función:
# analyze_java_file("MiPrograma.java")
# -------- Programa principal --------
def main():
    try:
        directory = "../../../Code/Java/Refactored"
        file = "Adivina.java"
        dirfile = f"{directory}/{file}"
        analyze_java_file(dirfile)
        # for file in os.listdir(DIRECTORIO_JAVA):
        #     if file.endswith('.java'):
        #         directory_file = os.path.join(DIRECTORIO_JAVA, file)
                # code_metrics = []
                
                # #Adding LOC
                # loc = getLOC(directory_file)
                # code_metrics.append(loc)

                # #Adding Halstead metrics
                # code_metrics = getHalsteadMetrics(directory_file,code_metrics)

                # #Agrega el contenido de las metricas en un Dataframe
                # df.loc[len(df)] = code_metrics

                # # Guardar en CSV
                # df.to_csv(DIRECTORIO_DATA+'code_metrics_ref.csv', index=False, encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{dirfile}'")
    sys.exit(1)

if __name__ == "__main__":
    main()
