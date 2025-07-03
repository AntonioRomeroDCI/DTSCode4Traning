import re
import math
import os
import csv
from collections import Counter, defaultdict

# DIR_CODE = "../../../Code/Java"
# DATA_CODE = "../../../Data/original"

DIR_CODE = "../../../Code/Java/Refactored"
DATA_CODE = "../../../Data/refactored"

JAVA_OPERATORS = [
    "+", "-", "*", "/", "=", "==", "!=", ">", "<", ">=", "<=", "&&", "||", "!", "%",
    "++", "--", "+=", "-=", "*=", "/=", "%=", "<<", ">>", "&", "|", "^", "~", ">>>",
    "instanceof", "new", "return", "throw", "try", "catch", "finally", ".", "?"
]

RESERVED_WORDS = {
    "public", "private", "protected", "static", "void", "int", "float", "double",
    "boolean", "char", "if", "else", "for", "while", "do", "switch", "case", "break", 
    "continue", "class", "new", "return", "System", "out", "println"
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
        'η': η, 'N': N,
        'V': V, 'D': D, 'E': E, 'T': T, 'B': B
    }

def extract_methods(code):
    pattern = re.compile(
        r'(public|private|protected)?\s+static\s+\w+\s+(\w+)\s*\([^)]*\)\s*\{(?:[^{}]*|\{[^{}]*\})*\}',
        re.DOTALL
    )
    return [(match.group(2), match.group()) for match in pattern.finditer(code)]

def analyze_folder(folder_path, output_detail_csv, output_summary_csv):
    results = []
    file_totals = defaultdict(lambda: Counter())

    for filename in os.listdir(folder_path):
        print(filename)
        if filename.endswith('.java'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            methods = extract_methods(code)
            print(methods)
            for name, body in methods:
                metrics = halstead_metrics(body)
                results.append({
                    'Archivo': filename,
                    'Método': name,
                    **metrics
                })
                for k, v in metrics.items():
                    if isinstance(v, (int, float)):
                        file_totals[filename][k] += v

    # Guardar métricas por método
    keys = ['Archivo', 'Método', 'η1', 'η2', 'N1', 'N2', 'η', 'N', 'V', 'D', 'E', 'T', 'B']
    with open(output_detail_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

    # Guardar métricas agregadas por archivo
    summary_rows = []
    for archivo, agg in file_totals.items():
        row = {'Archivo': archivo}
        row.update(agg)
        summary_rows.append(row)

    keys_summary = ['Archivo', 'η1', 'η2', 'N1', 'N2', 'η', 'N', 'V', 'D', 'E', 'T', 'B']
    with open(output_summary_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys_summary)
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f"✅ Métricas por método guardadas en: {output_detail_csv}")
    print(f"✅ Métricas agregadas por archivo guardadas en: {output_summary_csv}")

# === Ejecución ===
if __name__ == "__main__":
    analyze_folder(
        folder_path=DIR_CODE,
        output_detail_csv=f"{DATA_CODE}/halstead_por_metodo.csv",
        output_summary_csv=f"{DATA_CODE}/halstead_por_archivo.csv"
    )
