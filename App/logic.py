import time
import csv
import os
from DataStructures.List import array_list as lt

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-1'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {
        "Neighborhoods": None,
        "taxis_info": None}
    
    catalog["Neighborhoods"] = lt.new_list()
    catalog["taxis_info"] = lt.new_list()
    return catalog
    #TODO: Llama a las funciónes de creación de las estructuras de datos


# Funciones para la carga de datos

def load_data(catalog, filename):
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
    input_file = csv.DictReader(open(neigh_file, encoding="utf-8"))
    for neigh in input_file:
        add_neigh(catalog, neigh)
    return neigh_size(catalog)

def load_taxis(catalog):
    taxi_file = data_dir + "/taxis-small.csv"
    input_file = csv.DictReader(open(taxi_file, encoding="utf-8"))
    for taxi in input_file:
        add_taxi(catalog, taxi)
    return taxi_size(catalog)

def add_neigh(catalog, neigh):
    n = new_neigh(neigh["borough"], neigh["neighborhood"], neigh["latitude"], neigh["longitude"])
    lt.add_last(catalog["neighboorhoods"], n)
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
    neigh = {
        "borough":borough, 
        "neighborhood":neighbor, 
        "latitude":lat, 
        "longitude": longi}
    return neigh

def new_taxi_info(pickup, dropoff, passenger_count, trip_dist, 
                  pickup_longitude, pickup_latitude, rate_code, drop_long, drop_lat, payment, fare, extra, mta_tax, tip, tolls, improve, total)
    
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


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


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
        if float(taxi["total_amount"]) > 5 and float(taxi):
            contador["numero_viajes"] +=1
            lista = [taxi["pickup_datetime"], taxi["dropoff_datetime"]]
            hora, minuto , segundo = lista[0][10:].split(":")
            if int(segundo) % 60 == 0:
                segundo = 1
            else:
                segundo = 0
            hora_inicial = int(hora) *60 + int(minuto) + int (segundo)
            
            hora_final, minuto_final, segundo_final = lista[1][10:].split(":")
            if int(segundo_final) % 60 == 0:
                segundo_final = 1
            else:
                segundo_final = 0
                
            hora_termino = int(hora_final) *60 + int(minuto_final) + int (segundo_final)
            tiempo_viaje_total = hora_termino - hora_inicial
            contador["tiempo_promedio"] += tiempo_viaje_total
            
            if taxi["passenger_count"] in contador["cantidad_pasajeros_frecuente"]:
                contador["cantidad_pasajeros_frecuente"][taxi["passenger_count"]] += 1
            else:
                contador["cantidad_pasajeros_frecuente"][taxi["passenger_count"]] = 1
            
            if lista[:10] in contador["fecha_promedio"]:
                contador["fecha_promedio"] += 1
            else:
                contador["cantidad_pasajeros"][lista[:10]] = 1
                
            contador["precio_promedio_usd"] += float(taxi["total_amount"])
            contador["disatancia_total_promedio"] += float(taxi["trip_distance"])
            contador["precio_peaje_promedio"] += float(taxi["tolls_amount"])
            contador["cantidad_propinas_promedio"] += float(taxi["tip_amount"])
            
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
        if contador["cantidad_pasajeros_frecuentes"][cantidad] == cantidad_pasajeros:
            contador["cantidad_pasajeros_frecuente"] = (cantidad, cantidad_pasajeros)
            break
    time_end = get_time()
    time_total = delta_time(time_start, time_end)
    contador["tiempo_ejecucion"] = time_total
    
    return contador 
    
    
    
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
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


