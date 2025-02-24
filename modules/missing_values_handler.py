import pandas as pd

def manejar_valores_faltantes(dataset, features, target):
    """
    Analiza y maneja los valores faltantes en las columnas seleccionadas.
    """
    columnas_seleccionadas = features + [target]
    valores_nulos = dataset[columnas_seleccionadas].isnull().sum()
    valores_faltantes = valores_nulos[valores_nulos > 0]
    
    if valores_faltantes.empty:
        print("\n=============================")
        print(" Manejo de Valores Faltantes ")
        print("=============================")
        print("No se han detectado valores faltantes en las columnas seleccionadas.")
        print("No es necesario aplicar ninguna estrategia.")
        return dataset, True  # Indica que este paso ya está completo
    
    print("\n=============================")
    print(" Manejo de Valores Faltantes ")
    print("=============================")
    print("Se han detectado valores faltantes en las siguientes columnas:")
    for col, count in valores_faltantes.items():
        print(f"  - {col}: {count} valores faltantes")
    
    while True:
        print("\nSeleccione una estrategia para manejar los valores faltantes:")
        print("  [1] Eliminar filas con valores faltantes")
        print("  [2] Rellenar con la media de la columna (numéricas) y la moda (categóricas)")
        print("  [3] Rellenar con la mediana de la columna (numéricas) y la moda (categóricas)")
        print("  [4] Rellenar con la moda de la columna")
        print("  [5] Rellenar con un valor constante")
        print("  [6] Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        
        columnas_numericas = [col for col in columnas_seleccionadas if pd.api.types.is_numeric_dtype(dataset[col])]
        columnas_categoricas = [col for col in columnas_seleccionadas if col not in columnas_numericas]
        
        if opcion == "1":
            dataset = dataset.dropna(subset=columnas_seleccionadas)
            print("Filas con valores faltantes eliminadas.")
        elif opcion == "2":
            dataset[columnas_numericas] = dataset[columnas_numericas].fillna(dataset[columnas_numericas].mean())
            dataset[columnas_categoricas] = dataset[columnas_categoricas].fillna(dataset[columnas_categoricas].mode().iloc[0])
            print("Valores faltantes rellenados con la media (numéricas) y la moda (categóricas).")
        elif opcion == "3":
            dataset[columnas_numericas] = dataset[columnas_numericas].fillna(dataset[columnas_numericas].median())
            dataset[columnas_categoricas] = dataset[columnas_categoricas].fillna(dataset[columnas_categoricas].mode().iloc[0])
            print("Valores faltantes rellenados con la mediana (numéricas) y la moda (categóricas).")
        elif opcion == "4":
            dataset[columnas_seleccionadas] = dataset[columnas_seleccionadas].fillna(dataset[columnas_seleccionadas].mode().iloc[0])
            print("Valores faltantes rellenados con la moda de cada columna.")
        elif opcion == "5":
            if columnas_numericas:
                valor_numerico = input("Ingrese un valor numérico para reemplazar los valores faltantes en columnas numéricas: ").strip()
                try:
                    valor_numerico = float(valor_numerico)
                    dataset[columnas_numericas] = dataset[columnas_numericas].fillna(valor_numerico)
                except ValueError:
                    print("⚠ Error: Debe ingresar un número válido para las columnas numéricas.")
                    continue
            if columnas_categoricas:
                dataset[columnas_categoricas] = dataset[columnas_categoricas].fillna(dataset[columnas_categoricas].mode().iloc[0])
            print("Valores faltantes reemplazados con el valor numérico ingresado (numéricas) y la moda (categóricas).")
        elif opcion == "6":
            return dataset, False  # No se aplicó ningún cambio, sigue pendiente
        else:
            print("⚠ Opción inválida. Intente de nuevo.")
            continue
        
        return dataset, True  # Indica que el manejo de valores faltantes está completo