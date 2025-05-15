import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def mostrar_resumen_estadistico(dataset):
    """Muestra estadísticas descriptivas de las variables numéricas y categóricas."""
    print("\n=============================")
    print(" Resumen Estadístico ")
    print("=============================")
    print("\nEstadísticas de Variables Numéricas:")
    print(dataset.describe())
    
    print("\nDistribución de Valores de Variables Categóricas:")
    for col in dataset.select_dtypes(include=['object']).columns:
        print(f"\n{col}:")
        print(dataset[col].value_counts())

def graficar_histogramas(dataset):
    """Genera histogramas para todas las variables numéricas."""
    dataset.hist(bins=30, figsize=(15, 10))
    plt.suptitle("Histogramas de Variables Numéricas")
    plt.show()

def graficar_dispersion(dataset, dataset_original, columnas):
    """
    Genera gráficos de dispersión antes y después del preprocesado
    solo para las columnas que fueron normalizadas (columnas numéricas válidas).
    """
    if not columnas:
        print("No hay columnas normalizadas para graficar.")
        return

    for col in columnas:
        if col in dataset.columns and col in dataset_original.columns:
            plt.figure(figsize=(14, 5))

            # Antes del preprocesado
            plt.subplot(1, 2, 1)
            plt.scatter(range(len(dataset_original[col])), dataset_original[col], alpha=0.5)
            plt.title(f'{col} - Antes del Preprocesado')
            plt.xlabel('Índice')
            plt.ylabel(col)

            # Después del preprocesado
            plt.subplot(1, 2, 2)
            plt.scatter(range(len(dataset[col])), dataset[col], alpha=0.5, color='green')
            plt.title(f'{col} - Después del Preprocesado')
            plt.xlabel('Índice')
            plt.ylabel(col)

            plt.tight_layout()
            plt.show()



def graficar_heatmap_correlacion(dataset):
    """Genera un heatmap de correlación entre variables numéricas."""
    dataset_numerico = dataset.select_dtypes(include=['number'])  # Solo columnas numéricas
    if dataset_numerico.shape[1] > 1:  # Asegurar que haya más de una columna numérica
        plt.figure(figsize=(10, 8))
        sns.heatmap(dataset_numerico.corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title("Heatmap de Correlación entre Variables Numéricas")
        plt.show()
    else:
        print("No hay suficientes columnas numéricas para generar un heatmap de correlación.")

def visualizar_datos(dataset, dataset_original, columnas_normalizadas):
    """Permite al usuario seleccionar diferentes opciones de visualización."""
    while True:
        print("\n=============================")
        print(" Visualización de Datos ")
        print("=============================")
        print("Seleccione qué tipo de visualización desea generar:")
        print("  [1] Resumen estadístico de las variables seleccionadas")
        print("  [2] Histogramas de variables numéricas")
        print("  [3] Gráficos de dispersión antes y después de la normalización")
        print("  [4] Heatmap de correlación de variables numéricas")
        print("  [5] Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            mostrar_resumen_estadistico(dataset)
        elif opcion == "2":
            graficar_histogramas(dataset)
        elif opcion == "3":
            graficar_dispersion(dataset, dataset_original, columnas_normalizadas)
        elif opcion == "4":
            graficar_heatmap_correlacion(dataset)
        elif opcion == "5":
            return True  # Indica que la visualización se ha completado
        else:
            print("Opción inválida. Intente de nuevo.")
