# TP-Integrador-OE-Abril_Ramos_C1
# GESTIÓN DE VACACIONES - CHATBOT

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un chatbot en consola que automatiza el proceso de solicitud de vacaciones de empleados dentro de una organización.

El objetivo principal es optimizar un proceso administrativo que normalmente se realiza de forma manual, reduciendo tiempos de espera, errores humanos y mejorando la organización interna.

El chatbot permite:

- Solicitar vacaciones
- Validar la existencia del empleado
- Verificar disponibilidad de fechas
- Aprobar o rechazar solicitudes
- Registrar la información automáticamente

---

## Tecnologías utilizadas

- Python
- CSV como base de datos simulada
- GitHub para control de versiones

---

## Estructura del proyecto

```text
proyecto/
│── chatbot.py
│── vacaciones.csv
│── README.md
```

---

## Base de datos

El sistema utiliza un archivo llamado `vacaciones.csv` para almacenar información de empleados y fechas ya registradas.

Ejemplo:

```csv
nombre,dni,fecha_inicio,fecha_fin
Juan Perez,12345678,2026-07-10,2026-07-15
Ana Lopez,23456789,2026-08-01,2026-08-05
Carlos Diaz,34567890,2026-09-12,2026-09-18
```

---

## Cómo ejecutar el proyecto

1. Tener instalado Python.
2. Descargar o clonar el repositorio.
3. Verificar que el archivo `vacaciones.csv` esté en la misma carpeta que `chatbot.py`.
4. Ejecutar el siguiente comando:

```bash
python chatbot.py
```

---

## Funcionamiento

El chatbot realiza el siguiente flujo:

1. Solicita el DNI del empleado.
2. Verifica si existe en la base de datos.
3. Solicita fecha de inicio y fecha de fin.
4. Comprueba si las fechas están disponibles.
5. Aprueba o rechaza la solicitud.

---

## Lógica de decisiones

El sistema trabaja con dos validaciones principales:

### Validación de empleado
- Si el empleado existe, continúa.
- Si no existe, finaliza.

### Validación de fechas
- Si las fechas están disponibles, aprueba.
- Si están ocupadas, rechaza.

---

## Manejo de errores

El sistema contempla errores como:

- DNI inexistente
- Fechas ocupadas
- Datos mal ingresados

---

## Autor

Abril Genoveva Ramos Dietmair

Trabajo Práctico Integrador  
Organización Empresarial  
Tecnicatura Universitaria en Programación
