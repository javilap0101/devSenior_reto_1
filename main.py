from tabulate import tabulate
from datetime import datetime

class Experiment:
    def __init__(self, tipo, fecha, nombre, resultados):
        self.tipo = tipo
        self.fecha = fecha
        self.nombre = nombre
        self.resultados = resultados


# 1. Recopilación de datos experimentales: 
def add_experiment(experimentos):
    tipos_experimentos = ["Física", "Química", "Biología"]
    nombres_experimentos = [["Caída Libre", "MRU", "Ley de Hooke"], ["Reacción de neutralización", "Electrólisis del agua", "Reacción ácido-base"], ["Germinación","Fotosíntesis","Reproducción"]]
    
    tipo_experimento = None
    fecha = None
    nombre_experimento = None

    print("\nSeleccione el tipo del experimento: ")
    for i, tipo in enumerate(tipos_experimentos):    
        print(f"{i+1}.{tipo}")   # Muestra los tiposde los experimentos
    while True: # Validación del tipo del experimento
        try:
            opcion_1 = int(input("Ingrese la opción del tipo del experimento realizado: "))
            if 1 <= opcion_1 <= len(tipos_experimentos):
                tipo_experimento = tipos_experimentos[opcion_1 - 1]
                break
            else:    
                print("ERROR: Opcion no valida. Intente nuevamente.")
        except ValueError:
            print("ERROR: Formato de opcion incorrecto. Debe ser un numero.")

    
    while True: # Validación de la fecha del experimento
        fecha_str = input("\nIngrese la fecha del experimento (DD/MM/AAAA): ")
        
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            if fecha > datetime.now():
                print("ERROR: El experimento no puede tener una fecha futura!")
            else:    
                break
        except ValueError:
            print("ERROR: Formato de fecha incorrecto. Debe ser DD/MM/AAAA.")
            
    print("\nSeleccione el nombre del experimento: ")
    for i, nombre in enumerate(nombres_experimentos[opcion_1 - 1]):
        print(f"{i+1}.{nombre}") # Muestra los nombres de los experimentos
    while True: # Validación del nombre del experimento seleccionado
        try:
            opcion_2 = int(input("Ingrese la opción del nombre del experimento: "))
            if 1 <= opcion_2 <= len(nombres_experimentos[opcion_1 - 1]):
                nombre_experimento = nombres_experimentos[opcion_1 - 1][opcion_2 - 1]
                break
            else:    
                print("ERROR: Opcion no valida. Intente nuevamente.")
        except ValueError:
            print("ERROR: Formato de opcion incorrecto. Debe ser un numero.")
    
    resultados_str = input("Ingrese los resultados del experimento separados por comas (p.e 1,4,6): ")
    resultados = list(map(float, resultados_str.split(",")))

    # Se crea la instancia del experimento
    experimento = Experiment(tipo_experimento, fecha, nombre_experimento, resultados)
    experimentos.append(experimento)
    print("\nExperimento creado exitosamente!")


def show_experiment(experimentos):
    if(experimentos):
        print("\nExperimentos disponibles:")
        # Utilizar la libreria tabulate para mostrar los experimentos
        datos = [["Fecha", "Tipo", "Experimento", "Resultados"]]
        for datos_experimento in experimentos:
            datos.append([datos_experimento.fecha.strftime("%d/%m/%Y"), datos_experimento.tipo, datos_experimento.nombre,  ", ".join(map(str, datos_experimento.resultados))])
        # .join(map(str, experimento.resultados))])
        # La función map aplica la función str a cada elemento de la lista experimento.resultados
        # concatena los elementos de la lista experimento.resultados con un separador ","
        print(tabulate(datos, headers="firstrow", tablefmt="fancy_grid"))
    else:
        print("ERROR: No hay experimentos disponibles.")
   

def manage_experiment(experimentos):
    # submenú de gestionar experimentos
    print("\nSeleccione una de las siguientes opciones:")
    print("1. Crear experimento")   
    print("2. Mostrar experimento")
    print("3. Regresar al menú principal")
    option = input("Ingrese su opción: ")
    if option == "1":
        add_experiment(experimentos)
    elif option == "2":
        show_experiment(experimentos)
    elif option == "3":
        print("Regresando al menu principal...") 
        menu()
    else:
        print("ERROR: Opcion invalida. Por favor ingrese una opcion correcta.")
        return


# 2. Análisis de resultados:
def analysis_of_results(experimentos):
    pass

# 3. Generación de informe:
def generate_report(experimentos):
    pass

def export_report_to_txt(experimentos):
    pass

def menu():
    experimentos = []
    
    while True:
        print("\nSeleccione una de las siguientes opciones:")
        print("1. Gestionar experimentos")
        print("2. Analisis de resultados")
        print("3. Generar informe")
        print("4. Exportar informe a txt")
        print("5. Salir")
        option = input("Ingrese su opcion: ")
        if option == "1":
            manage_experiment(experimentos)
        elif option == "2":
            analysis_of_results(experimentos)
        elif option == "3":
            generate_report(experimentos)
        elif option == "4":
            export_report_to_txt(experimentos)
        elif option == "5":
            break
        else:
            print("ERROR: Opcion invalida. Por favor ingrese una opcion entre 1 y 5.") 

menu()