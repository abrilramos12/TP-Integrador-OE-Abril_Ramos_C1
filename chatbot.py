import csv

empleados = []

with open('vacaciones.csv', 'r') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        empleados.append(fila)

print('=== BOT DE GESTIÓN DE VACACIONES ===')

dni = input('Ingrese su DNI: ')
empleado_encontrado = False

for empleado in empleados:
    if empleado['dni'] == dni:
        empleado_encontrado = True
        break

if empleado_encontrado == False:
    print('Empleado no encontrado')

else:
    fecha_inicio = input('Ingrese fecha de inicio (YYYY-MM-DD): ')
    fecha_fin = input('Ingrese fecha de fin (YYYY-MM-DD): ')

    fecha_ocupada = False

    for empleado in empleados:
        if empleado['fecha_inicio'] == fecha_inicio:
            fecha_ocupada = True

    if fecha_ocupada:
        print('Las fechas solicitadas no están disponibles')
    else:
        print('Solicitud aprobada')
        print('Vacaciones registradas correctamente')