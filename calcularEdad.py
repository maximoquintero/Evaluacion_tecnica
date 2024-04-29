# - Algoritmo de Cálculo de edad exacta (año, mes, semana, día, hora). (Básico).
#• Realizar un algoritmo que calcula la edad de una persona.
# El usuario debe ingresar su año de nacimiento, día y hora.

from datetime import datetime

# formato que utiliza: Año, Mes, Día, Hora, Minutos, Segundos, Milisegundos.

def calcularEdad(fecha):
    fechaActual = datetime.now()
    fechaRevision = []
    
    fechaRevision.append(fechaActual.year - fecha.year)
    fechaRevision.append(fechaActual.month - fecha.month)
    fechaRevision.append(fechaActual.day - fecha.day)
    fechaRevision.append(fechaActual.hour - fecha.hour)
    fechaRevision.append(fechaActual.minute - fecha.minute)

    for i in range(len(fechaRevision)):
        if fechaRevision[i] < 0:
            fechaRevision[i] = abs(fechaRevision[i])

    año, mes, dia, hora, minuto = map(str, fechaRevision)
    
    edadCalculada = "Tienes " + año + " años, " + mes + " meses, " + dia + " dias, " + hora + " horas, " + minuto + " minutos."
    print(edadCalculada)

fecha = datetime(1969, 9, 13, 12, 59)
calcularEdad(fecha)
