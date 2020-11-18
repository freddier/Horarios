# -*- coding: UTF-8 -*-
# 👆 Sin lo de arriba no se puede poner emojis
import pytz
import datetime
import click


@click.command()
@click.option('--date_to_convert', prompt='Generar banderas para la fecha, ejemplo 2020-11-17 21:00:00',
              help='La fecha debe cumplir con el formato %Y-%m-%d %H:%M:%S, ejemplo: 2020-11-17 21:00:00')
def print_flags(date_to_convert):
    print(f'Hora: {date_to_convert}')
    print("Generando bloque de banderas:\n")

    date_to_convert = parse(date_to_convert)
    if date_to_convert is None:
        print(
            "La fecha no cumple con el formato requerido: intentar $> python3 horarios.py "
            "--date_to_convert='2020-11-17 21:00:00'")
    else:
        # En orden de tamaño de mercado/prioridad
        zones = [
            ["🇲🇽", "America/Mexico_City"],
            ["🇨🇴", "America/Bogota"],
            ["🇵🇪", "America/Lima"],
            ["🇨🇱", "America/Santiago"],
            ["🇦🇷", "America/Buenos_Aires"],
            ["🇪🇸", "Europe/Madrid"],
            ["🇺🇾", "America/Montevideo"],
            ["🇪🇨", "America/Guayaquil"],
            ["🇬🇹", "America/Guatemala"],
            ["🇸🇻", "America/El_Salvador"],
            ["🇧🇴", "America/La_Paz"],
            ["🇵🇾", "America/Asuncion"],
            ["🇩🇴", "America/Santo_Domingo"],
            ["🇵🇦", "America/Panama"],
            ["🇨🇷", "America/Costa_Rica"],
            ["🇭🇳", "America/Tegucigalpa"],
            ["🇻🇪", "America/Caracas"],
            ["🇳🇮", "America/Managua"],
            ["🇨🇺", "Cuba"],
            ["🇺🇸", "US/Pacific"]
        ]

        # Inicializamos el diccionario
        times = {}

        # If you need Brazil:
        # ["🇧🇷","America/Sao_Paulo"]

        # Los timezones no están derivados de países, sino de ciudades.
        # Aunque la prioridad es por país

        for country in zones:
            zone = country[1]
            flag = country[0]
            dtc = date_to_convert.astimezone(pytz.timezone(zone))
            if zone == "Europe/Madrid":
                # Imprime la hora en formato de 24 horas y una "H" al final
                dtc = dtc.strftime("%-HH")
            else:
                # Imprime la hora en formato de 12 horas PM/AM
                dtc = dtc.strftime("%-I%p")
            try:
                times[dtc] = times[dtc] + flag
            except KeyError:
                times[dtc] = flag

            # Si el país es USA en Pacific, agregar el "PT" frente a bandera de US
            if zone == "US/Pacific":
                times[dtc] = times[dtc] + " PT"

            times[dtc] = times[dtc] + " "

        for t, c in times.items():
            print(t.lower(), c.strip())


def parse(date_to_convert):
    try:
        return datetime.datetime.strptime(
            date_to_convert, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None


if __name__ == '__main__':
    print_flags()
