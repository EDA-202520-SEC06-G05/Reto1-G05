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
    pass


def print_req_2(control):
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
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
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


def req_4(catalog, fecha_ini, fecha_fin, filtro):
    """
    Retorna el resultado del requerimiento 4
    """
    tiempo_inicial = get_time()
    diccionario = {
        "tiempo_ejecucion" : 0,
        "filtro_seleccioando" : filtro,
        "numero_viajes_totales" : 0,
        "busquedad_barrio_filtro" : {},
        
        }
    barrios_filtrados = barrios(catalog)
    for i in catalog["taxis_info"]["elements"]:
        lista_inicio = []
        lista_final = []
        fecha_inicial = i["pickup_datetime"]
        fecha_inicial = fecha_inicial[:10]
        if fecha_ini <= fecha_inicial <= fecha_fin:
            diccionario["numero_viajes_totales"] +=1
            latitud = float(i["pickup_latitude"].replace(",", "."))
            longitud = float(i["pickup_longitude"].replace(",", "."))
            latitud_llegada = float(i["dropoff_latitude"].replace(",", "."))
            longitud_llegada = float(i["dropoff_longitude"].replace(",", "."))
            if barrios_filtrados["Manhattan"]["elements"][0]["west"] <= longitud <= barrios_filtrados["Manhattan"]["elements"][0]["east"] and barrios_filtrados["Manhattan"]["elements"][0]["south"] <= latitud <= barrios_filtrados["Manhattan"]["elements"][0]["north"]:
                for each in barrios_filtrados["Manhattan"]["elements"][1]["elements"]:
                    latitud_barrio = float(each["latitude"].replace(",", "."))
                    longitud_barrio = float(each["longitude"].replace(",", "."))
                    distancia = harvesine_miles(latitud, longitud, latitud_barrio, longitud_barrio)
                    lista_inicio.append((each["neighborhood"], distancia))
                    ditancia_llegada = harvesine_miles(latitud_llegada, longitud_llegada, latitud_barrio, longitud_barrio)
                    lista_final.append((each["neighborhood"], ditancia_llegada))
            elif barrios_filtrados["Brooklyn"]["elements"][0]["west"] <= longitud <= barrios_filtrados["Brooklyn"]["elements"][0]["east"] and barrios_filtrados["Brooklyn"]["elements"][0]["south"] <= latitud <= barrios_filtrados["Brooklyn"]["elements"][0]["north"]:
                for each in barrios_filtrados["Brooklyn"]["elements"][1]["elements"]:
                    latitud_barrio = float(each["latitude"].replace(",", "."))
                    longitud_barrio = float(each["longitude"].replace(",", "."))
                    distancia = harvesine_miles(latitud, longitud, latitud_barrio, longitud_barrio)
                    lista_inicio.append((each["neighborhood"], distancia))
                    ditancia_llegada = harvesine_miles(latitud_llegada, longitud_llegada, latitud_barrio, longitud_barrio)
                    lista_final.append((each["neighborhood"], ditancia_llegada))
            elif barrios_filtrados["Queens"]["elements"][0]["west"] <= longitud <= barrios_filtrados["Queens"]["elements"][0]["east"] and barrios_filtrados["Queens"]["elements"][0]["south"] <= latitud <= barrios_filtrados["Queens"]["elements"][0]["north"]:
                for each in barrios_filtrados["Queens"]["elements"][1]["elements"]:
                    latitud_barrio = float(each["latitude"].replace(",", "."))
                    longitud_barrio = float(each["longitude"].replace(",", "."))
                    distancia = harvesine_miles(latitud, longitud, latitud_barrio, longitud_barrio)
                    lista_inicio.append((each["neighborhood"], distancia))
                    ditancia_llegada = harvesine_miles(latitud_llegada, longitud_llegada, latitud_barrio, longitud_barrio)
                    lista_final.append((each["neighborhood"], ditancia_llegada))
            elif barrios_filtrados["Bronx"]["elements"][0]["west"] <= longitud <= barrios_filtrados["Bronx"]["elements"][0]["east"] and barrios_filtrados["Bronx"]["elements"][0]["south"] <= latitud <= barrios_filtrados["Bronx"]["elements"][0]["north"]:
                for each in barrios_filtrados["Bronx"]["elements"][1]["elements"]:

                    latitud_barrio = float(each["latitude"].replace(",", "."))
                    longitud_barrio = float(each["longitude"].replace(",", "."))
                    distancia = harvesine_miles(latitud, longitud, latitud_barrio, longitud_barrio)
                    lista_inicio.append((each["neighborhood"], distancia))
                    ditancia_llegada = harvesine_miles(latitud_llegada, longitud_llegada, latitud_barrio, longitud_barrio)
                    lista_final.append((each["neighborhood"], ditancia_llegada))
            elif barrios_filtrados["Staten Island"]["elements"][0]["west"] <= longitud <= barrios_filtrados["Staten Island"]["elements"][0]["east"] and barrios_filtrados["Staten Island"]["elements"][0]["south"] <= latitud <= barrios_filtrados["Staten Island"]["elements"][0]["north"]:
                for each in barrios_filtrados["Staten Island"]["elements"][1]["elements"]:
                    latitud_barrio = float(each["latitude"].replace(",", "."))
                    longitud_barrio = float(each["longitude"].replace(",", "."))
                    distancia = harvesine_miles(latitud, longitud, latitud_barrio, longitud_barrio)
                    lista_inicio.append((each["neighborhood"], distancia))
                    ditancia_llegada = harvesine_miles(latitud_llegada, longitud_llegada, latitud_barrio, longitud_barrio)
                    lista_final.append((each["neighborhood"], ditancia_llegada))
            menor = lista_inicio[0]     
            p = 1
            while p < len(lista_inicio):
                if lista_inicio[p][1] < menor[1]:
                    menor = lista_inicio[p]
                p += 1
            barrio_inicio = menor[0]
            menor_1 = lista_final[0]
            j = 1
            while j < len(lista_final):
                if lista_final[j][1] < menor_1[1]:
                    menor_1 = lista_final[j]
                j += 1
            barrio_final = menor_1[0]
            
            if barrio_inicio == barrio_final:
                None
            else:
                llave = str(barrio_inicio) + " - " + str(barrio_final)
                if llave in diccionario["busquedad_barrio_filtro"]:
                    tiempo = i["dropoff_datetime"]
                    tiempo = tiempo[11:]
                    tiempo = tiempo.split(":")
                    hora, minuto, segundo = int(tiempo[0]), int(tiempo[1]), int(tiempo[2])
                    minutos_totales = hora * 60 + minuto + (segundo / 60)
                    diccionario["busquedad_barrio_filtro"][llave]["distancia_promedio"] += float(i["trip_distance"])
                    diccionario["busquedad_barrio_filtro"][llave]["tiempo_promedio"] += minutos_totales
                    diccionario["busquedad_barrio_filtro"][llave]["costo_promedio"] += float(i["total_amount"])
                    
                else:
                    tiempo = i["dropoff_datetime"]
                    tiempo = tiempo[11:]
                    tiempo = tiempo.split(":")
                    hora, minuto, segundo = int(tiempo[0]), int(tiempo[1]), int(tiempo[2])
                    minutos_totales = hora * 60 + minuto + (segundo / 60)
                    
                    diccionario["busquedad_barrio_filtro"][llave] = {
                        "barrio_inicio": barrio_inicio,
                        "barrio_final": barrio_final,
                        "distancia_promedio" : float(i["trip_distance"]),
                        "tiempo_promedio": minutos_totales,
                        "costo_promedio": float(i["total_amount"]),
                    }
                    
    valor = 0
    barrio = None
    for each in diccionario["busquedad_barrio_filtro"]:
        diccionario["busquedad_barrio_filtro"][each]["distancia_promedio"] = diccionario["busquedad_barrio_filtro"][each]["distancia_promedio"] / diccionario["numero_viajes_totales"]
        diccionario["busquedad_barrio_filtro"][each]["tiempo_promedio"]    = diccionario["busquedad_barrio_filtro"][each]["tiempo_promedio"] / diccionario["numero_viajes_totales"]
        diccionario["busquedad_barrio_filtro"][each]["costo_promedio"]     = diccionario["busquedad_barrio_filtro"][each]["costo_promedio"] / diccionario["numero_viajes_totales"]

        if filtro == "MAYOR":
            if valor == 0 or diccionario["busquedad_barrio_filtro"][each]["costo_promedio"] > valor:
                    valor = diccionario["busquedad_barrio_filtro"][each]["costo_promedio"]
                    barrio = diccionario["busquedad_barrio_filtro"][each]

        elif filtro == "MENOR":
            if valor == 0 or diccionario["busquedad_barrio_filtro"][each]["costo_promedio"] < valor:
                    valor = diccionario["busquedad_barrio_filtro"][each]["costo_promedio"]
                    barrio = diccionario["busquedad_barrio_filtro"][each]
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)
    diccionario["tiempo_ejecucion"] = tiempo_total
    diccionario["barrio_inicio"] = barrio["barrio_inicio"]
    diccionario["barrio_final"] = barrio["barrio_final"]
    diccionario["distancia_promedio"] = barrio["distancia_promedio"]
    diccionario["tiempo_promedio"] = barrio["tiempo_promedio"]
    diccionario["costo_promedio"] = barrio["costo_promedio"]
    del diccionario["busquedad_barrio_filtro"]
    return diccionario
