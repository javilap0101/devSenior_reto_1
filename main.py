import statistics
from tabulate import tabulate
from datetime import datetime

class Experiment:
    """
    Representa un experimento con sus atributos principales.
    
    Atributos:
        name (str): Nombre del experimento.
        date (datetime): Fecha del experimento.
        type_experiment (str): Tipo de experimento (Física, Química, Biología).
        results (list): Lista de resultados numéricos del experimento.
        avg (float): Promedio de los resultados.
        min (float): Valor mínimo de los resultados.
        max (float): Valor máximo de los resultados.
    """
    def __init__(self, name, date, type_experiment, results):
        self.name = name
        self.date = date
        self.type_experiment = type_experiment
        self.results = results
        self.avg = statistics.mean(results)
        self.min = min(results)
        self.max = max(results)

# 1. Recopilación de datos experimentales: 
def add_experiment(experiments):
    """
    Crea un nuevo experimento y lo agrega a la lista de experimentos.

    Argumentos:
        experiments (list): Lista de experimentos existentes.
    """
    type_experiments = ["Física", "Química", "Biología"]
    name_experiments = [["Caída Libre", "MRU", "Ley de Hooke"], ["Reacción de neutralización", "Electrólisis del agua", "Reacción ácido-base"], ["Germinación","Fotosíntesis","Reproducción"]]
    
    print("\nSeleccione el tipo de experimento: ")
    for i, type_experiment in enumerate(type_experiments):    
        print(f"{i+1}. {type_experiment}")   # Muestra los nombres de los experimentos
    while True: # Validación del nombre del experimento
        try:
            option_1 = int(input("Ingrese el número del tipo de experimento: "))
            if 1 <= option_1 <= len(type_experiments):
                type_experiment = type_experiments[option_1 - 1]
                break
            else:    
                print("ERROR: Opción no valida. Intente nuevamente.")
        except ValueError:
            print("ERROR: Formato de opcion incorrecto. Debe ser un numero.")

    
    while True: # Validación de la fecha del experimento
        date_str = input("\nIngrese la fecha del experimento (DD/MM/AAAA): ")
        
        try:
            date = datetime.strptime(date_str, "%d/%m/%Y")
            if date > datetime.now():
                print("ERROR: El experimento no puede tener una fecha futura!")
            else:    
                break
        except ValueError:
            print("ERROR: Formato de fecha incorrecto. Debe ser DD/MM/AAAA.")
            
    print("\nSeleccione el nombre del experimento: ")
    for i, name in enumerate(name_experiments[option_1 - 1]):
        print(f"{i+1}. {name}") # Muestra los tipos de experimentos
    while True: # Validación del tipo de experimento
        try:
            option_2 = int(input("Ingrese el número del nombre dl experimento: "))
            if 1 <= option_2 <= len(name_experiments[option_1 - 1]):
                name = name_experiments[option_1 - 1][option_2 - 1]
                break
            else:    
                print("ERROR: Opcion no valida. Intente nuevamente.")
        except ValueError:
            print("ERROR: Formato de opcion incorrecto. Debe ser un numero.")

    results_str = input("Ingrese los resultados del experimento separados por comas (p.e 1,4,6): ")
    results = list(map(float, results_str.split(",")))
    experimento = Experiment(name, date, type_experiment, results)
    experiments.append(experimento)
    print("Experimento creado exitosamente!")

def show_experiment(experiments):
    """
    Muestra todos los experimentos registrados en una tabla utilizando tabulate.

    Argumentos:
        experiments (list): Lista de experimentos existentes.
    """
    if(experiments):
        print("\nExperimentos disponibles:")
    # Utilizar la libreria tabulate para mostrar los experimentos
        datos = [["Experimento", "Fecha", "Tipo", "Resultados"]]
        for experiment in experiments:
            datos.append([experiment.name, experiment.date.strftime("%d/%m/%Y"), experiment.type_experiment, ", ".join(map(str, experiment.results))])
        # .join(map(str, experimento.resultados))])
        # La función map aplica la función str a cada elemento de la lista experimento.resultados
        # concatena los elementos de la lista experimento.resultados con un separador ","
        print(tabulate(datos, headers="firstrow", tablefmt="fancy_grid"))
    else:
        print("ERROR: No hay experimentos disponibles.")
   
