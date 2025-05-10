import os

def run_test(nombre_archivo):
    print(f"\n▶ Ejecutando {nombre_archivo}...\n")
    os.system(f"python -m unittest tests.{nombre_archivo}")

def main():
    while True:
        print("\n======================")
        print(" Menú de Pruebas")
        print("======================")
        print(" 1. Probar manejo de valores faltantes")
        print(" 2. Probar codificación de datos categóricos")
        print(" 3. Probar normalización de datos")
        print(" 4. Probar manejo de valores atípicos")
        print(" 5. Ejecutar todas las pruebas")
        print(" 6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            run_test("test_missing_values_handler")
        elif opcion == "2":
            run_test("test_categorical_transformer")
        elif opcion == "3":
            run_test("test_normalization_scaling")
        elif opcion == "4":
            run_test("test_outlier_handler")
        elif opcion == "5":
            os.system("python -m unittest discover tests")
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
