import sys
import App.logic as logic

data_structure = None

def new_logic(data_structure):
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic(data_structure)
    return control
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    neighbourhoods, taxis = logic.load_data(control)
    return print(neighbourhoods, taxis)
    #TODO: Realizar la carga de datos


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    
    """
    pasajeros = int(input("Por favor ingrese la cantidad de pasajeros: "))
    resultado = logic.req_1(control, pasajeros)
    print("\n=== RESULTADO REQ 1 ===")
    print(f"Tiempo de ejecución: {resultado['tiempo_ejecucion_ms']} ms")
    print(f"Total trayectos: {resultado['total_trayectos']}")
    print(f"Duración promedio (min): {resultado['duracion_promedio(min)']}")
    print(f"Costo total promedio: {resultado['costo_total_promedio']}")
    print(f"Distancia promedio (millas): {resultado['distancia_promedio_millas']}")
    print(f"Peajes promedio: {resultado['peajes_promedio']}")
    print(f"Propina promedio: {resultado['propina_promedio']}")
    print(f"Método de pago más usado: {resultado['metodo_pago_mas_usado']}")
    print(f"Fecha inicio más frecuente: {resultado['fecha_inicio_mas_frecuente']}\n")
    # TODO: Imprimir el resultado del requerimiento 1



def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    metodo_p = str(input("Ingrese el método de pago: "))
    resultado = logic.req_2(control, metodo_p)
    print("\n=== RESULTADO REQ 2 ===")
    print(f"Total trayectos: {resultado['total_trayectos']}")
    print(f"Duración promedio (min): {resultado['duración_promedio(min)']}")
    print(f"Costo total promedio: {resultado['costo_total_promedio']}")
    print(f"Distancia promedio (millas): {resultado['distancia_promedio_millas']}")
    print(f"Peajes promedio: {resultado['peajes_promedio']}")
    print(f"Propina promedio: {resultado['propina_promedio']}")
    print(f"Pasajeros más frecuente: {resultado['pasajeros_mas_frecuente']}")
    print(f"Fecha finalización más frecuente: {resultado['fecha_finalizacion']}\n")
    # TODO: Imprimir el resultado del requerimiento 2


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    valor_menor = float(input("Por favor ingrese el valor minimo del viaje: "))
    valor_mayor = float(input("Por favor ingrese el valor maximo del viaje"))
    resultado = logic.req_3(control,valor_menor,valor_mayor)
    return print(resultado)
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    filtro = str(input("Por favor ingrese su filtro (MAYOR-MENOR): "))
    fecha_ini = str(input("Ahora ingrese la fecha Inicial (Debe estar en formato %Y-%m-%d): "))
    fecha_fin = str(input("Ahora ingrese la fecha final (Debe estar en formato %Y-%m-%d): "))
    resultado = logic.req_4(control,fecha_ini,fecha_fin,filtro)
    return print(resultado)
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    filtro = str(input("Por favor ingrese la selección de costo (MAYOR/MENOR): "))
    fecha_ini = str(input("Ahora ingrese la fecha inicial (formato %Y-%m-%d): "))
    fecha_fin = str(input("Ahora ingrese la fecha final (formato %Y-%m-%d): "))
    resultado = logic.req_5(control, filtro, fecha_ini, fecha_fin)
    print("\n=== RESULTADO REQ 5 ===")
    print(f"Tiempo de ejecución: {resultado['tiempo_ms']} ms")
    print(f"Total trayectos filtrados: {resultado['total_trayectos_filtrados']}")
    print(f"Franja horaria: {resultado['franja_horaria']}")
    print(f"Costo promedio: {resultado['costo_promedio']}")
    print(f"Número de trayectos: {resultado['numero_trayectos']}")
    print(f"Duración promedio: {resultado['duracion_promedio']}")
    print(f"Pasajeros promedio: {resultado['pasajeros_promedio']}")
    print(f"Costo mayor: {resultado['costo_mayor']}")
    print(f"Costo menor: {resultado['costo_menor']}\n")
    
    # TODO: Imprimir el resultado del requerimiento 5


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    barrio = str(input("Por favor ingrese el barrio de inicio:"))
    fecha_ini = str(input("Ahora ingrese la fecha Inicial (Debe estar en formato %Y-%m-%d): "))
    fecha_fin = str(input("Ahora ingrese la fecha final (Debe estar en formato %Y-%m-%d): "))
    resultado = logic.req_6(control,fecha_ini,fecha_fin,barrio)
    return print (resultado)
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic(data_structure)

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
