

LISTA = ['QUEEN','PUNK','TRI','DEAD','RAPE','MURDER']                       #Declaracion de lista
TUPLA = tuple(LISTA)                                                        #Creacion de una tupla llena de los valores de la lista  
a=2                                                                         #Declaracion de variable y asignacion de valor
while a>1:                                                                  #Sentencia while usada como bucle infinito
    print(LISTA)                                                            #Imprmime los valores de la lista
    respuesta = input('La lista tiene los siguientes elementos:\nDesea modificarla?\n')         #Instruccion que pide el dato, lo asigna a una variable y lo convierte a entero
    if (respuesta == 'si') or (respuesta  == 'Si'):        #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
        cambio = input('Presiona 1 para remplazar dato, presiona 2 para agregar dato\n')        #Instruccion que pide el dato, lo asigna a una variable y lo convierte a entero
        if cambio=='1':                                    #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
            posicion = input('Dame la posicion que deseas remplazar:\n')                        #Instruccion que pide el dato, lo asigna a una variable y lo convierte a entero
            dato = input('Dame el dato que deseas insertar:\n')                                 #Instruccion que pide el dato, lo asigna a una variable y lo convierte a entero
            LISTA[int(posicion)] = dato                    #Convierte el dato dentro del corchete a entero, inserta el valor del dato en ese espacio
        if cambio == '2':                                  #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
            dato = input('Dame el dato que quieres agregar:\n')                                 #Instruccion que pide el dato, lo asigna a una variable y lo convierte a entero
            LISTA.append(dato)                             #Agrega el dato al final de la lista
    buscar = input('Que deseas hacer:\n1-Buscar elemento en la lista\n2-Saber si existe el elemento en la lino\n3-Eliminar elemento\n4-Invertir el orden de elementos\n5-Separar cadena de frases\n6-Salir\n') #Instruccion que pide el dato, lo asigna a una variable y lo convierte a entero
    if buscar == '1':                                      #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
        busqueda = input('Dame el dato que deseas buscar:\n') #Instruccion que pide el dato, lo asigna a una variable y lo convierte a entero
        print(LISTA.index(busqueda))                         #Imprime el valor resultante de la busqueda en la lista, busca la variable que es el argumento de index
        print(LISTA,'\n')                                  #Imprmime los valores de la lista
        print(TUPLA,'\n')                                  #Imprmime los valores de la tupla

    if buscar == '2':                                      #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
     busqueda = input('Dame el dato que deseas saber si existe:\n')      #Instruccion que pide el dato, lo asigna a una variable y lo convierte a entero
     busqueda in LISTA                                   #Solo verifica si la variable se encuentra en la lista
     print(LISTA,'\n')                                   #Imprmime los valores de la lista
     print(TUPLA,'\n')                                   #Imprmime los valores de la tupla
    if buscar == '3':                                    #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
     busqueda = input('Dame el dato que deseas eliminar:\n')      #Instruccion que pide el dato, lo asigna a una variable y lo convierte a entero
     LISTA.remove( busqueda)                            #Elimina el valor de la variable de la lista
     print(LISTA,'\n')                                  #Imprmime los valores de la lista
     print(TUPLA,'\n')                                  #Imprmime los valores de la tupla
    if buscar == '4':                                   #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
        LISTA.reverse()                                 #Invierte los elementos de la lista
        print(LISTA,'\n')                              #Imprmime los valores de la lista
        print(TUPLA,'\n')                              #Imprmime los valores de la tupla
    if buscar == '5':                                  #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
     busqueda = input('Dame la frase que deseas separar:\n')      #Instruccion que pide el dato, lo asigna a una variable y lo convierte a entero
     print(busqueda.split())                           #Separa un enunciado por palabra y lo guarda en una lista
     print(LISTA,'\n')                                 #Imprmime los valores de la lista
     print(TUPLA,'\n')                                 #Imprmime los valores de la tupla
    if buscar == '6':                                  #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
         print(LISTA,'\n')                             #Imprmime los valores de la lista
         print(TUPLA,'\n')                             #Imprmime los valores de la tupla
         quit()                                        #Intruccion para salir del programa