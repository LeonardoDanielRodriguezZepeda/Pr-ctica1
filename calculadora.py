
print("¿Cúal operación quieres hacer?")      #Instruccion que imprime un mensaje al usuario
ecuacion=input()                             #Instruccion que guarda el dato que el usuario selecciona
a =int(input("Dame el primer numero"))       #Instruccion que pide el dato, lo asigna a una variable y lo convierte a entero
b= int(input("Dame el segundo numeros"))     #Instruccion que pide el dato, lo asigna a una variable y lo convierte a entero

if ecuacion == "suma":                       #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
     c=a+b                                   #Instruccion de operacion suma

if ecuacion == "resta":                      #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
     c=a-b                                   #Instruccion de operacion resta

if ecuacion == "multiplicacion":             #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
      c=a*b                                  #Instruccion de operacion multiplicacion
    
if ecuacion == "division":                   #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
       c=a/b                                 #Instruccion de operacion division


print("El resultado de tu operacion es:",c)  #Imprime el resultado al usuario

