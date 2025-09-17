import time
import csv
import os
from DataStructures.List import array_list as lt
import math

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-1'

def new_logic(data_structure):
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    data_structure = lt
    catalog = {
        "Neighborhoods": None,
        "taxis_info": None}
    catalog["Neighborhoods"] = lt.new_list()
    catalog["taxis_info"] = lt.new_list()
    return catalog
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    pass


# Funciones para la carga de datos

def load_data(catalog):
    """
    Carga los datos del reto
    """
    taxi = load_taxis(catalog)
    neigh = load_neigh(catalog)
    return taxi , neigh

    # TODO: Realizar la carga de datos
    pass

def load_neigh(catalog):
    neigh_file = data_dir + "/nyc-neighborhoods.csv"
    input_file = csv.DictReader(open(neigh_file, encoding="utf-8"), delimiter=";")
    for neigh in input_file:
        add_neigh(catalog, neigh)
    return neigh_size(catalog)

def load_taxis(catalog):
    
    inicio = get_time()
    
    trip_total = 0
    min_trip = None
    max_trip = None
    
    first5 = lt.new_list()
    last5 = lt.new_list()
    
    taxi_file = data_dir + "/taxis-large.csv"
    input_file = csv.DictReader(open(taxi_file, encoding="utf-8"), delimiter=",")
    for taxi in input_file:
        if taxi and "pickup_datetime" in taxi and "dropoff_datetime" in taxi:
            add_taxi(catalog, taxi)
            trip_total += 1
        
            pick_up = taxi["pickup_datetime"]
            dropoff = taxi["dropoff_datetime"]
            start = pick_up[11:16]
            finish = dropoff[11:16]
        
            h1str, m1str = start.split(":")
            h2str, m2str = finish.split(":")
        
            h1, m1 = int(h1str), int(m1str)
            h2, m2 = int(h2str), int(m2str)
        
            duration = (h2 *60 + m2) - (h1 *60 + m1)
            if duration < 0:
                duration += 24*60
        
            distance = float(taxi["trip_distance"])
            cost = float(taxi["total_amount"])
        
            register = {
                "pickup_datetime": pick_up,
                "dropoff_datetime": dropoff,
                "duration_min": duration,
                "distance": distance,
                "cost": cost    
            }
        
            if lt.size(first5) < 5:
                lt.add_last(first5, register)
        
            lt.add_last(last5, register)
            if lt.size(last5) > 5:
                lt.remove_first(last5)
        
            if distance > 0:
                if min_trip is None or distance < min_trip["distancia"]:
                    min_trip = {
                        "pickup_datetime": pick_up,
                        "distancia": distance,
                        "cost": cost
                    }
            if max_trip is None or distance > max_trip["distancia"]:
                max_trip = {
                    "pickup_datetime": pick_up,
                    "distancia": distance,
                    "cost": cost
            }
    fin = get_time()
    result = {
        "tiempo_carga_ms": float(fin) - float(inicio),
        "total_trayectos": trip_total,
        "trayecto_min": min_trip,
        "trayecto_max": max_trip,
        "primeros5": first5,
        "ultimos5": last5
    }
    return result    

def add_neigh(catalog, neigh):
    n = new_neigh(
        neigh["borough"],
        neigh["neighborhood"],
        neigh["latitude"],
        neigh["longitude"]
        )
    lt.add_last(catalog["Neighborhoods"], n)
    return catalog

def add_taxi(catalog, taxi):
    t = new_taxi_info(
        taxi["pickup_datetime"],
        taxi["dropoff_datetime"],
        taxi["passenger_count"],
        taxi["trip_distance"],
        taxi["pickup_longitude"],
        taxi["pickup_latitude"],
        taxi["rate_code"],
        taxi["dropoff_longitude"],
        taxi["dropoff_latitude"], 
        taxi["payment_type"],
        taxi["fare_amount"], 
        taxi["extra"], 
        taxi["mta_tax"],
        taxi["tip_amount"], 
        taxi["tolls_amount"], 
        taxi["improvement_surcharge"],
        taxi["total_amount"])
    lt.add_last(catalog["taxis_info"], t)
    return catalog
    
