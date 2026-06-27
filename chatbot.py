import csv
from datetime import datetime

empleados = []
estado = 'inicio'


with open('vacaciones.csv', 'r') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        empleados.append(fila)

print('=== BOT DE GESTIÓN DE VACACIONES ===')

estado = 'validacion_empleado'


while True:
    dni = input('Ingrese su DNI: ').strip()

    if dni == '':
        print('Error: debe ingresar un DNI')

    elif not dni.isdigit():
        print('Error: el DNI debe contener solo números')

    else:
        empleado_encontrado = None

        for empleado in empleados:
            if empleado['dni'] == dni:
                empleado_encontrado = empleado
                break

        if empleado_encontrado is None:
            print('Empleado no encontrado. Intente nuevamente.')

        else:
            break

estado = 'validacion_fechas'


while True:
    fecha_inicio = input('Ingrese fecha de inicio (YYYY-MM-DD): ').strip()
    fecha_fin = input('Ingrese fecha de fin (YYYY-MM-DD): ').strip()

    try:
        fecha_inicio_obj = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_fin_obj = datetime.strptime(fecha_fin, '%Y-%m-%d')


        if fecha_inicio_obj > fecha_fin_obj:
            print('Error: la fecha de inicio no puede ser mayor a la fecha de fin')

        else:
            break

    except ValueError:
        print('Error: formato de fecha inválido')

estado = 'validacion_disponibilidad'
fecha_ocupada = False

for empleado in empleados:
    inicio_existente = datetime.strptime(empleado['fecha_inicio'], '%Y-%m-%d')
    fin_existente = datetime.strptime(empleado['fecha_fin'], '%Y-%m-%d')

    if fecha_inicio_obj <= fin_existente and fecha_fin_obj >= inicio_existente:
        fecha_ocupada = True
        break


if fecha_ocupada:
    estado = 'rechazo'
    print('Las fechas solicitadas no están disponibles')

else:
    estado = 'aprobacion'
    print('Solicitud aprobada')


    with open('vacaciones.csv', 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([
            empleado_encontrado['nombre'],
            dni,
            fecha_inicio,
            fecha_fin
        ])

    print('Vacaciones registradas correctamente')

estado = 'fin'
print('Estado final:', estado)