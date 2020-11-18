# -*- coding: UTF-8 -*-
# 👆 Sin lo de arriba no se puede poner emojis
import pytz
import datetime
import json

# Mi script asume la hora de tu PC
date_to_convert = "2020-11-17 21:00:00"
# Recuerda: Es la hora de tu PC

date_to_convert = datetime.datetime.strptime(
    date_to_convert, "%Y-%m-%d %H:%M:%S")

print(date_to_convert)
print("Generando bloque de banderas:")
print("")

# En orden de tamaño de mercado/prioridad
# Loading the zones from the JSON file

with open('zones.json') as zones_file:
    zones = json.load(zones_file)

# Inicializamos el diccionario
times = {"00pm": "X"}

# If you need Brazil:
# you can add it to the zones.json file
# ["🇧🇷","America/Sao_Paulo"]

# Los timezones no están derivados de países, sino de ciudades.
# Aunque la prioridad es por país

for country in zones:
    dtc = date_to_convert.astimezone(pytz.timezone(country[1]))
    if country[1] == "Europe/Madrid":
        # Imprime la hora en formato de 24 horas y una "H" al final
        dtc = dtc.strftime("%-HH")
    else:
        # Imprime la hora en formato de 12 horas PM/AM
        dtc = dtc.strftime("%-I%p")
    try:
        times[dtc] = times[dtc] + country[0]
    except KeyError:
        times[dtc] = country[0]

    # Si el país es USA en Pacific, agregar el "PT" frente a bandera de US
    if country[1] == "US/Pacific":
        times[dtc] = times[dtc] + " PT"

    times[dtc] = times[dtc] + " "

for t, c in times.items():
    if c != "X":
        print(t.lower(), c.strip())