def new_neigh(borough, neighbor, lat, longi):
    neigh = {"borough":borough, 
            "neighborhood":neighbor, 
            "latitude":lat, 
            "longitude": longi}
    
    return neigh


def new_taxi_info(pickup, dropoff, passenger_count, trip_dist, 
                  pickup_longitude, pickup_latitude, rate_code, drop_long, drop_lat, payment, fare, extra, mta_tax, tip, tolls, improve, total):
    
    taxi_info = {"pickup_datetime":pickup, 
                "dropoff_datetime":dropoff, 
                "passenger_count":passenger_count, 
                "trip_distance": trip_dist, 
                "pickup_longitude": pickup_longitude,
                "pickup_latitude":pickup_latitude, 
                "rate_code": rate_code, 
                "dropoff_longitude": drop_long, 
                "dropoff_latitude": drop_lat, 
                "payment_type":payment, 
                "fare_amount":fare,
                "extra": extra, 
                "mta_tax": mta_tax, 
                "tip_amount": tip, 
                "tolls_amount": tolls, 
                "improvement_surcharge": improve, 
                "total_amount":total}
    return taxi_info

def neigh_size(catalog):
    return lt.size(catalog["Neighborhoods"])

def taxi_size(catalog):
    return lt.size(catalog["taxis_info"])
    
# Funciones de consulta sobre el catálogo    

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog, pasajeros):
    """
    Retorna el resultado del requerimiento 1
    """

    start_time = get_time() 
    contador=0
    sumatoria_duracion=0
    sumatoria_costo_total=0
    sumatoria_distancia=0
    sumatoria_peajes=0
    sumatoria_propinas=0
    conteo_metodos_pago={}
    conteo_fechas_inicio={}

    for i in range(0,lt.size(catalog["taxis_info"])):
        viaje = lt.get_element(catalog["taxis_info"], i)
        pc = int(viaje["passenger_count"])
        if (pc != 0) and (pc == pasajeros):
            contador+=1
            pickup= viaje["pickup_datetime"]
            dropoff= viaje["dropoff_datetime"]
            start= pickup[11:16]
            finish= dropoff[11:16]
            h1str,m1str= start.split(":")
            h2str,m2str=finish.split(":")
            h1,m1= int(h1str),int(m1str)
            h2,m2=int(h2str),int(m2str)
            duracion_sum= (h2*60+m2)-(h1*60+m1)
            if duracion_sum<0:
                duracion_sum+=24*60
            sumatoria_duracion += duracion_sum

            sumatoria_costo_total+= float(viaje["total_amount"])
            sumatoria_distancia+= float(viaje["trip_distance"])
            sumatoria_peajes+= float(viaje["tolls_amount"])
            sumatoria_propinas+= float(viaje["tip_amount"])

            metodo_pago=viaje["payment_type"]
            if metodo_pago in conteo_metodos_pago:
                conteo_metodos_pago[metodo_pago]+=1
            else:
                conteo_metodos_pago[metodo_pago]=1

            fecha=pickup[0:10] 
            if fecha in conteo_fechas_inicio:
                conteo_fechas_inicio[fecha]+=1
            else:
                conteo_fechas_inicio[fecha]=1
    if contador>0:
        duracion=sumatoria_duracion/contador
        costo_total=sumatoria_costo_total/contador
        distancia=sumatoria_distancia/contador
        peajes=sumatoria_peajes/contador
        propina=sumatoria_propinas/contador
    else:
        duracion=costo_total=distancia=peajes=propina=0
    metodo_frec=None
    cantidad_maxima=-1
    for metodo in conteo_metodos_pago:
        cantidad =conteo_metodos_pago[metodo]
        if cantidad >cantidad_maxima:
            cantidad_maxima=cantidad
            metodo_frec=str(metodo)+" - "+str(cantidad)
    fecha_frec=None
    max_fecha=-1
    for fecha in conteo_fechas_inicio:
        cantidad=conteo_fechas_inicio[fecha]
        if cantidad>max_fecha:
            max_fecha=cantidad
            fecha_frec=fecha
    end_time = get_time()  
    tiempo_ms = delta_time(start_time, end_time)        
    resultado={
        "tiempo_ejecucion_ms":tiempo_ms,
        "total_trayectos":contador,
        "duracion_promedio(min)":duracion,
        "costo_total_promedio":costo_total,
        "distancia_promedio_millas":distancia,
        "peajes_promedio":peajes,
        "metodo_pago_mas_usado":metodo_frec,
        "propina_promedio":propina,
        "fecha_inicio_mas_frecuente":fecha_frec
    }
    return resultado

    # TODO: Modificar el requerimiento 1


