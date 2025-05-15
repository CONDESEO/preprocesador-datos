import os

def seleccionar_columnas(dataset):
    """
    Permite al usuario seleccionar las columnas de entrada (features) y la variable objetivo (target).
    """
    if dataset is None:
        print("⚠ Error: No hay datos cargados. Cargue un dataset antes de seleccionar las columnas.")
        return None, None
    
    columnas = list(dataset.columns)
    print("\n=============================")
    print(" Selección de Columnas ")
    print("=============================")
    print("Columnas disponibles en los datos:")
    
    for i, col in enumerate(columnas, 1):
        print(f"  [{i}] {col}")
    
    while True:
        try:
            features_idx = input("\nIngrese los números de las columnas de entrada (features), separados por comas: ")
            features_idx = [int(i.strip()) for i in features_idx.split(",")]
            
            if not features_idx:
                print("Error: Debe seleccionar al menos una columna como feature.")
                continue
            
            target_idx = int(input("Ingrese el número de la columna de salida (target): ").strip())
            
            if target_idx in features_idx:
                print("Error: La variable target no puede estar en las features.")
                continue
            
            features = [columnas[i - 1] for i in features_idx]
            target = columnas[target_idx - 1]
            
            print(f"\nSelección guardada: Features = {features}, Target = {target}")
            return features, target
            
        except ValueError:
            print("Error: Entrada inválida. Asegúrese de ingresar números separados por comas.")
        except IndexError:
            print("Error: Alguno de los números ingresados no corresponde a una columna válida.")
