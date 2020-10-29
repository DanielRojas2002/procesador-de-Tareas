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