def req_2(catalog, filtro):

    contador = 0
    duration = 0
    total_costs = 0
    distancia = 0
    peajes = 0
    pasajeros = {}
    propina = 0  
    fechas = {}
    
    for each in range(0,lt.size(catalog["taxis_info"])):
        metodo = lt.get_element(catalog["taxis_info"],each)
        pm = str(metodo["payment_type"])        
        if pm == filtro:
            contador += 1
            
            pickup = metodo["pickup_datetime"]
            dropoff = metodo["dropoff_datetime"]
            start = pickup[11:16]
            finish = dropoff[11:16]
            h1str , m1str = start.split(":")
            h2str, m2str = finish.split(":")
            h1 , m1 = int(h1str), int(m1str)
            h2, m2 = int(h2str), int(m2str)
            duration_sum = (h2 *60 + m2) - (h1 *60 + m1)
            duration += duration_sum
            
            total_costs += float(metodo["total_amount"]) 
            distancia += float(metodo["trip_distance"]) 
            peajes += float(metodo["tolls_amount"])
            propina += float(metodo["tip_amount"])
            
            num_pasajeros = int(metodo["passenger_count"])
            if num_pasajeros in pasajeros:
                pasajeros[num_pasajeros]+=1
            else:
                pasajeros[num_pasajeros] = 1
                
            fecha = dropoff[0:10]
            if fecha in fechas:
                fechas[fecha] += 1
            else: 
                fechas[fecha] = 1
    
    if contador > 0:
        duration = duration / contador
        total_costs = total_costs / contador
        distancia = distancia / contador
        peajes = peajes / contador
        propina = propina / contador
        
    pasajero_frec = None
    cantidad_max = -1 
    for num_pasajeros in pasajeros:
        cantidad = pasajeros[num_pasajeros]
        if cantidad > cantidad_max:
            cantidad_max = cantidad
            pasajero_frec = str(num_pasajeros)+ "-"+ str(cantidad)
    
    fecha_frec = None
    max_fecha = -1
    for fecha in fechas:
        cantidad = fechas[fecha]
        if cantidad > max_fecha:
            max_fecha = cantidad
            fecha_frec = fecha 
                
    resultado = {
        "total_trayectos": contador,
        "duración_promedio(min)": duration,
        "costo_total_promedio": total_costs,
        "distancia_promedio_millas": distancia,
        "peajes_promedio": peajes,
        "pasajeros_mas_frecuente": pasajero_frec,
        "propina_promedio": propina,
        "fecha_finalizacion": fecha_frec  
    }        
    return resultado

    """
    Retorna el resultado del requerimiento 2
    """   
# TODO: Modificar el requerimiento 2



