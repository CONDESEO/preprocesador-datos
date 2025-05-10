import pandas as pd
from sklearn.preprocessing import LabelEncoder

def transformar_datos_categoricos(dataset, features):
    """
    Detecta y transforma columnas categóricas en las variables de entrada seleccionadas.
    """
    columnas_categoricas = [col for col in features if dataset[col].dtype == 'object']
    
    if not columnas_categoricas:
        print("\n=============================")
        print(" Transformación de Datos Categóricos ")
        print("=============================")
        print("No se han detectado columnas categóricas en las variables de entrada seleccionadas.")
        print("No es necesario aplicar ninguna transformación.")
        return dataset, True  # Indica que este paso ya está completo
    
    print("\n=============================")
    print(" Transformación de Datos Categóricos ")
    print("=============================")
    print("Se han detectado columnas categóricas en las variables de entrada seleccionadas:")
    for col in columnas_categoricas:
        print(f"  - {col}")
    
    while True:
        print("\nSeleccione una estrategia de transformación:")
        print("  [1] One-Hot Encoding (genera nuevas columnas binarias)")
        print("  [2] Label Encoding (convierte categorías a números enteros)")
        print("  [3] Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            dataset = pd.get_dummies(dataset, columns=columnas_categoricas, drop_first=True)
            print("\nTransformación completada con One-Hot Encoding.")
        elif opcion == "2":
            label_encoders = {}
            for col in columnas_categoricas:
                le = LabelEncoder()
                dataset[col] = le.fit_transform(dataset[col])
                label_encoders[col] = le
            print("\nTransformación completada con Label Encoding.")
        elif opcion == "3":
            return dataset, False  # No se aplicó ningún cambio, sigue pendiente
        else:
            print("⚠ Opción inválida. Intente de nuevo.")
            continue
        
        return dataset, True, columnas_categoricas  # Indica que la transformación está completa
