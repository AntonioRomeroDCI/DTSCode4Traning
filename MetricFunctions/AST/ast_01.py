import javalang

java_code = """
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
"""

# Parsear el código
tree = javalang.parse.parse(java_code)

# Recorrer el árbol
for path, node in tree:
    print(f"Tipo de nodo: {type(node).__name__}")
    if isinstance(node, javalang.tree.MethodDeclaration):
        print(f"  Método: {node.name}")
    if isinstance(node, javalang.tree.ClassDeclaration):
        print(f"  Clase: {node.name}")
    if isinstance(node, javalang.tree.StatementExpression):
        print(f"  Expresión: {node.expression}")
