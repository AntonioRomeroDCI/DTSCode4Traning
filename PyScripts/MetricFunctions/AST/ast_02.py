import javalang
from collections import Counter


java_code = """
public class Demo {
    public static void main(String[] args) {
        int x = 0;
        for (int i = 0; i < 10; i++) {
            if (i % 2 == 0) {
                x += i;
            } else {
                x -= i;
            }
        }
        System.out.println(x);
    }

    public static int square(int n) {
        return n * n;
    }
}
"""

tree = javalang.parse.parse(java_code)

# Extraer métricas: número de clases, métodos y llamadas
num_classes = 0
num_methods = 0
num_calls = 0

for _, node in tree:
    if isinstance(node, javalang.tree.ClassDeclaration):
        num_classes += 1
    elif isinstance(node, javalang.tree.MethodDeclaration):
        num_methods += 1
    elif isinstance(node, javalang.tree.MethodInvocation):
        num_calls += 1

print(f"Clases: {num_classes}, Métodos: {num_methods}, Llamadas a métodos: {num_calls}")

# Aplicar transformaciones: renombrar métodos
for path, node in tree:
    if isinstance(node, javalang.tree.MethodDeclaration) and node.name == "main":
        print(f"Método encontrado: {node.name} → cambiar a 'start'")

java_code_mod = java_code.replace("main", "start", 1)
print(java_code_mod)

# Calcular complejidad ciclomática (McCabe)
mccabe = 1  # Complejidad mínima

for _, node in tree:
    if isinstance(node, (javalang.tree.IfStatement,
                         javalang.tree.ForStatement,
                         javalang.tree.WhileStatement,
                         javalang.tree.DoStatement,
                         javalang.tree.SwitchStatement,
                         javalang.tree.AssertStatement)):
                         #javalang.tree.CaseStatement)):
        mccabe += 1

print(f"Complejidad ciclomática: {mccabe}")

# Usar el AST como input para ML (vector simple)
counter = Counter()

for _, node in tree:
    counter[type(node).__name__] += 1

print(dict(counter))