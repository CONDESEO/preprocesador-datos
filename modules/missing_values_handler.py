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
        print("  [2] Rellenar con la media de la columna")
        print("  [3] Rellenar con la mediana de la columna")
        print("  [4] Rellenar con la moda de la columna")
        print("  [5] Rellenar con un valor constante")
        print("  [6] Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            dataset = dataset.dropna(subset=columnas_seleccionadas)
            print("✅ Filas con valores faltantes eliminadas.")
        elif opcion == "2":
            dataset[columnas_seleccionadas] = dataset[columnas_seleccionadas].fillna(dataset[columnas_seleccionadas].mean())
            print("✅ Valores faltantes rellenados con la media de cada columna.")
        elif opcion == "3":
            dataset[columnas_seleccionadas] = dataset[columnas_seleccionadas].fillna(dataset[columnas_seleccionadas].median())
            print("✅ Valores faltantes rellenados con la mediana de cada columna.")
        elif opcion == "4":
            dataset[columnas_seleccionadas] = dataset[columnas_seleccionadas].fillna(dataset[columnas_seleccionadas].mode().iloc[0])
            print("✅ Valores faltantes rellenados con la moda de cada columna.")
        elif opcion == "5":
            valor = input("Ingrese un valor numérico para reemplazar los valores faltantes: ")
            try:
                valor = float(valor)
                dataset[columnas_seleccionadas] = dataset[columnas_seleccionadas].fillna(valor)
                print(f"✅ Valores faltantes reemplazados con el valor {valor}.")
            except ValueError:
                print("⚠ Error: Debe ingresar un número válido.")
                continue
        elif opcion == "6":
            return dataset, False  # No se aplicó ningún cambio, sigue pendiente
        else:
            print("⚠ Opción inválida. Intente de nuevo.")
            continue
        
        return dataset, True  # Indica que el manejo de valores faltantes está completo
