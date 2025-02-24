import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def normalizar_escalar_datos(dataset, features):
    """
    Detecta y aplica normalización o escalado a las columnas numéricas dentro de las variables de entrada seleccionadas.
    """
    columnas_numericas = [col for col in features if col in dataset.columns and pd.api.types.is_numeric_dtype(dataset[col])]
    
    if not columnas_numericas:
        print("\n=============================")
        print(" Normalización y Escalado ")
        print("=============================")
        print("No se han detectado columnas numéricas en las variables de entrada seleccionadas.")
        print("No es necesario aplicar ninguna normalización.")
        return dataset, True  # Indica que este paso ya está completo
    
    print("\n=============================")
    print(" Normalización y Escalado ")
    print("=============================")
    print("Se han detectado columnas numéricas en las variables de entrada seleccionadas:")
    for col in columnas_numericas:
        print(f"  - {col}")
    
    while True:
        print("\nSeleccione una estrategia de normalización:")
        print("  [1] Min-Max Scaling (escala valores entre 0 y 1)")
        print("  [2] Z-score Normalization (media 0, desviación estándar 1)")
        print("  [3] Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            scaler = MinMaxScaler()
            dataset[columnas_numericas] = scaler.fit_transform(dataset[columnas_numericas])
            print("Normalización completada con Min-Max Scaling.")
        elif opcion == "2":
            scaler = StandardScaler()
            dataset[columnas_numericas] = scaler.fit_transform(dataset[columnas_numericas])
            print("Normalización completada con Z-score Normalization.")
        elif opcion == "3":
            return dataset, False  # No se aplicó ningún cambio, sigue pendiente
        else:
            print("⚠ Opción inválida. Intente de nuevo.")
            continue
        
        return dataset, True  # Indica que la normalización está completa
