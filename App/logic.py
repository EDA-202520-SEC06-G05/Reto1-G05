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
    n = new_neigh(neigh["borough"],
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
    duracion=0
    costo_total=0
    distancia=0
    peajes=0
    propina=0
    metodos_pago={}
    fechas={}

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
            duracion += duracion_sum

            costo_total+= float(viaje["total_amount"])
            distancia+= float(viaje["trip_distance"])
            peajes+= float(viaje["tolls_amount"])
            propina+= float(viaje["tip_amount"])

            metodo_pago=viaje["payment_type"]
            if metodo_pago in metodos_pago:
                metodos_pago[metodo_pago]+=1
            else:
                metodos_pago[metodo_pago]=1

            fecha=pickup[0:10] 
            if fecha in fechas:
                fechas[fecha]+=1
            else:
                fechas[fecha]=1
    if contador>0:
        duracion=duracion/contador
        costo_total=costo_total/contador
        distancia=distancia/contador
        peajes=peajes/contador
        propina=propina/contador
    else:
        duracion=costo_total=distancia=peajes=propina=0
    metodo_frec=None
    cantidad_max=-1
    for metodo in metodos_pago:
        cantidad =metodos_pago[metodo]
        if cantidad >cantidad_max:
            cantidad_max=cantidad
            metodo_frec=str(metodo)+" - "+str(cantidad)
    fecha_frec=None
    max_fecha=-1
    for fecha in fechas:
        cantidad=fechas[fecha]
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



def req_3(catalog):
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


def req_4(catalog, filtro, fecha_inicio, fecha_final):

    """
    Retorna el resultado del requerimiento 4
    """
    tiempo_inicio = get_time()
    catologo = {
        "tiempo_ejecucion": 0,
        "filtro_seleccionado": filtro,
        "numero_viajes_total": 0,
        "barrios_filtrados" : {}
    }
    
    barrios = lt.new_list
    for each in catalog["Neighborhoods"]:
        sub_barrios = {
            "neighborhood": each["neighborhood"],
            "latitude": each["latitude"],
            "longitude": each["longitude"]
        }
        lt.add_last(barrios, sub_barrios)
    
    for each in catalog["taxis_info"]:
        inicial = each["pickup_datetime"]
        fecha_inicial = inicial[:10]
        if fecha_ini <= fecha_inicial <= fecha_fin:
            catologo["numero_viajes_total"] += 1
            lt1 = float(each["pickup_latitude"])
            lo1 = float(each["pickup_longitude"])
            lt2 = float(each["dropoff_latitude"])
            lo2 = float(each["dropoff_longitude"])
            barrio_inicial = None
            barrio_final = None
            contador = 0
            mayor_inidice_inical = 0
            mayor_indice_final = 0
            while contador < lt.size(barrios):
                longitud_barrio = barrios[contador]["longitud"]
                latitud_barrio = barrios[contador]["latitud"]
                distancia_inicial = harvesine_miles(lt1, lo1, float(latitud_barrio), float(longitud_barrio))
                distancia_final = harvesine_miles(lt2, lo2, float(latitud_barrio), float(longitud_barrio))
                if distancia_inicial <= barrio_inicial:
                    barrio_inicial = distancia_inicial
                    mayor_indice_iniical = contador
                if distancia_final <= barrio_final:
                    barrio_final = distancia_final
                    mayor_indice_final = contador
                contador += 1
            barrio_inicial = barrios[mayor_inidice_inical]["neighborhood"]
            barrio_final = barrios[mayor_indice_final]["neighborhood"]
            llave = (barrio_inicial + "" + barrio_final)
            if barrio_inicial == barrio_final:
                None
            elif llave in catologo["barrios_filtrados"]:
                catologo["barrios_filtrados"][llave]["frecuencia"] += 1
                catologo["barrios_filtrados"][llave]["distancia_promedio"] += each["trip_distance"]
                catologo["barrios_filtrados"][llave]["costo_promedio"] += each["total_amount"]
                lista = [each["pickup_datetime"], each["dropoff_datetime"]]
                hora, minuto , segundo = lista[0][11:].split(":")
                hora_inicial = int(hora) *60 + int(minuto) + (int (segundo) / 60)
                hora_final, minuto_final, segundo_final = lista[1][11:].split(":")
                hora_termino = int(hora_final) *60 + int(minuto_final) + (int (segundo_final)/ 60)
                if lista[0][:10] != lista[1][:10]:
                    hora_termino += 24*60
                tiempo_viaje_total = hora_termino - hora_inicial
                catologo["barrios_filtrados"][llave]["tiempo_duracion_promedio"] += tiempo_viaje_total
            else:
                lista = [each["pickup_datetime"], each["dropoff_datetime"]]
                hora, minuto , segundo = lista[0][11:].split(":")
                hora_inicial = int(hora) *60 + int(minuto) + (int (segundo) / 60)
                hora_final, minuto_final, segundo_final = lista[1][11:].split(":")
                hora_termino = int(hora_final) *60 + int(minuto_final) + (int (segundo_final)/ 60)
                if lista[0][:10] != lista[1][:10]:
                    hora_termino += 24*60
                tiempo_viaje_total = hora_termino - hora_inicial                
                
                catologo["barrios_filtrados"][llave] = {
                                                        "frecuencia":0,
                                                        "nombre_barrio_inicial": barrio_inicial,
                                                        "nombre_barrio_final": barrio_final,
                                                        "distancia_promedio" : each["trip_distance"],
                                                        "costo_promedio": each["total_amount"],
                                                        "tiempo_duracion_promedio": tiempo_viaje_total
                                                        } 
            
            
        #Falta sacar los promedios de los datos
        #Luego dependiendo del filtro damos por max o min en un ciclo while las iteracciones necesarias en barrios filtrados 
        # Return el catologo
    
            
            
    
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog, fecha_ini , fecha_fin):
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
    tiempo_inicio = get_time()
    catalogo = {
        "tiempo_ejecucion":0,
        "numero_viajes_total":0,
        "distancia_total_promedio":0,
        "tiempo_duracion_promedio":0,
        "nombre_barrio_final_mas_frecuente":{},
        "medios_de_pago": {}
    }
    
    barrios = lt.new_list
    for each in catalog["Neighborhoods"]:
        sub_barrios = {
            "neighborhood": each["neighborhood"],
            "latitude": each["latitude"],
            "longitude": each["longitude"]
        }
        lt.add_last(barrios, sub_barrios)
        
    for each in catalog["taxis_info"]:
        inicial = each["pickup_datetime"]
        fecha_inicial = inicial[:10]
        if fecha_ini <= fecha_inicial <= fecha_fin:
            catalogo["numero_viajes_total"] += 1
            lt1 = float(each["pickup_latitude"])
            lo1 = float(each["pickup_longitude"])
            lt2 = float(each["dropoff_latitude"])
            lo2 = float(each["dropoff_longitude"])
            barrio_inicial = None
            barrio_final = None
            contador = 0
            mayor_inidice_inical = 0
            mayor_indice_final = 0
            while contador < lt.size(barrios):
                longitud_barrio = barrios[contador]["longitud"]
                latitud_barrio = barrios[contador]["latitud"]
                distancia_inicial = harvesine_miles(lt1, lo1, float(latitud_barrio), float(longitud_barrio))
                distancia_final = harvesine_miles(lt2, lo2, float(latitud_barrio), float(longitud_barrio))
                if distancia_inicial <= barrio_inicial:
                    barrio_inicial = distancia_inicial
                    mayor_indice_iniical = contador
                if distancia_final <= barrio_final:
                    barrio_final = distancia_final
                    mayor_indice_final = contador
                contador += 1
            barrio_inicial = barrios[mayor_inidice_inical]["neighborhood"]
            if barrio_inicial != barrio:
                None
            else:
                barrio_final = barrios[mayor_indice_final]["neighborhood"]
                if barrio_final in catalogo["nombre_barrio_final_mas_frecuente"]:
                    catalogo["nombre_barrio_final_mas_frecuente"][barrio_final] += 1
                else:
                    catalogo["nombre_barrio_final_mas_frecuente"][barrio_final] = 1
                if each["payment_type"] in catalogo["medios_de_pago"]:
                    catalogo["medios_de_pago"][each["payment_type"]] += 1
                    lista = [each["pickup_datetime"], each["dropoff_datetime"]]
                    hora, minuto , segundo = lista[0][11:].split(":")
                    hora_inicial = int(hora) *60 + int(minuto) + (int (segundo) / 60)
                    hora_final, minuto_final, segundo_final = lista[1][11:].split(":")
                    hora_termino = int(hora_final) *60 + int(minuto_final) + (int (segundo_final)/ 60)
                    if lista[0][:10] != lista[1][:10]:
                        hora_termino += 24*60
                    tiempo_viaje_total = hora_termino - hora_inicial  
                    catalogo["medios_de_pago"][each["payment_type"]] = catalogo["medios_de_pago"][each["payment_type"]] + 1
                    catalogo["medios_de_pago"][each["payment_type"]]["precio_total"] += each["total_amount"]
                    catalogo["medios_de_pago"][each["payment_type"]]["tiempo_promedio"] += tiempo_viaje_total
                else:
                    lista = [each["pickup_datetime"], each["dropoff_datetime"]]
                    hora, minuto , segundo = lista[0][11:].split(":")
                    hora_inicial = int(hora) *60 + int(minuto) + (int (segundo) / 60)
                    hora_final, minuto_final, segundo_final = lista[1][11:].split(":")
                    hora_termino = int(hora_final) *60 + int(minuto_final) + (int (segundo_final)/ 60)
                    if lista[0][:10] != lista[1][:10]:
                        hora_termino += 24*60
                    tiempo_viaje_total = hora_termino - hora_inicial  
                    
                    catalogo["medios_de_pago"][each["payment_type"]] = {"tipo_de_pago": each["payment_type"], "cantidad_trayectos": 1,"precio_total": each["total_amount"], "mas_usado": False, "mayor_recaudacion": False, "tiempo_promedio": tiempo_viaje_total}
                    
            #Ingresar los promedios de los valores de cada uno 
            #Sacar cual es el mayor uso de pago y el que mas recaudo
            #Ingresarlo al diccionario y devolvelo al final 
            
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


