import modules.data_loader as dl
import modules.column_selector as cs

def main():
    dataset = None
    features, target = None, None
    seleccion_columnas_completada = False
    preprocesado_iniciado = False
    
    while True:
        print("\n====================")
        print("Menú Principal")
        print("====================")
        print(f"[✓] 1. Cargar datos (archivo: datos.csv)" if dataset is not None else "[✗] 1. Cargar datos")

        # Bloqueo de preprocesado hasta que se seleccionen columnas
        if dataset is not None:
            print(f"[-] 2. Preprocesado de datos {'(selección de columnas requerida)' if not seleccion_columnas_completada else ''}")
            if seleccion_columnas_completada:
                print(f"  [✓] 2.1 Selección de columnas (completado)")
                print(f"  [-] 2.2 Manejo de datos faltantes (pendiente)")
                print(f"  [✗] 2.3 Transformación de datos categóricos (pendiente)")
                print(f"  [✗] 2.4 Normalización y escalado (requiere transformación categórica)")
                print(f"  [✗] 2.5 Detección y manejo de valores atípicos (requiere normalización)")
        else:
            print("[✗] 2. Preprocesado de datos (selección de columnas requerida)")

        # Solo desbloqueamos visualización y exportación después del preprocesado
        print(f"[✗] 3. Visualización de datos (requiere preprocesado completo)" if not preprocesado_iniciado else "[✓] 3. Visualización de datos")
        print(f"[✗] 4. Exportar datos (requiere preprocesado completo)" if not preprocesado_iniciado else "[✓] 4. Exportar datos")
        print("[✓] 5. Salir")
        
        choice = input("Seleccione una opción: ").strip()
        
        if choice == "1":
            dataset = dl.cargar_datos()
        elif choice == "2" and dataset is not None:
            features, target = cs.seleccionar_columnas(dataset)
            if features and target:
                seleccion_columnas_completada = True  # Marca la selección como completada
        elif choice == "3" and preprocesado_iniciado:
            print("📊 Mostrando visualización de datos...")
        elif choice == "4" and preprocesado_iniciado:
            print("💾 Exportando datos...")
        elif choice == "5":
            print("👋 Saliendo del programa...")
            break
        else:
            print("⚠ Opción inválida o bloqueada.")

if __name__ == "__main__":
    main()
