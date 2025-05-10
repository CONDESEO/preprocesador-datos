import pandas as pd
import os

def exportar_datos(dataset):
    print("\n=============================")
    print(" Exportación de Datos ")
    print("=============================")
    print("Seleccione el formato de exportación:")
    print("  [1] CSV (.csv)")
    print("  [2] Excel (.xlsx)")
    print("  [3] Volver al menú principal")
    
    opcion = input("Seleccione una opción: ").strip()

    if opcion not in ["1", "2"]:
        print("Cancelando exportación...")
        return False

    nombre_archivo = input("Ingrese el nombre del archivo de salida (sin extensión): ").strip()

    if not nombre_archivo:
        print(" Error: Nombre de archivo vacío.")
        return False

    try:
        if opcion == "1":
            nombre_completo = nombre_archivo + ".csv"
            dataset.to_csv(nombre_completo, index=False)
        elif opcion == "2":
            nombre_completo = nombre_archivo + ".xlsx"
            dataset.to_excel(nombre_completo, index=False)

        print(f'Datos exportados correctamente como "{nombre_completo}".')
        return True
    except Exception as e:
        print(f" Error al exportar datos: {e}")
        return False
