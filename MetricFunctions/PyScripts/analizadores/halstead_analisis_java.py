import os
import re
import csv
import math
from collections import Counter, defaultdict

DIR_CODE = "../../../Code/Java"
DATA_CODE = "../../../Data/original"

# DIR_CODE = "../../../Code/Java/Refactored"
# DATA_CODE = "../../../Data/refactored"

# Operadores básicos en Java
JAVA_OPERATORS = [
    "+", "-", "*", "/", "=", "==", "!=", ">", "<", ">=", "<=", "&&", "||", "!", "%",
    "++", "--", "+=", "-=", "*=", "/=", "%=", "<<", ">>", "&", "|", "^", "~", ">>>",
    "instanceof", "new", "return", "throw", "try", "catch", "finally", ".", "?"
]

RESERVED_WORDS = {
    "public", "private", "protected", "static", "void", "int", "float", "double",
    "boolean", "char", "if", "else", "for", "while", "do", "switch", "case", "break",
    "continue", "class", "new", "return", "System", "out", "println", "final"
}

def halstead_metrics(code_block):
    code = re.sub(r'//.*|/\*[\s\S]*?\*/|"(.*?)"', '', code_block)
    op_pattern = '|'.join(re.escape(op) for op in JAVA_OPERATORS)
    op_counts = Counter(re.findall(op_pattern, code))
    code_no_ops = re.sub(op_pattern, ' ', code)
    tokens = re.findall(r'\b[A-Za-z_][A-Za-z_0-9]*\b', code_no_ops)
    operands = [t for t in tokens if t not in RESERVED_WORDS]
    opnd_counts = Counter(operands)

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
        'η': η, 'N': N, 'V': V, 'D': D, 'E': E, 'T': T, 'B': B
    }

def extract_methods(code):
    pattern = re.compile(
        r'(public|private|protected)?\s+static\s+\w+\s+(\w+)\s*\([^)]*\)\s*\{',
        re.MULTILINE
    )
    starts = [m.start() for m in pattern.finditer(code)]
    method_names = [m.group(2) for m in pattern.finditer(code)]

    methods = []
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(code)
        body = code[start:end]
        methods.append((method_names[i], body))
    return methods

def analyze_folder(folder_path, csv_metodo, csv_archivo):
    metodo_results = []
    archivo_totales = defaultdict(lambda: Counter())

    for filename in os.listdir(folder_path):
        if filename.endswith(".java"):
            full_path = os.path.join(folder_path, filename)
            with open(full_path, 'r', encoding='utf-8') as f:
                code = f.read()

            methods = extract_methods(code)
            for name, body in methods:
                metrics = halstead_metrics(body)
                row = {'Archivo': filename, 'Método': name}
                row.update(metrics)
                metodo_results.append(row)

                for k, v in metrics.items():
                    if isinstance(v, (int, float)):
                        archivo_totales[filename][k] += v

    # Guardar CSV por método
    method_keys = ['Archivo', 'Método', 'η1', 'η2', 'N1', 'N2', 'η', 'N', 'V', 'D', 'E', 'T', 'B']
    with open(csv_metodo, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=method_keys)
        writer.writeheader()
        writer.writerows(metodo_results)

    # Guardar CSV por archivo (suma agregada)
    summary = []
    for archivo, metricas in archivo_totales.items():
        row = {'Archivo': archivo}
        row.update(metricas)
        summary.append(row)

    archivo_keys = ['Archivo', 'η1', 'η2', 'N1', 'N2', 'η', 'N', 'V', 'D', 'E', 'T', 'B']
    with open(csv_archivo, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=archivo_keys)
        writer.writeheader()
        writer.writerows(summary)

    print(f"✅ Métricas por método exportadas a: {csv_metodo}")
    print(f"✅ Métricas agregadas por archivo exportadas a: {csv_archivo}")

# === Ejecución principal ===
if __name__ == "__main__":
    analyze_folder(
        folder_path=DIR_CODE,
        csv_metodo=f"{DATA_CODE}/halstead_por_metodo_02.csv",
        csv_archivo=f"{DATA_CODE}/halstead_por_archivo_02.csv"
    )
