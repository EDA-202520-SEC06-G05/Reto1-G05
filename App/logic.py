import time
import csv
import os
from DataStructures.List import array_list as lt


data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-1'

def new_logic(data_structure):
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    data_structure = lt
    catalog = {"Neighborhoods": None,
               "taxis_info": None}
    catalog["Neighborhoods"] = data_structure.new_list()
    catalog["taxis_info"] = data_structure.new_list()
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
    
    taxi_file = data_dir + "/taxis-small.csv"
    input_file = csv.DictReader(open(taxi_file, encoding="utf-8"), delimiter=",")
    for taxi in input_file:
        add_taxi(catalog, taxi)
        trip_total += 1
        
        pick_up = taxi["pickup_datetime"]
        dropoff = taxi["dropoff_datetime"]
        start = pick_up[11:16]
        finish = dropoff[11:16]
        
        h1str, m1str = start.split(":")
        h2str, m2str = finish.split(":")
        
        h1, m1 = int(h1str), int(m1str)
        h2, m2 = int(h2str), int(h2str)
        
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
        taxi["extra"], taxi["mta_tax"],
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

    for viaje in catalog["taxis_info"]:
        if viaje["passenger_count"]!="" and int(float(viaje["passenger_count"]))== pasajeros:
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

def req_2(catalog):
    
    filtro = "CREDIT_CARD"
    contador = 0
    duration = 0
    total_costs = 0
    distancia = 0
    peajes = 0
    pasajeros = {}
    propina = 0  
    fechas = {}
    
    for each in catalog["taxis_info"]:        
        if each["payment_method"] == filtro:
            contador += 1
            
            pickup = each["pickup_datetime"]
            dropoff = each["dropoff_datetime"]
            start = pickup[11:16]
            finish = dropoff[11:16]
            h1str , m1str = start.split(":")
            h2str, m2str = finish.split(":")
            h1 , m1 = int(h1str), int(m1str)
            h2, m2 = int(h2str), int(m2str)
            duration_sum = (h2 *60 + m2) - (h1 *60 + m1)
            duration += duration_sum
            
            total_costs += float(each["total_amount"]) 
            distancia += float(each["trip_distance"]) 
            peajes += float(each["tolls_amount"])
            propina += float(each["tip_amount"])
            
            num_pasajeros = int(each["passenger_count"])
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
    
    for taxi in catalog["taxis_info"]:
        lista = []
        if (float(taxi["total_amount"])) > float(valor_menor) and (float(taxi["total_amount"])) < float(valor_mayor):
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



def req_4(catalog, fecha_inicio, fecha_final, filtro3):
    """
    Retorna el resultado del requerimiento 4
    """
    catologo = {
        "filtro": 0,
        "numero_total_viajes": 0,
        "barrios_frecuentes": {},
    }
    barrios = {
        
    }
    for i in range(1, lt.size(catalog["Neighborhoods"])+1):
        linea = lt.get_element(catalog["Neighborhoods"], i)
        if linea["borough"] in barrios:
            valor= {str(linea["neighborhood"]): linea["neighborhood"],
                                         str(linea["latitude"]): linea["latitude"],
                                         str(linea["longitude"]) : linea["longitude"]
                                         }
            barrios[linea["borough"]] = lt.add_last(barrios[linea["borough"]], valor)
        else:
            barrios[linea["borough"]] = lt.new_list()
            valor= {str(linea["neighborhood"]): linea["neighborhood"],
                                         str(linea["latitude"]): linea["latitude"],
                                         str(linea["longitude"]) : linea["longitude"]
                                         }
            barrios[linea["borough"]] = lt.add_last(barrios[linea["borough"]], valor)
    
    for taxi in catalog["taxis_info"]:
        fecha = taxi["pickup_datetime"]
        fecha = fecha[:11]
        if fecha < fecha_final or fecha > fecha_inicio:
            catologo["numero_total_viajes"] +=1
            
            
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


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


