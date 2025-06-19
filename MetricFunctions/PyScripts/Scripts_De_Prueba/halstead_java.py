import re
import math
from collections import Counter

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

def analyze_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()

    methods = extract_methods(code)
    print(f"{'Método':<25} {'η1':<3} {'η2':<3} {'N1':<3} {'N2':<3} {'V':<10} {'D':<10} {'E':<10} {'T':<8} {'B':<8}")
    print('-' * 90)

    for name, body in methods:
        m = halstead_metrics(body)
        print(f"{name:<25} {m['η1']:<3} {m['η2']:<3} {m['N1']:<3} {m['N2']:<3} "
              f"{m['V']:<10.2f} {m['D']:<10.2f} {m['E']:<10.2f} {m['T']:<8.2f} {m['B']:<8.6f}")

# === Ejecución principal ===
if __name__ == "__main__":
    analyze_file("../../../Code/Java/Refactored/Adivina.java")