def req_3(catalog,valor_menor, valor_mayor):
    """
    Retorna el resultado del requerimiento 3
    """
    time_start = get_time()
    
    contador = {
        "tiempo_ejecucion": 0,
        "numero_viajes": 0,
        "tiempo_promedio":0,
        "precio_promedio_usd":0,
        "disatancia_total_promedio":0,
        "precio_peaje_promedio": 0,
        "cantidad_pasajeros_frecuente" : {},
        "cantidad_propinas_promedio": 0,
        "fecha_promedio": {}
        }
    
    for taxi in catalog["taxis_info"]["elements"]:
        lista = []
        if (float(taxi["total_amount"])) >= float(valor_menor) and (float(taxi["total_amount"])) <= float(valor_mayor):
            contador["numero_viajes"] +=1
            lista = [taxi["pickup_datetime"], taxi["dropoff_datetime"]]
            hora, minuto , segundo = lista[0][11:].split(":")
            hora_inicial = int(hora) *60 + int(minuto) + (int (segundo) / 60)
            hora_final, minuto_final, segundo_final = lista[1][11:].split(":")
            hora_termino = int(hora_final) *60 + int(minuto_final) + (int (segundo_final)/ 60)
            if lista[0][:10] != lista[1][:10]:
                hora_termino += 24*60
            tiempo_viaje_total = hora_termino - hora_inicial
            contador["tiempo_promedio"] += tiempo_viaje_total
            
            if taxi["passenger_count"] in contador["cantidad_pasajeros_frecuente"]:
                contador["cantidad_pasajeros_frecuente"][taxi["passenger_count"]] += 1
            else:
                contador["cantidad_pasajeros_frecuente"][taxi["passenger_count"]] = 1
            
            if lista[1][:10] in contador["fecha_promedio"]:
                contador["fecha_promedio"][lista[1][:10]] += 1
            else:
                contador["fecha_promedio"][lista[1][:10]] = 1
                
            contador["precio_promedio_usd"] += float(taxi["total_amount"])
            contador["disatancia_total_promedio"] += float(taxi["trip_distance"])
            contador["precio_peaje_promedio"] += float(taxi["tolls_amount"])
            contador["cantidad_propinas_promedio"] += float(taxi["tip_amount"])
    if contador["numero_viajes"] == 0:
        contador["tiempo_ejecucion"] = delta_time(time_start, get_time())
        return contador
    contador["tiempo_promedio"] = contador["tiempo_promedio"]/contador["numero_viajes"]
    contador["precio_promedio_usd"] = contador["precio_promedio_usd"]/contador["numero_viajes"]
    contador["disatancia_total_promedio"] = contador["disatancia_total_promedio"]/contador["numero_viajes"]
    contador["precio_peaje_promedio"] = contador["precio_peaje_promedio"]/contador["numero_viajes"]
    contador["cantidad_propinas_promedio"] = contador["cantidad_propinas_promedio"]/contador["numero_viajes"]
    
    fecha_promedio = list(contador["fecha_promedio"].values())
    fecha_promedio = max(fecha_promedio)
    for fecha in contador["fecha_promedio"]:
        if contador["fecha_promedio"][fecha] == fecha_promedio:
            contador["fecha_promedio"] = fecha
            break
    
    cantidad_pasajeros= list(contador["cantidad_pasajeros_frecuente"].values())
    cantidad_pasajeros = max(cantidad_pasajeros)
    for cantidad in contador["cantidad_pasajeros_frecuente"]:
        if contador["cantidad_pasajeros_frecuente"][cantidad] == cantidad_pasajeros:
            contador["cantidad_pasajeros_frecuente"] = (cantidad, cantidad_pasajeros)
            break
    time_end = get_time()
    time_total = delta_time(time_start, time_end)
    contador["tiempo_ejecucion"] = time_total
    
    return contador 
    # TODO: Modificar el requerimiento 3
    pass

