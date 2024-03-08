# Creación del algoritmo de SJF en Python

# Creación de las variables con las listas de procesos.
# [Nombre del proceso, Arrival Time, Burst Time].

process = [["P1",2,8],["P2",4,3],["P3",5,1],["P4",7,3],["P5",13,12],["P6",9,12],["P7",15,4],["P8",18,7],["P9",22,1]] #Lista con todos los procesos y sus respectivos tiempos,

# sorted(Iterable, key= lambda subLista : (subLista[Indice2], subLista[Indice1]) )
orderedProccess = sorted(process, key=lambda x: (x[2], x[1])) #Creamos una función lambda para ordenar la lista de los procesos por medio del indice 2 y luego del indice 1.
timeLine = [] #Ponemos por defecto al proceso 0 en primero porque asi lo maneja el algoritmo SJF.
totalTime = 0 #El tiempo que se tardara en ejecutar los procesos

orderedProccess.insert(0,["P0",0,9]) #Insertamos el proceso 0 al inicio de la cadena de procesos a realizar.
for procedure in orderedProccess: #Recorremos la lista para simplemente agarrar el primer valor de cada.
    timeLine.append(procedure[0]) #Añadimos el nombre del proceso a una lista nueva.

for procedure in orderedProccess: #Recorremos la lista para simplemente agarrar el primer valor de cada.
    totalTime += procedure[2] #Hacemos la suma del tiempo total de ejecución. 

print("-----Orden de procesos-----") #Texto.
print(timeLine) #Mostramos la cadena de procesos en el orden correcto.
print(f"Tiempo total de ejecución: {totalTime}" ) #Imprimimos en consola la cantidad de tiempo que se tardara en ejecutarse los procesos