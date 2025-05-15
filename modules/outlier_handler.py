import pandas as pd

def detectar_valores_atipicos(dataset, features):
    """
    Detecta valores atípicos en las columnas numéricas seleccionadas usando el método IQR.
    """
    columnas_numericas = [col for col in features if col in dataset.columns and pd.api.types.is_numeric_dtype(dataset[col])]
    valores_atipicos = {}
    
    for col in columnas_numericas:
        Q1 = dataset[col].quantile(0.25)
        Q3 = dataset[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = dataset[(dataset[col] < (Q1 - 1.5 * IQR)) | (dataset[col] > (Q3 + 1.5 * IQR))]
        valores_atipicos[col] = outliers.shape[0]
    
    return valores_atipicos

def manejar_valores_atipicos(dataset, features):
    """
    Permite al usuario seleccionar una estrategia para manejar los valores atípicos en columnas numéricas.
    """
    valores_atipicos = detectar_valores_atipicos(dataset, features)
    valores_atipicos = {col: count for col, count in valores_atipicos.items() if count > 0}
    
    if not valores_atipicos:
        print("\n=============================")
        print(" Detección y Manejo de Valores Atípicos ")
        print("=============================")
        print("No se han detectado valores atípicos en las columnas seleccionadas.")
        print("No es necesario aplicar ninguna estrategia.")
        return dataset, True  # Indica que este paso ya está completo
    
    print("\n=============================")
    print(" Detección y Manejo de Valores Atípicos ")
    print("=============================")
    print("Se han detectado valores atípicos en las siguientes columnas:")
    for col, count in valores_atipicos.items():
        print(f"  - {col}: {count} valores atípicos detectados")
    
    while True:
        print("\nSeleccione una estrategia para manejar los valores atípicos:")
        print("  [1] Eliminar filas con valores atípicos")
        print("  [2] Reemplazar valores atípicos con la mediana de la columna")
        print("  [3] Mantener valores atípicos sin cambios")
        print("  [4] Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        
        columnas_numericas = list(valores_atipicos.keys())
        
        if opcion == "1":
            for col in columnas_numericas:
                Q1 = dataset[col].quantile(0.25)
                Q3 = dataset[col].quantile(0.75)
                IQR = Q3 - Q1
                dataset = dataset[(dataset[col] >= (Q1 - 1.5 * IQR)) & (dataset[col] <= (Q3 + 1.5 * IQR))]
            print("Filas con valores atípicos eliminadas.")
        elif opcion == "2":
            for col in columnas_numericas:
                Q1 = dataset[col].quantile(0.25)
                Q3 = dataset[col].quantile(0.75)
                IQR = Q3 - Q1
                median_value = dataset[col].median()
                dataset.loc[(dataset[col] < (Q1 - 1.5 * IQR)) | (dataset[col] > (Q3 + 1.5 * IQR)), col] = median_value
            print("Valores atípicos reemplazados con la mediana de cada columna.")
        elif opcion == "3":
            print("Valores atípicos mantenidos sin cambios.")
        elif opcion == "4":
            return dataset, False  # No se aplicó ningún cambio, sigue pendiente
        else:
            print("Opción inválida. Intente de nuevo.")
            continue
        
        return dataset, True  # Indica que el manejo de valores atípicos está completo