def barrios(catalog):
    barrios = lt.new_list()
    for each in catalog["Neighborhoods"]["elements"]:
        sub_barrios= {
            "neighborhood": each["neighborhood"],
            "latitude": each["latitude"],
            "longitude": each["longitude"]
        }
        lt.add_last(barrios, sub_barrios)
    filtro_barrio_grande = {
        "Manhattan": lt.new_list(),
        "Brooklyn": lt.new_list(),
        "Queens": lt.new_list(),
        "Bronx": lt.new_list(),
        "Staten Island": lt.new_list()
    }
    lt.add_last(filtro_barrio_grande["Manhattan"], lt.sub_list(barrios, 0, 10))   
    lt.add_last(filtro_barrio_grande["Brooklyn"],  lt.sub_list(barrios, 10, 6))   
    lt.add_last(filtro_barrio_grande["Queens"],    lt.sub_list(barrios, 16, 5))   
    lt.add_last(filtro_barrio_grande["Bronx"],     lt.sub_list(barrios, 21, 4))   
    lt.add_last(filtro_barrio_grande["Staten Island"], lt.sub_list(barrios, 25, 4))
    # Sacar la distancia en un plano cartesiano de los barrios para hacer un plano con los 5 cuadrados 
    for each in filtro_barrio_grande:
        lista = filtro_barrio_grande[each]
        sub_barrios = lt.last_element(lista)
        coordenadas = {
            "west" : None,
            "east":  None,
            "north":  None,
            "south": None
        }
        for sub in sub_barrios["elements"]:
            latitud = float(sub["latitude"].replace(",", "."))
            longitud = float(sub["longitude"].replace(",", "."))
            if coordenadas["north"] ==  None:
                coordenadas["north"] = latitud
            elif coordenadas["north"] < latitud:
                coordenadas["north"] = latitud
            if coordenadas["south"] ==  None:
                coordenadas["south"] = latitud
            elif coordenadas["south"] > latitud:
                coordenadas["south"] = latitud
            if coordenadas["east"] ==  None:
                coordenadas["east"] = longitud
            elif coordenadas["east"] < longitud:
                coordenadas["east"] = longitud
            if coordenadas["west"] ==  None:
                coordenadas["west"] = longitud
            elif coordenadas["west"] > longitud:
                coordenadas["west"] = longitud
        
        lt.add_first(lista, coordenadas)
    return filtro_barrio_grande

def harvesine_miles(lat1, lon1, lat2, lon2):
    R = 3958.8
    lat1 = lat1 * math.pi / 180
    lon1 = lon1 * math.pi / 180
    lat2 = lat2 * math.pi / 180
    lon2 = lon2 * math.pi / 180
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2) **2)
    c = 2 * math.asin(math.sqrt(a))
    return R * c

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
            if len(lista_inicio) == 0 or len(lista_final) == 0:
                continue
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
    return diccionario



def req_5(catalog, filter, fecha_ini, fecha_fin):
    """
    Retorna el resultado del requerimiento 5
    """
    inicio = get_time()
    hours = {}
    total_filtered = 0
    
    for i in range(0, lt.size(catalog["taxis_info"])):
        trip = lt.get_element(catalog["taxis_info"], i)
        
        pickup = trip["pickup_datetime"]
        dropoff = trip["dropoff_datetime"]
        fecha = pickup[:10]
        
        if fecha_ini <= fecha <= fecha_fin:
            total_filtered += 1

            h_initial = int(pickup[11:13])
            
            start = pickup[11:16]
            finish = dropoff[11:16]
            h1, m1 = start.split(":")
            h2, m2 = finish.split(":")
            h1, m1, h2, m2 = int(h1), int(m1), int(h2), int(m2)
            duration = (h2*60+m2) - (h1*60+m2)
            if duration < 0:
                duration += 24*60
            
            cost = float(trip["total_amount"])
            passengers = int(trip["passenger_count"])
            
            if h_initial not in hours:
                hours[h_initial] = {
                    "count": 0, "sum_cost":0, "sum_dur": 0, "sum_pass": 0, "max_cost":cost,
                    "min_cost": cost                    
                }
            hours[h_initial]["count"] += 1
            hours[h_initial]["sum_cost"] += cost
            hours[h_initial]["sum_dur"] += duration
            hours[h_initial]["sum_pass"] += passengers
            
            if cost > hours[h_initial]["max_cost"]:
                hours[h_initial]["max_cost"] = cost
            if cost < hours[h_initial]["min_cost"]:
                hours[h_initial]["min_cost"] = cost
    
    chosed_h = None
    chosed_prom = None
    
    for h_initial in hours:
        prom = hours[h_initial]["sum_cost"] / hours[h_initial]["count"]
        if chosed_h is None:
            chosed_h = h_initial
            chosed_prom = prom
        else:
            if (filter == "MAYOR" and prom > chosed_prom) or (filter == "MENOR" and prom < chosed_prom):
                chosed_h = h_initial
                chosed_prom = prom
    
    fin = get_time()    
    
    stats = hours[chosed_h]
    count = stats["count"]
    
    return {
        "tiempo_ms": fin-inicio,
        "total_trayectos_filtrados": total_filtered,
        "franja_horaria": "["+str(chosed_h) + "-" +str(chosed_h+1) +")",
        "costo_promedio": stats["sum_cost"] / count,
        "numero_trayectos": count,
        "duracion_promedio": stats["sum_dur"] / count,
        "pasajeros_promedio": stats["sum_pass"] / count,
        "costo_mayor": stats["max_cost"],
        "costo_menor": stats["min_cost"]
    }
    
    
    
    # TODO: Modificar el requerimiento 5

