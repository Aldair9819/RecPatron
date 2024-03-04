import pandas as pd

# Especifica la ruta del archivo .txt
ruta_archivo = 'Tarea 040224\\PARAMETROS_FINALES_CRUDOS.csv'
encoding = 'latin-1'

# Lee el archivo .txt en un DataFrame de Pandas
dataframe = pd.read_csv(ruta_archivo,encoding= encoding, sep=',' )


# Muestra las primeras filas del DataFrame para verificar la carga de datos
print(dataframe.head())
print("Nombres de los datos->")
print(dataframe.iloc[:0, ])

columnas_deseadas = ['OD_mg/L', 'CONDUC_CAMPO', 'TEMP_AGUA']
nuevo_dataframe = dataframe[columnas_deseadas]
print(nuevo_dataframe.head())

print(nuevo_dataframe.info())

dataframe_sin_nulos = nuevo_dataframe.dropna()
print(dataframe_sin_nulos.info())

