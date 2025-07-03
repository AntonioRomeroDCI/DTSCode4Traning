import pandas as pd

FOLDER="Refactored"

# Rutas de los archivos CSV
csv1_path = f'./Data/Metrics/ChatGPT/v2/{FOLDER}/halstead_mccabe_por_archivo.csv'
csv2_path = f'./Data/Times/ChatGPT/v2/{FOLDER}/promedios.csv'

# Leer los CSV
df1 = pd.read_csv(csv1_path)
df2 = pd.read_csv(csv2_path)

# Mostrar los primeros registros de cada uno
print("Primeros registros de halstead_mccabe_por_archivo.csv:")
print(df1.head())
print("\nPrimeros registros de promedios.csv:")
print(df2.head())

# Realizar el join (ajusta el tipo de join y la columna según sea necesario)
# Aquí asumimos que ambas tablas tienen una columna en común llamada 'id'
join_column = 'Clase'
merged_df = pd.merge(df1, df2, on=join_column, how='inner')  # Puedes cambiar 'inner' a 'left', 'right', 'outer'

#Se mueve la columna target al final
col = 'refactor'
merged_df = merged_df[[c for c in merged_df.columns if c != col] + [col]]

#Ordernamiento de info
merged_df = merged_df.sort_values(by='Clase')

# Mostrar resultado del join
print("\nResultado del join:")
print(merged_df.head())

# Guardar resultado en un nuevo CSV
merged_df.to_csv(f'resultado_join_{FOLDER}.csv', index=False)
print("\nJoin guardado en resultado_join.csv")