# submenú de gestionar experimentos
def manage_experiment(experiments):
    """
    Gestiona la creación y visualización de experimentos.

    Argumentos:
        experiments (list): Lista de experimentos existentes.
    """
    print("\nSeleccione una de las siguientes opciones:")
    print("1. Crear experimento")   
    print("2. Mostrar experimento")
    print("3. Regresar al menú principal")
    option = input("Ingrese su opción: ")
    if option == "1":
        add_experiment(experiments)
    elif option == "2":
        show_experiment(experiments)
    elif option == "3":
        print("Regresando al menu principal...") 
        return
    else:
        print("ERROR: Opcion invalida. Por favor ingrese una opcion correcta.")
        return

# 2. Análisis de resultados:
def analysis_of_results(experiments):
    """
    Gestiona el análisis de los resultados de los experimentos registrados y comparación entre los mismos.

    Argumentos:
        experiments (list): Lista de experimentos registrados.

    """    
    if not experiments:
        print("ERROR: No hay experimentos para realizar análisis")
    else:
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
            return
        else:
            print("ERROR: Opcion invalida. Por favor ingrese una opcion correcta.")

def show_analysis_of_result(experiment):
    """
    Muestra las estadísticas básicas de un experimento específico (promedio, valor mínimo y valor máximo).

    Args:
        experiment (Experiment): Objeto del tipo `Experiment` que contiene los datos del experimento.
    """
    print(f"\nEl Experimento: {experiment.name} tiene las siguientes estadisticas:")
    print(f"1. Tiene un promedio de: {experiment.avg:.2f}")
    print(f"2. El valor mínimo registrado fue de: {experiment.min}")
    print(f"3. El valor máximo registrado fue de: {experiment.max}")

def show_comparision_experiments(experiments):
    """
    Compara los resultados de múltiples experimentos registrados.

    Identifica los siguientes aspectos:
        1. El experimento con el promedio más alto.
        2. El experimento con el valor mínimo más bajo.
        3. El experimento con el valor máximo más alto.

    Args:
        experiments (list): Lista de experimentos registrados.

    """
    if len(experiments) < 2:
        print("ERROR: No hay experimentos suficientes para realizar una comparación")
    else:
        # Encontrar el índice y el experimento con el valor mínimo más bajo
        min_result = min(enumerate(experiments), key=lambda x: x[1].min)
        min_index, min_experiment = min_result[0], min_result[1]

        # Encontrar el índice y el experimento con el valor máximo más alto
        max_result = max(enumerate(experiments), key=lambda x: x[1].max)
        max_index, max_experiment = max_result[0], max_result[1]

        # Encontrar el índice y el experimento con el valor promedio más alto
        avg_result = max(enumerate(experiments), key=lambda x: x[1].avg)
        avg_index, avg_experiment = avg_result[0], avg_result[1]
        
        print(f"\nEl experimento con el promedio mas alto es el # {avg_index + 1}")
        print(f"El experimento lleva por nombre {avg_experiment.name}")
        print(f"\nEl experimento que tuvo el valor mínimo mas bajo es el # {min_index + 1}")
        print(f"El experimento lleva por nombre {min_experiment.name}")
        print(f"\nEl experimento que tuvo el valor máximo mas alto es el # {max_index + 1}")
        print(f"El experimento lleva por nombre {max_experiment.name}")

# 3. Generación de informe:
def generate_report(experiments):
    """
    Genera un reporte completo sobre los experimentos registrados.

    El reporte incluye:
        1. El número total de experimentos registrados.
        2. Un listado de todos los experimentos con sus detalles.
        3. Una comparación entre experimentos, si hay al menos dos.

    Args:
        experiments (list): Lista de experimentos registrados.
        
    """
    if not experiments:
        print("ERROR: No hay experimentos para generar reporte!")
    else:
        print("="*50)
        print(f"Se han registrado {len(experiments)} experimentos")
        print("="*50)
        print("Listado de experimentos: ")
        show_experiment(experiments)
        if len(experiments) > 1:
            print("="*50)
            print("Comparación de experimentos: ")
            show_comparision_experiments(experiments)
        print("Reporte generado correctamente")

