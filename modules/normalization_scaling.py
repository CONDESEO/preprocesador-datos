import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def normalizar_escalar_datos(dataset, features, columnas_a_ignorar=[]):
    """
    Aplica normalización o escalado a columnas numéricas, ignorando columnas categóricas y binarias.
    Si una columna tiene solo 2 valores únicos y no son 0 y 1, se convierte a 0/1 y se ignora.
    """
    columnas_numericas = []
    for col in features:
        if col in dataset.columns and pd.api.types.is_numeric_dtype(dataset[col]) and col not in columnas_a_ignorar:
            valores_unicos = sorted(dataset[col].dropna().unique())
            
            if len(valores_unicos) == 2:
                # Si ya son 0 y 1, ignorar
                if set(valores_unicos) == {0, 1}:
                    columnas_a_ignorar.append(col)
                    print(f"⚠ '{col}' ya está codificada como binaria (0/1), se ignora en normalización.")
                else:
                    # Convertir a 0/1 y luego ignorar
                    print(f"⚠ '{col}' tiene solo dos valores únicos: {valores_unicos}. Se convierten a 0 y 1.")
                    mapa = {valores_unicos[0]: 0, valores_unicos[1]: 1}
                    dataset[col] = dataset[col].map(mapa)
                    columnas_a_ignorar.append(col)
            else:
                columnas_numericas.append(col)

    if not columnas_numericas:
        print("\n=============================")
        print(" Normalización y Escalado ")
        print("=============================")
        print("No se han detectado columnas numéricas elegibles para normalización.")
        return dataset, True

    print("\n=============================")
    print(" Normalización y Escalado ")
    print("=============================")
    print("Se han detectado columnas numéricas a normalizar:")
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
            print("\nNormalización completada con Min-Max Scaling.")
        elif opcion == "2":
            scaler = StandardScaler()
            dataset[columnas_numericas] = scaler.fit_transform(dataset[columnas_numericas])
            print("\nNormalización completada con Z-score Normalization.")
        elif opcion == "3":
            return dataset, False
        else:
            print("Opción inválida. Intente de nuevo.")
            continue

        return dataset, True
