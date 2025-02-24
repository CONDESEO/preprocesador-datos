import modules.data_loader as dl
#import modules.preprocessing as pp
#import modules.visualization as vz
#import modules.exporter as ex

def main():
    dataset = None
    preprocessed = False
    while True:
        print("\n====================")
        print("Menú Principal")
        print("====================")
        print("[1] Cargar datos")
        print("[2] Preprocesar datos" if dataset else "[✗] Preprocesar datos (requiere carga)")
        print("[3] Visualizar datos" if preprocessed else "[✗] Visualizar datos (requiere preprocesado)")
        print("[4] Exportar datos" if preprocessed else "[✗] Exportar datos (requiere preprocesado)")
        print("[5] Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == "1":
            dataset = dl.cargar_datos()
        elif choice == "2" and dataset:
            dataset = pp.procesar(dataset)
            preprocessed = True
        elif choice == "3" and preprocessed:
            vz.visualizar(dataset)
        elif choice == "4" and preprocessed:
            ex.exportar(dataset)
        elif choice == "5":
            break
        else:
            print("Opción inválida o bloqueada.")

if __name__ == "__main__":
    main()
