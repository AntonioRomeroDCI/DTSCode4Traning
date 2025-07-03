import javalang
import os
import math
import csv
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import pandas as pd

DIR_CODE = "../../Code/Java/Rare"
DATA_CODE = "../../Data/Rare"

# Refactored
# DIR_CODE = "../../Code/Java/Refactored"
# DATA_CODE = "../../Data/Refactored"

def analizar_metodo(metodo):
    operators, operands, mccabe = [], [], 1  # McCabe inicia en 1

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

        # McCabe: contar nodos de decisión
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
        return None, None

    archivo = os.path.basename(path_archivo)
    resultados_metodo = []
    acumulado = Counter()
    complejidad_total = 0

    for _, node in tree.filter(javalang.tree.MethodDeclaration):
        nombre = node.name
        metodo = node
        sub_tree = list(node)
        metrica = analizar_metodo(sub_tree)
        metrica['archivo'] = archivo
        metrica['metodo'] = nombre
        resultados_metodo.append(metrica)

        # Acumular por archivo
        acumulado.update({k: metrica[k] for k in ['n1', 'n2', 'N1', 'N2', 'n', 'N']})
        complejidad_total += metrica['McCabe']

    # Métricas Halstead globales
    V = acumulado['N'] * math.log2(acumulado['n']) if acumulado['n'] > 0 else 0
    D = (acumulado['n1'] / 2) * (acumulado['N2'] / acumulado['n2']) if acumulado['n2'] > 0 else 0
    E = D * V
    resumen = {
        "archivo": archivo,
        **acumulado,
        "V": round(V, 2),
        "D": round(D, 2),
        "E": round(E, 2),
        "McCabe": complejidad_total
    }

    return resumen, resultados_metodo

def analizar_directorio(carpeta):
    resumen_archivo = []
    detalle_metodos = []

    for archivo in os.listdir(carpeta):
        if archivo.endswith(".java"):
            path = os.path.join(carpeta, archivo)
            resumen, metodos = analizar_archivo(path)
            if resumen:
                resumen_archivo.append(resumen)
                detalle_metodos.extend(metodos)

    return resumen_archivo, detalle_metodos

def guardar_csv(nombre, datos, campos):
    with open(nombre, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for fila in datos:
            writer.writerow(fila)

def graficar_metricas(df, x, y, titulo):
    plt.figure(figsize=(10, 6))
    df.plot.bar(x=x, y=y, legend=False)
    plt.title(titulo)
    plt.ylabel(y)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# === CONFIGURACIÓN ===
carpeta_java = DIR_CODE

resumen_archivo, detalle_metodos = analizar_directorio(carpeta_java)

guardar_csv(f"{DATA_CODE}/halstead_mccabe_por_archivo.csv", resumen_archivo,
            ['archivo', 'n1', 'n2', 'N1', 'N2', 'n', 'N', 'V', 'D', 'E', 'McCabe'])

guardar_csv(f"{DATA_CODE}/halstead_mccabe_por_metodo.csv", detalle_metodos,
            ['archivo', 'metodo', 'n1', 'n2', 'N1', 'N2', 'n', 'N', 'V', 'D', 'E', 'McCabe'])

print("✅ Resultados exportados a CSV.")

# === VISUALIZACIÓN ===
df_arch = pd.DataFrame(resumen_archivo)
if not df_arch.empty:
    graficar_metricas(df_arch, x="archivo", y="V", titulo="Volumen Halstead por Archivo")
    graficar_metricas(df_arch, x="archivo", y="McCabe", titulo="Complejidad McCabe por Archivo")