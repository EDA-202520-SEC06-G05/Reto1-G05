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
    pass


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
        taxi["extra"], taxi["mta_tax"],
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
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass
    


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog, filtro, fecha_inicio, fecha_final):

    """
    Retorna el resultado del requerimiento 4
    """
    tiempo_inicial = get_time()
    contador = {
        "tiempo" : 0,
        "filtro" : 0,
        "trayectos_totales" : 0,
        "barrios": {}
    }
    
    

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
