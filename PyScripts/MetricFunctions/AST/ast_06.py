import javalang
import os
import math
import csv
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

# DIR_CODE = "../../Code/Java/Rare"
# DIR_GRAPHS = "../../Graficas/Rare"
# DATA_CODE = "../../Data/Rare"

DIR_CODE = "../../Code/Java/Refactored"
DIR_GRAPHS = "../../Graficas/Refactored"
DATA_CODE = "../../Data/Refactored"


def analizar_metodo(metodo):
    operators, operands, mccabe = [], [], 1

    for path, node in metodo:
        if isinstance(node, javalang.tree.BinaryOperation):
            operators.append(node.operator)
            operands.append(str(node.operandl))
            operands.append(str(node.operandr))
        elif isinstance(node, javalang.tree.Assignment):
            operators.append(node.type)
            operands.append(str(node.expressionl))
            operands.append(str(node.value))
        elif isinstance(node, javalang.tree.MethodInvocation):
            operators.append(node.member)
            operands.extend(map(str, node.arguments))
        elif isinstance(node, javalang.tree.Literal):
            operands.append(node.value)
        elif isinstance(node, javalang.tree.MemberReference):
            operands.append(node.member)
        elif isinstance(node, javalang.tree.VariableDeclarator):
            operands.append(node.name)

        if isinstance(node, (javalang.tree.IfStatement, javalang.tree.ForStatement,
                             javalang.tree.WhileStatement, javalang.tree.DoStatement,
                             javalang.tree.SwitchStatement, javalang.tree.AssertStatement)):
            mccabe += 1

    n1, n2 = len(set(operators)), len(set(operands))
    N1, N2 = len(operators), len(operands)
    n, N = n1 + n2, N1 + N2
    V = N * math.log2(n) if n > 0 else 0
    D = (n1 / 2) * (N2 / n2) if n2 > 0 else 0
    E = D * V

    return {
        "n1": n1, "n2": n2, "N1": N1, "N2": N2,
        "n": n, "N": N,
        "V": round(V, 2), "D": round(D, 2), "E": round(E, 2),
        "McCabe": mccabe
    }

def analizar_archivo(path_archivo):
    with open(path_archivo, 'r', encoding='utf-8') as f:
        codigo = f.read()

    try:
        tree = javalang.parse.parse(codigo)
    except:
        return None

    archivo = os.path.basename(path_archivo)
    acumulado = Counter()

    for _, node in tree.filter(javalang.tree.MethodDeclaration):
        sub_tree = list(node)
        metrica = analizar_metodo(sub_tree)
        acumulado.update({k: metrica[k] for k in ['n1', 'n2', 'N1', 'N2', 'n', 'N', 'McCabe']})

    n, N = acumulado['n'], acumulado['N']
    V = N * math.log2(n) if n > 0 else 0
    D = (acumulado['n1'] / 2) * (acumulado['N2'] / acumulado['n2']) if acumulado['n2'] > 0 else 0
    E = D * V

    resumen = {
        "archivo": archivo,
        **acumulado,
        "V": round(V, 2),
        "D": round(D, 2),
        "E": round(E, 2)
    }

    return resumen

def analizar_directorio(carpeta):
    resumen_archivo = []

    for archivo in os.listdir(carpeta):
        if archivo.endswith(".java"):
            path = os.path.join(carpeta, archivo)
            resumen = analizar_archivo(path)
            if resumen:
                resumen_archivo.append(resumen)

    return resumen_archivo

def guardar_csv(nombre, datos, campos):
    with open(nombre, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for fila in datos:
            writer.writerow(fila)

def graficar_y_guardar(df, x, y, titulo, filename):
    plt.figure(figsize=(10, 6))
    df.plot(kind="bar", x=x, y=y, legend=False, color="skyblue", edgecolor="black")
    plt.title(titulo)
    plt.ylabel(y)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    os.makedirs(DIR_GRAPHS, exist_ok=True)
    ruta = os.path.join(DIR_GRAPHS, filename)
    plt.savefig(ruta)
    plt.close()
    print(f"📈 Gráfica guardada: {ruta}")

# === CONFIGURACIÓN ===
carpeta_java = DIR_CODE
salida_csv = f"{DATA_CODE}/halstead_mccabe_agregado_por_archivo.csv"

resumen_archivo = analizar_directorio(carpeta_java)

guardar_csv(salida_csv, resumen_archivo,
            ['archivo', 'n1', 'n2', 'N1', 'N2', 'n', 'N', 'V', 'D', 'E', 'McCabe'])

print(f"✅ CSV generado: {salida_csv}")

# === VISUALIZACIÓN + PNG ===
df = pd.DataFrame(resumen_archivo)

if not df.empty:
    graficar_y_guardar(df, x="archivo", y="V", titulo="Volumen Halstead por archivo", filename="volumen_halstead.png")
    graficar_y_guardar(df, x="archivo", y="E", titulo="Esfuerzo Halstead por archivo", filename="esfuerzo_halstead.png")
    graficar_y_guardar(df, x="archivo", y="McCabe", titulo="Complejidad McCabe por archivo", filename="mccabe.png")
