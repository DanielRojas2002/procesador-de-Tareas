from plyer import notification
import time
import datetime


def notificacion(segundos,separador):
    minutos=segundos*60
    time.sleep(minutos)
    
    
    notification.notify(
    title="NOTIFICACION",
    message = "Metete al script para renovarlo :) ",
    timeout=10,
    )
    notification.notify(
    title="NOTIFICACION",
    message = "¿Ya Hiciste tu tarea? :( ",
    timeout=15,
    )
    
    print("1=SI\n2=NO")
    notifi=int(input("Quieres seguir esperando la notificacion : "))
    print(separador)
    
    if notifi==2:
        notification.notify(
        title="NOTIFICACION",
        message = "Espero que tu tarea , ya es este hecha Adioss... :) ",
        timeout=15,
        )
        
    while notifi==1:
        time.sleep(minutos)
        notification.notify(
        title="NOTIFICACION",
        message = "¿Ya Hiciste tu tarea ?:( ",
        timeout=15,
        )
        
        notification.notify(
        title="NOTIFICACION",
        message = "Metete al script para renovarlo :) ",
        timeout=10,
        )
        
        print("1=SI\n2=NO")
        notifi=int(input("Quieres seguir esperando la notificacion : "))
        print(separador)
        
        if notifi==2:
            notification.notify(
            title="NOTIFICACION",
            message = "Espero que tu tarea , ya es este hecha Adioss... :) ",
            timeout=15,
            )


fecha_actual = datetime.date.today()
opcion=1
separador=("*"*40)
contador=1
while opcion==1:
    print(separador + "BIENVENIDO AL REGISTRO DE TAREAS : "+ separador)
    archivoA=open("./archivos/tarea.txt" , 'a')
    archivoA.write(f"TAREAS DEL {fecha_actual} :)" +"\n" )
    cuantas=int(input("Cuantas tareas vas a registrar : "))
    for tarea in range(cuantas):
        tarea=(input("Dime la tarea : "))
        contador2=str(contador)
        archivoA.write("TAREA " + contador2+" "+ tarea+  "\n" )
        contador=contador+1
    archivoA.write("///////////////////////////////////////////////////////////////" +"\n" )
    print(separador)
    print("Ya estan registradas las tareas en el documento .txt")
    print("Porfavor no cierres este programa :)")
    print(separador)
    archivoA.close()
    
    segundos=int(input("Cuantos minutos quieres que pasen para que te mande una notificacion : "))
    print(separador)
    notificacion(segundos,separador)
    opcion=2