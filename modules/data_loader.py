import pandas as pd
import sqlite3
import os

def cargar_datos():
    """
    Permite al usuario seleccionar y cargar un archivo de datos en formato CSV, Excel o SQLite.
    Verifica que la ruta ingresada sea válida antes de abrir el archivo.
    """
    while True:
        print("\n=============================")
        print(" Carga de Datos ")
        print("=============================")
        print("Seleccione el tipo de archivo a cargar:")
        print("[1] CSV")
        print("[2] Excel")
        print("[3] SQLite")
        print("[4] Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ruta = input("Ingrese la ruta del archivo CSV: ").strip()
            if not os.path.isabs(ruta):
                ruta = os.path.abspath(ruta)
            if os.path.exists(ruta) and ruta.lower().endswith(('.csv', '.txt')):
                print(f"✅ Archivo encontrado: {ruta}")
                df = pd.read_csv(ruta, sep=None, engine='python')
                return df
            else:
                print(f"❌ Error: Archivo no encontrado o formato no válido. Ruta ingresada: {ruta}")

        elif opcion == "2":
            ruta = input("Ingrese la ruta del archivo Excel: ").strip()
            if not os.path.isabs(ruta):
                ruta = os.path.abspath(ruta)
            if os.path.exists(ruta) and ruta.lower().endswith('.xlsx'):
                print(f"✅ Archivo encontrado: {ruta}")
                try:
                    excel_file = pd.ExcelFile(ruta, engine='openpyxl')
                    hojas = excel_file.sheet_names
                    print(f"Hojas disponibles: {hojas}")
                    hoja = input("Ingrese el nombre de la hoja a cargar: ").strip()
                    if hoja in hojas:
                        df = pd.read_excel(ruta, sheet_name=hoja, engine='openpyxl')
                        return df
                    else:
                        print("❌ Error: Nombre de hoja no válido.")
                except Exception as e:
                    print(f"❌ Error al abrir el archivo Excel: {e}")
            else:
                print(f"❌ Error: Archivo no encontrado o formato incorrecto. Ruta ingresada: {ruta}")

        elif opcion == "3":
            ruta = input("Ingrese la ruta de la base de datos SQLite: ").strip()
            if not os.path.isabs(ruta):
                ruta = os.path.abspath(ruta)
            if os.path.exists(ruta) and ruta.lower().endswith(('.sqlite', '.db')):
                print(f"✅ Base de datos encontrada: {ruta}")
                try:
                    conn = sqlite3.connect(ruta)
                    cursor = conn.cursor()
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                    tablas = [tabla[0] for tabla in cursor.fetchall()]
                    if not tablas:
                        print("❌ Error: No hay tablas en la base de datos.")
                        conn.close()
                        continue
                    print("Tablas disponibles:")
                    for i, tabla in enumerate(tablas, 1):
                        print(f"[{i}] {tabla}")
                    try:
                        opcion_tabla = int(input("Seleccione una tabla: "))
                        if 1 <= opcion_tabla <= len(tablas):
                            df = pd.read_sql(f"SELECT * FROM {tablas[opcion_tabla - 1]}", conn)
                            conn.close()
                            return df
                        else:
                            print("❌ Error: Opción inválida.")
                    except ValueError:
                        print("❌ Error: Ingrese un número válido.")
                except Exception as e:
                    print(f"❌ Error al abrir la base de datos: {e}")
            else:
                print(f"❌ Error: Archivo no encontrado o formato incorrecto. Ruta ingresada: {ruta}")

        elif opcion == "4":
            return None  # Volver al menú principal
        else:
            print("❌ Error: Opción no válida.")

def mostrar_info(df, ruta):
    """
    Muestra información básica del dataset cargado.
    """
    print("\n✅ Datos cargados correctamente desde:", ruta)
    print(f"Número de filas: {df.shape[0]}")
    print(f"Número de columnas: {df.shape[1]}")
    #print("\nTipos de datos:")
    #print(df.dtypes)
    print("\nPrimeras 5 filas:")
    print(df.head())

    return df  # Retorna el DataFrame cargado para su uso en el pipeline
