import modules.data_loader as dl
import modules.column_selector as cs
import modules.missing_values_handler as mvh
import modules.categorical_transformer as ct

def main():
    dataset = None
    features, target = None, None
    seleccion_columnas_completada = False
    valores_faltantes_gestionados = False
    transformacion_categorica_completada = False
    preprocesado_iniciado = False
    
    while True:
        print("\n====================")
        print("Menú Principal")
        print("====================")
        print(f"[✓] 1. Cargar datos (archivo: datos.csv)" if dataset is not None else "[-] 1. Cargar datos (ningún archivo cargado)")

        # Preprocesado de datos con sus pasos
        if dataset is not None:
            print(f"[-] 2. Preprocesado de datos")
            print(f"  [✓] 2.1 Selección de columnas (completado)" if seleccion_columnas_completada else "  [✗] 2.1 Selección de columnas (pendiente)")
            print(f"  [✓] 2.2 Manejo de datos faltantes (completado)" if valores_faltantes_gestionados else "  [-] 2.2 Manejo de datos faltantes (pendiente)")
            print(f"  [✓] 2.3 Transformación de datos categóricos (completado)" if transformacion_categorica_completada else "  [-] 2.3 Transformación de datos categóricos (pendiente)")
            print(f"  [✗] 2.4 Normalización y escalado (requiere transformación categórica)" if not transformacion_categorica_completada else "  [-] 2.4 Normalización y escalado (pendiente)")
            print(f"  [✗] 2.5 Detección y manejo de valores atípicos (requiere normalización)")
        else:
            print("[✗] 2. Preprocesado de datos (requiere carga de datos)")

        print(f"[✗] 3. Visualización de datos (requiere preprocesado completo)" if not preprocesado_iniciado else "[✓] 3. Visualización de datos")
        print(f"[✗] 4. Exportar datos (requiere preprocesado completo)" if not preprocesado_iniciado else "[✓] 4. Exportar datos")
        print("[✓] 5. Salir")
        
        choice = input("Seleccione una opción: ").strip()
        
        if choice == "1":
            dataset = dl.cargar_datos()
            dl.mostrar_info(dataset)
        elif choice == "2" and dataset is not None:
            if not seleccion_columnas_completada:
                features, target = cs.seleccionar_columnas(dataset)
                if features and target:
                    seleccion_columnas_completada = True
            elif not valores_faltantes_gestionados:
                dataset, valores_faltantes_gestionados = mvh.manejar_valores_faltantes(dataset, features, target)
            elif not transformacion_categorica_completada:
                dataset, transformacion_categorica_completada = ct.transformar_datos_categoricos(dataset, features)
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
