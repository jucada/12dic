import datetime as dt

ahora = dt.datetime.now()

print(f"Estamos {ahora.day} y el mes {ahora.month} del {ahora.year}.")
print(f"Hora: {ahora.hour} --- Minutos: {ahora.minute} --- Segundos: {ahora.second}")