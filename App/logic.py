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
    t = new_taxi_info(taxi["pickup_datetime"],taxi["dropoff_datetime"],taxi["passenger_count"],taxi["trip_distance"],taxi["pickup_longitude"],taxi["pickup_latitude"],
                      taxi["rate_code"],taxi["dropoff_longitude"],taxi["dropoff_latitude"], taxi["payment_type"],taxi["fare_amount"], taxi["extra"], taxi["mta_tax"],
                      taxi["tip_amount"], taxi["tolls_amount"], taxi["improvement_surcharge"],taxi["total_amount"])
    lt.add_last(catalog["taxis_info"], t)
    return catalog
    
def new_neigh(borough, neighbor, lat, longi):
    neigh = {"borough":borough, "neighborhood":neighbor, 
             "latitude":lat, "longitude": longi}
    return neigh

def new_taxi_info(pickup, dropoff, passenger_count, trip_dist, 
                  pickup_longitude, pickup_latitude, rate_code, drop_long, drop_lat, payment, fare, extra, mta_tax, tip, tolls, improve, total):
    
    taxi_info = {"pickup_datetime":pickup, "dropoff_datetime":dropoff, "passenger_count":passenger_count, "trip_distance": trip_dist, "pickup_longitude": pickup_longitude,
                 "pickup_latitude":pickup_latitude, "rate_code": rate_code, "dropoff_longitude": drop_long, "dropoff_latitude": drop_lat, "payment_type":payment, "fare_amount":fare,
                 "extra": extra, "mta_tax": mta_tax, "tip_amount": tip, "tolls_amount": tolls, "improvement_surcharge": improve, "total_amount":total}
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



def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog, filtro1, filtro2, filtro3):
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
