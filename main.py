import statistics
from tabulate import tabulate
from datetime import datetime

class Experiment:
    def __init__(self, name, date, type_experiment, results):
        self.name = name
        self.date = date
        self.type_experiment = type_experiment
        self.results = results
        self.avg = statistics.mean(results)
        self.min = min(results)
        self.max = max(results)


# 1. Recopilación de datos experimentales: 
def add_experiment(experimentos):
    nombre_experimentos = ["Física", "Química", "Biología"]
    tipos_experimentos = [["Caída Libre", "MRU", "Ley de Hooke"], ["Reacción de neutralización", "Electrólisis del agua", "Reacción ácido-base"], ["Germinación","Fotosíntesis","Reproducción"]]
    
    print("\nSeleccione el nombre del experimento: ")
    for i, nombre in enumerate(nombre_experimentos):    
        print(f"{i+1}. {nombre}")   # Muestra los nombres de los experimentos
    while True: # Validación del nombre del experimento
        try:
            opcion_1 = int(input("Ingrese el número del experimento: "))
            if 1 <= opcion_1 <= len(nombre_experimentos):
                nombre = nombre_experimentos[opcion_1 - 1]
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
            
    print("\nSeleccione el tipo de experimento: ")
    for i, tipo in enumerate(tipos_experimentos[opcion_1 - 1]):
        print(f"{i+1}. {tipo}") # Muestra los tipos de experimentos
    while True: # Validación del tipo de experimento
        try:
            opcion_2 = int(input("Ingrese el numero del experimento: "))
            if 1 <= opcion_2 <= len(tipos_experimentos[opcion_1 - 1]):
                tipo_experimento = tipos_experimentos[opcion_1 - 1][opcion_2 - 1]
                break
            else:    
                print("ERROR: Opcion no valida. Intente nuevamente.")
        except ValueError:
            print("ERROR: Formato de opcion incorrecto. Debe ser un numero.")
    
    resultados_str = input("Ingrese los resultados del experimento separados por comas (p.e 1,4,6): ")
    resultados = list(map(float, resultados_str.split(",")))
    experimento = Experiment(nombre, fecha, tipo_experimento, resultados)
    experimentos.append(experimento)
    print("Experimento creado exitosamente!")


def show_experiment(experimentos):
    if(experimentos):
        print("\nExperimentos disponibles:")
    # Utilizar la libreria tabulate para mostrar los experimentos
        datos = [["Experimento", "Fecha", "Tipo", "Resultados"]]
        for experimento in experimentos:
            datos.append([experimento.nombre, experimento.fecha.strftime("%d/%m/%Y"), experimento.tipo, ", ".join(map(str, experimento.resultados))])
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
        show_menu()
    else:
        print("ERROR: Opcion invalida. Por favor ingrese una opcion correcta.")
        return


# 2. Análisis de resultados:
def analysis_of_results(experiments):
    print("\nSeleccione una de las siguientes opciones:")
    print("1. Cálcular estadisticas básicas")   
    print("2. Mostrar comparación entre experimentos")
    print("3. Regresar al menú principal")
    option = input("Ingrese su opción: ")
    if option == "1":    
        print("\nSeleccione uno de los siguientes experimentos para realizar los cálculos:")
        for i, experiment in enumerate(experiments, start=1):
            print(f"{i}. {experiment.name}")
        while True:
            try:
                analysis_option = int(input("Ingrese el número del experimento que desea analizar: "))
                if 1 <= analysis_option <= len(experiments):
                    show_analysis_of_result(experiments[analysis_option - 1])
                    break
                else:    
                    print("ERROR: Opcion no valida. Intente nuevamente.")
            except ValueError:
                print("ERROR: Formato de opción incorrecto. Debe ser un número.")
    elif option == "2":
        show_comparision_experiments(experiments)
    elif option == "3":
        print("Regresando al menu principal...") 
        show_menu()
    else:
        print("ERROR: Opcion invalida. Por favor ingrese una opcion correcta.")

def show_analysis_of_result(experiment):
    print(f"\nEl Experimento: {experiment.name} tiene las siguientes estadisticas:")
    print(f"1. Tiene un promedio de: {experiment.avg}")
    print(f"2. El valor mínimo registrado fue de: {experiment.min}")
    print(f"3. El valor máximo registrado fue de: {experiment.max}")

def show_comparision_experiments(experiments):
    pass

# 3. Generación de informe:
def generate_report(experimentos):
    pass

def export_report_to_txt(experimentos):
    pass

def show_menu():
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

show_menu()