def export_report_to_txt(experiments):
    """
    Exporta un reporte detallado de los experimentos registrados a un archivo de texto.

    El reporte incluye:
        1. El número total de experimentos registrados.
        2. Un listado detallado de todos los experimentos con sus características.
        3. Una comparación entre experimentos (si hay más de uno), indicando:
           - El experimento con el promedio más alto.
           - El experimento con el valor mínimo más bajo.
           - El experimento con el valor máximo más alto.

    Args:
        experiments (list): Lista de objetos `Experiment` registrados.
        
    """
    if not experiments:
        print("ERROR: No hay experimentos para exportar reporte")
    else:
        with open("reporte.txt", "w", encoding="utf-8") as file:
            file.write("\n")
            file.write("="*50)
            file.write("\nReporte General")
            file.write("\n")
            file.write("="*50)
            file.write(f"\nSe han registrado {len(experiments)} experimentos")
            file.write("\n")
            file.write("="*50)
            file.write("\nListado de Experimentos: ")
            for i, experiment in enumerate(experiments, start=1):
                file.write(f"\n\nExperimento {i}")
                file.write(f"\nTipo de Experimento: {experiment.type_experiment}")
                file.write(f"\nNombre: {experiment.name}")
                file.write(f"\nFecha: {experiment.date.strftime("%d/%m/%Y")}")
                file.write(f"\nResultados: {experiment.results}")
                file.write(f"\nPromedio: {experiment.avg}")
                file.write(f"\nValor mínimo: {experiment.min}")
                file.write(f"\nValor máximo: {experiment.results}")
                
            if len(experiments) > 1:
                min_result = min(enumerate(experiments), key=lambda x: x[1].min)
                min_index, min_experiment = min_result[0], min_result[1]

                # Encontrar el índice y el experimento con el valor máximo más alto
                max_result = max(enumerate(experiments), key=lambda x: x[1].max)
                max_index, max_experiment = max_result[0], max_result[1]

                # Encontrar el índice y el experimento con el valor promedio más alto
                avg_result = max(enumerate(experiments), key=lambda x: x[1].avg)
                avg_index, avg_experiment = avg_result[0], avg_result[1]
                
                file.write("\n")
                file.write("="*50)
                file.write(f"\nEl experimento con el promedio mas alto es el # {avg_index + 1}")
                file.write(f"\nEl experimento lleva por nombre {avg_experiment.name}")
                file.write(f"\nEl experimento que tuvo el valor mínimo mas bajo es el # {min_index + 1}")
                file.write(f"\nEl experimento lleva por nombre {min_experiment.name}")
                file.write(f"\nEl experimento que tuvo el valor máximo mas alto es el # {max_index + 1}")
                file.write(f"\nEl experimento lleva por nombre {max_experiment.name}")
        print("Reporte generado correctamente")

def show_menu():
    """
    Muestra el menú principal de la aplicación y maneja las interacciones del usuario.
    
    """
    experiments = []
    
    while True:
        print("\nSeleccione una de las siguientes opciones:")
        print("1. Gestionar experimentos")
        print("2. Analisis de resultados")
        print("3. Generar informe")
        print("4. Exportar informe a txt")
        print("5. Salir")
        option = input("Ingrese su opcion: ")
        if option == "1":
            manage_experiment(experiments)
        elif option == "2":
            analysis_of_results(experiments)
        elif option == "3":
            generate_report(experiments)
        elif option == "4":
            export_report_to_txt(experiments)
        elif option == "5":
            break
        else:
            print("ERROR: Opcion invalida. Por favor ingrese una opcion entre 1 y 5.") 

show_menu()