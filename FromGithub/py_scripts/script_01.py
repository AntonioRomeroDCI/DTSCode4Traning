from pydriller import Repository
import os

# Repositorio a analizar (puede ser local o remoto)
REPO_URL = 'https://github.com/spring-projects/spring-framework.git'

# Carpeta para guardar los resultados
OUTPUT_DIR_BEFORE = 'FromGithub/Before'
OUTPUT_DIR_AFTER = 'FromGithub/After'

#os.makedirs(OUTPUT_DIR, exist_ok=True)

# Recorre commits que contengan la palabra 'refactor'
for commit in Repository(REPO_URL).traverse_commits():
    if 'refactor' in commit.msg.lower():
        print(f'Procesando commit {commit.hash[:7]}: {commit.msg.strip()}')

        for file in commit.modified_files:
            if file.filename.endswith('.java'):
                if file.source_code and file.source_code_before:
                    # Nombre base del archivo
                    base_name = file.filename.replace('/', '_').replace('\\', '_')
                    hash_short = commit.hash[:7]

                    # Crear rutas de salida
                    # before_path = os.path.join(OUTPUT_DIR, f'{hash_short}_{base_name}_before.java')
                    # after_path = os.path.join(OUTPUT_DIR, f'{hash_short}_{base_name}_after.java')
                    before_path = os.path.join(OUTPUT_DIR_BEFORE, f'{base_name}')
                    after_path = os.path.join(OUTPUT_DIR_AFTER, f'{base_name}')

                    # Guardar código antes y después
                    with open(before_path, 'w', encoding='utf-8') as f:
                        f.write(file.source_code_before)
                    with open(after_path, 'w', encoding='utf-8') as f:
                        f.write(file.source_code)

                    print(f'  → Guardado: {before_path} y {after_path}')
