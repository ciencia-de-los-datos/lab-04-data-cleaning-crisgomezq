"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados. """

import pandas as pd

def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0) # Leer documento
    df = df.copy() # Copiar dataframe

    df.dropna(inplace=True) # Eliminar Datos faltantes
    
    df=df.apply(lambda x: x.astype(str)) # Convertir todas las columnas a tipo string

    df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x) # Convertir a minúsculas
    
    df = df.apply(lambda x: x.str.replace("$", "")) # Eliminar signo de pesos
    df = df.apply(lambda x: x.str.replace(",", "")) # Eliminar comas
    df = df.apply(lambda x: x.str.replace("-", " ") if x.dtype == "object" else x) # Reemplazar guiones por espacio
    df = df.apply(lambda x: x.str.replace("_", " ") if x.dtype == "object" else x) # Reemplazar guiones por espacio    
    df = df.apply(lambda x: x.str.replace("  ", " " ) if x.dtype == "object" else x) # Reemplazar dobles espacios por un solo espacio

    df['monto_del_credito'] = df['monto_del_credito'].astype(float) # Convertir la columna monto_del_credito a tipo flotante
    
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True, format='mixed')
      
    df.drop_duplicates(inplace=True) # Eliminar duplicados
     
    return df

# print(clean_data())