def req_6(catalog, fecha_ini, fecha_fin, barrio):
    """
    Retorna el resultado del requerimiento 6
    """
    tiempo_inicial = get_time()
    diccionario = {
        "tiempo_ejecucion" : 0,
        "numero_viajes_totales":0,
        "distancia_promedio" : 0,
        "tiempo_promedio" : 0,
        "nombre_barrio_final": 0,
        "medios_de_pago" : {}
    }
    barrios_filtrados = barrios(catalog)
    diccionario2 = {
        
    }
    
    for i in catalog["taxis_info"]["elements"]:
        lista_inicio = []
        lista_final = []
        fecha_inicial = i["pickup_datetime"]
        fecha_inicial = fecha_inicial[:10]
        if fecha_ini <= fecha_inicial <= fecha_fin:
            diccionario["numero_viajes_totales"] +=1
            diccionario["distancia_promedio"] += float(i["trip_distance"].replace(",", "."))
            tiempo = i["dropoff_datetime"]
            tiempo = tiempo[11:]
            tiempo = tiempo.split(":")
            hora, minuto, segundo = int(tiempo[0]), int(tiempo[1]), int(tiempo[2])
            minutos_totales = hora * 60 + minuto + (segundo / 60)
            diccionario["tiempo_promedio"] += minutos_totales
            latitud = float(i["pickup_latitude"].replace(",", "."))
            longitud = float(i["pickup_longitude"].replace(",", "."))
            if barrios_filtrados["Manhattan"]["elements"][0]["west"] <= longitud <= barrios_filtrados["Manhattan"]["elements"][0]["east"] and barrios_filtrados["Manhattan"]["elements"][0]["south"] <= latitud <= barrios_filtrados["Manhattan"]["elements"][0]["north"]:
                for each in barrios_filtrados["Manhattan"]["elements"][1]["elements"]:
                    latitud_barrio = float(each["latitude"].replace(",", "."))
                    longitud_barrio = float(each["longitude"].replace(",", "."))
                    latitud_llegada = float(i["dropoff_latitude"].replace(",", "."))
                    longitud_llegada = float(i["dropoff_longitude"].replace(",", "."))
                    distancia = harvesine_miles(latitud, longitud, latitud_barrio, longitud_barrio)
                    lista_inicio.append((each["neighborhood"], distancia))
                    ditancia_llegada = harvesine_miles(latitud_llegada, longitud_llegada, latitud_barrio, longitud_barrio)
                    lista_final.append((each["neighborhood"], ditancia_llegada))
            elif barrios_filtrados["Brooklyn"]["elements"][0]["west"] <= longitud <= barrios_filtrados["Brooklyn"]["elements"][0]["east"] and barrios_filtrados["Brooklyn"]["elements"][0]["south"] <= latitud <= barrios_filtrados["Brooklyn"]["elements"][0]["north"]:
                for each in barrios_filtrados["Brooklyn"]["elements"][1]["elements"]:
                    latitud_barrio = float(each["latitude"].replace(",", "."))
                    longitud_barrio = float(each["longitude"].replace(",", "."))
                    latitud_llegada = float(i["dropoff_latitude"].replace(",", "."))
                    longitud_llegada = float(i["dropoff_longitude"].replace(",", "."))
                    distancia = harvesine_miles(latitud, longitud, latitud_barrio, longitud_barrio)
                    lista_inicio.append((each["neighborhood"], distancia))
                    ditancia_llegada = harvesine_miles(latitud_llegada, longitud_llegada, latitud_barrio, longitud_barrio)
                    lista_final.append((each["neighborhood"], ditancia_llegada))
            elif barrios_filtrados["Queens"]["elements"][0]["west"] <= longitud <= barrios_filtrados["Queens"]["elements"][0]["east"] and barrios_filtrados["Queens"]["elements"][0]["south"] <= latitud <= barrios_filtrados["Queens"]["elements"][0]["north"]:
                for each in barrios_filtrados["Queens"]["elements"][1]["elements"]:
                    latitud_barrio = float(each["latitude"].replace(",", "."))
                    longitud_barrio = float(each["longitude"].replace(",", "."))
                    latitud_llegada = float(i["dropoff_latitude"].replace(",", "."))
                    longitud_llegada = float(i["dropoff_longitude"].replace(",", "."))
                    distancia = harvesine_miles(latitud, longitud, latitud_barrio, longitud_barrio)
                    lista_inicio.append((each["neighborhood"], distancia))
                    ditancia_llegada = harvesine_miles(latitud_llegada, longitud_llegada, latitud_barrio, longitud_barrio)
                    lista_final.append((each["neighborhood"], ditancia_llegada))
            elif barrios_filtrados["Bronx"]["elements"][0]["west"] <= longitud <= barrios_filtrados["Bronx"]["elements"][0]["east"] and barrios_filtrados["Bronx"]["elements"][0]["south"] <= latitud <= barrios_filtrados["Bronx"]["elements"][0]["north"]:
                for each in barrios_filtrados["Bronx"]["elements"][1]["elements"]:
                    latitud_barrio = float(each["latitude"].replace(",", "."))
                    longitud_barrio = float(each["longitude"].replace(",", "."))
                    latitud_llegada = float(i["dropoff_latitude"].replace(",", "."))
                    longitud_llegada = float(i["dropoff_longitude"].replace(",", "."))
                    distancia = harvesine_miles(latitud, longitud, latitud_barrio, longitud_barrio)
                    lista_inicio.append((each["neighborhood"], distancia))
                    ditancia_llegada = harvesine_miles(latitud_llegada, longitud_llegada, latitud_barrio, longitud_barrio)
                    lista_final.append((each["neighborhood"], ditancia_llegada))
            elif barrios_filtrados["Staten Island"]["elements"][0]["west"] <= longitud <= barrios_filtrados["Staten Island"]["elements"][0]["east"] and barrios_filtrados["Staten Island"]["elements"][0]["south"] <= latitud <= barrios_filtrados["Staten Island"]["elements"][0]["north"]:
                for each in barrios_filtrados["Staten Island"]["elements"][1]["elements"]:
                    latitud_barrio = float(each["latitude"].replace(",", "."))
                    longitud_barrio = float(each["longitude"].replace(",", "."))
                    latitud_llegada = float(i["dropoff_latitude"].replace(",", "."))
                    longitud_llegada = float(i["dropoff_longitude"].replace(",", "."))
                    distancia = harvesine_miles(latitud, longitud, latitud_barrio, longitud_barrio)
                    lista_inicio.append((each["neighborhood"], distancia))
                    ditancia_llegada = harvesine_miles(latitud_llegada, longitud_llegada, latitud_barrio, longitud_barrio)
                    lista_final.append((each["neighborhood"], ditancia_llegada))
            if len(lista_inicio) == 0 or len(lista_final) == 0:
                continue
            menor = lista_inicio[0]     
            p = 1
            while p < len(lista_inicio):
                if lista_inicio[p][1] < menor[1]:
                    menor = lista_inicio[p]
                p += 1
            barrio_inicio = menor[0]
            menor_1 = lista_final[0]
            if barrio_inicio == barrio:
                menor_1 = lista_final[0]
                j = 1
                while j < len(lista_final):
                    if lista_final[j][1] < menor_1[1]:
                        menor_1 = lista_final[j]
                    j += 1
            barrio_final = menor_1[0]
            if barrio_final in diccionario2:
                diccionario2[barrio_final]["suma"] += 1
                    
            else:
                diccionario2[barrio_final] ={
                    "suma": 1,
                    "barrio" : barrio_final
                }
            
            llave = i["payment_type"]
            if llave in diccionario["medios_de_pago"]:
                tiempo = i["dropoff_datetime"]
                tiempo = tiempo[11:]
                tiempo = tiempo.split(":")
                hora, minuto, segundo = int(tiempo[0]), int(tiempo[1]), int(tiempo[2])
                minutos_totales = hora * 60 + minuto + (segundo / 60)
                diccionario["medios_de_pago"][llave]["cantidad_trayectos"] += 1
                diccionario["medios_de_pago"][llave]["precio_promedio"] += float(i["total_amount"])
                diccionario["medios_de_pago"][llave]["tiempo_promedio"] += minutos_totales
            else:
                tiempo = i["dropoff_datetime"]
                tiempo = tiempo[11:]
                tiempo = tiempo.split(":")
                hora, minuto, segundo = int(tiempo[0]), int(tiempo[1]), int(tiempo[2])
                minutos_totales = hora * 60 + minuto + (segundo / 60)
                diccionario["medios_de_pago"][llave] = {
                        "cantidad_trayectos" : 1,
                        "precio_promedio": float(i["total_amount"]),
                        "tiempo_promedio" : minutos_totales,
                        "medio": llave 
                    }
                
    #Arregla la busqueda del barrio con mayor suma 
    frecuente = 0 
    if not diccionario2:
        diccionario["nombre_barrio_final"] = None
    else:
        frecuente = None  # guardará el dict {"suma": X, "barrio": "Nombre"}
        for _, data in diccionario2.items():
            if frecuente is None or data["suma"] > frecuente["suma"]:
                frecuente = data
    diccionario["nombre_barrio_final"] = frecuente["barrio"]
    
    diccionario["distancia_promedio"] = diccionario["distancia_promedio"] / diccionario["numero_viajes_totales"]
    diccionario["tiempo_promedio"] = diccionario["tiempo_promedio"] / diccionario["numero_viajes_totales"]
    mayor_frecuencia = None
    max_frec = 0
    mas_recaudado = None
    max_recaudo = 0
    for i in diccionario["medios_de_pago"]:
        if diccionario["medios_de_pago"][i]["cantidad_trayectos"] > max_frec:
            max_frec = diccionario["medios_de_pago"][i]["cantidad_trayectos"]
            mayor_frecuencia = (i, max_frec)
        if diccionario["medios_de_pago"][i]["precio_promedio"] > max_recaudo:
            max_recaudo = diccionario["medios_de_pago"][i]["precio_promedio"]
            mas_recaudado = (i, max_recaudo)
    diccionario["medio_pago_mas_frecuente"] = mayor_frecuencia
    diccionario["medio_pago_mas_recaudado"] = mas_recaudado
    del diccionario["medios_de_pago"]
    tiempo_final = get_time()
    tiempo_ejecucion = delta_time(tiempo_inicial,tiempo_final)
    diccionario["tiempo_ejecucion"] = tiempo_ejecucion
    return diccionario 


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


