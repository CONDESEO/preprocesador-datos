import modules.data_loader as dl
import modules.column_selector as cs
import modules.missing_values_handler as mvh
import modules.categorical_transformer as ct
import modules.normalization_scaling as ns
import modules.outlier_handler as oh
import modules.data_visualizer as dv
import modules.data_exporter as de


def main():
    dataset = None
    dataset_original = None
    features, target = None, None
    seleccion_columnas_completada = False
    valores_faltantes_gestionados = False
    transformacion_categorica_completada = False
    normalizacion_completada = False
    valores_atipicos_gestionados = False
    visualizacion_completada = False
    exportacion_completada = False
    
    while True:
        print("\n====================")
        print("Menú Principal")
        print("====================")
        print(f"[✓] 1. Cargar datos (archivo: datos.csv)" if dataset is not None else "[-] 1. Cargar datos (ningún archivo cargado)")

        # Preprocesado de datos con sus pasos
        if dataset is not None:
            print(f"[-] 2. Preprocesado de datos. Para ejecutar siguiente subapartado introducir: 2")
            print(f"  [✓] 2.1 Selección de columnas (completado)" if seleccion_columnas_completada else "  [✗] 2.1 Selección de columnas (pendiente)")
            print(f"  [✓] 2.2 Manejo de valores faltantes (completado)" if valores_faltantes_gestionados else "  [-] 2.2 Manejo de valores faltantes (pendiente)")
            print(f"  [✓] 2.3 Transformación de datos categóricos (completado)" if transformacion_categorica_completada else "  [-] 2.3 Transformación de datos categóricos (pendiente)")
            print(f"  [✓] 2.4 Normalización y escalado (completado)" if normalizacion_completada else "  [-] 2.4 Normalización y escalado (pendiente)")
            print(f"  [✓] 2.5 Detección y manejo de valores atípicos (completado)" if valores_atipicos_gestionados else "  [-] 2.5 Detección y manejo de valores atípicos (pendiente)")
        else:
            print("[✗] 2. Preprocesado de datos (requiere carga de datos)")

        print(f"[✓] 3. Visualización de datos" if visualizacion_completada else "[✗] 3. Visualización de datos (requiere preprocesado completo)")
        if exportacion_completada:
            print(f"[✓] 4. Exportar datos")
        elif visualizacion_completada and not exportacion_completada:
            print("[ ] 4. Exportar datos (disponible)")
        else:
            print("[✗] 4. Exportar datos(requiere visualización de datos)")
        print("[✓] 5. Salir")
        
        choice = input("Seleccione una opción: ").strip()
        
        if choice == "1":
            dataset = dl.cargar_datos()
            dataset_original = dataset.copy() if dataset is not None else None
            if dataset is not None:
                dl.mostrar_info(dataset)
        elif choice == "2" and dataset is not None:
            if not seleccion_columnas_completada:
                features, target = cs.seleccionar_columnas(dataset)
                if features and target:
                    seleccion_columnas_completada = True
            elif not valores_faltantes_gestionados:
                dataset, valores_faltantes_gestionados = mvh.manejar_valores_faltantes(dataset, features, target)
            elif not transformacion_categorica_completada:
                dataset, transformacion_categorica_completada, columnas_categoricas = ct.transformar_datos_categoricos(dataset, features)
            elif not normalizacion_completada:
                dataset, normalizacion_completada, columnas_normalizadas = ns.normalizar_escalar_datos(dataset, features, columnas_categoricas)
            elif not valores_atipicos_gestionados:
                dataset, valores_atipicos_gestionados = oh.manejar_valores_atipicos(dataset, features)
        elif choice == "3" and valores_atipicos_gestionados:
            visualizacion_completada = dv.visualizar_datos(dataset, dataset_original, columnas_normalizadas)
        elif choice == "4":
            if visualizacion_completada:
                exportacion_completada = de.exportar_datos(dataset)
            else:
                print("\n=============================")
                print(" Exportación de Datos ")
                print("=============================")
                print("No es posible exportar los datos hasta que se complete el preprocesado y la visualización.")
                print("Por favor, finalice todas las etapas antes de continuar.")

        elif choice == "5":
            salir_aplicacion()

def salir_aplicacion():
    print("\n=============================")
    print(" Salir de la Aplicación ")
    print("=============================")
    print("¿Está seguro de que desea salir?")
    print("  [1] Sí")
    print("  [2] No")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        print("\nCerrando la aplicación...")
        exit(0)
    elif opcion == "2":
        print("\nRegresando al menú principal...")
        return
    else:
        print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
