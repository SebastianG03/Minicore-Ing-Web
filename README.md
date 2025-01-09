# Descripción
El presente código utiliza el Framework de FastApi en conjunto con una implementación de SQLAlchemy llamada SQLModel utilizada comúnmente junto a este Framework. Esto permite generar de manera automática la base de datos durante la primera ejecución del código dentro de una base de datos SQL Lite.

# Objetivo de la API
El objetivo de esta API es cumplir con los requerimientos especificados para la creación de este minicore. Los requerimientos son básicamente la creación de una API que permita al usuario administrar departamentos y empleados para realizar un seguimiento de sus gastos por departamento. Es decir, en base a dos fechas administradas por el usuario se filtrará el histórico de gastos con el fin de obtener el total de gasto de cada departamento.


## Arquitectura

El código se divide en application, core y entities.
- <b>infraestructure:</b> contiene la lógica tras el funcionamiento del código incluyendo los datos de la bases de datos, la manipulación de la base de datos y los servicios.
- <b>application:</b> contiene los controladores necesarios que aplican los routers de FastApi.
- <b>entities:</b> contiene todos los modelos necesarios que se utilizará en la aplicación.
- <b>tests:</b> contiene las pruebas unitarias para cada controlador.

## Tablas
Esta API administra 3 diferentes tablas presentes en la base de datos. <br>
Las tablas almacenadas en la base de datos son las siguientes:
- <b>Employees:</b> Almacena el nombre de cada empleado y le asigna automáticamente una ID.
- <b>Departments:</b> Enlista los nombres de los departamentos de la empresa.
- <b>Spents:</b> Es una tabla que contiene un histórico de los gastos de cada departamento y realiza un seguimiento de la fecha del gasto y su emisario (empleado que ejecutó dicho gasto).

## Implementación
Los requisitos para la implementación son los siguientes:
1. Tener instalado python 3.9 o superior, y declararlo en las variables del sistema
2. Clonar o descargar el proyecto y ejecutar la siguiente línea de código en la línea de comandos:


```
    ./Scripts/activate
    pip install -r /path/to/requirements.txt
```
3. Para ejecutar al API se utiliza el siguiente comando (asegúrese de que el terminal se encuentre en la posicion correcta)
```pip install -r /path/to/requirements.txt

    fastapi dev src/main.py
```
## Links
- Se puede acceder a la página por este link: http://127.0.0.1:8000/docs 
- Puede acceder a la página deployada por medio de este link: https://circular-dona-dasedev-cffcdb53.koyeb.app/docs

## Documentación adicional
- [FastAPI | API Example with SQL Model](https://fastapi.tiangolo.com/tutorial/sql-databases/#create-models)
- [SQL Model Relationships](https://sqlmodel.tiangolo.com/tutorial/fastapi/relationships/)
- [FastAPI Life Cycle Events](https://fastapi.tiangolo.com/advanced/events/)
- [How deploy an API using Fast Api on Koyeb](https://www.koyeb.com/docs/deploy/fastapi)

## Métodos de contacto:
- Email: guamandavid11235@gmail.com
- Número de contacto: +593 093 982 7471
