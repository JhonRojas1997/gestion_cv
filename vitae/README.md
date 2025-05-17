# VitaeConsole

Sistema de gestion y guardado de hojas de vida.

## Integrantes
Cristian Cano Castaño
Jhon Fredy Rojas Remolina
Jonathan Licona

## Características
Se crea un sistema para manejo de hojas de vida el cual cuenta con las siguientes caracteristicas.

- Registro hojas de vida.
- Actualizacion hojas de vida.
- Consulta de hojs de vida.
- Eliminar hojas de vida
- Reportes exportables en CSV
- Guardado de hojas de vida en archivo Json
- Uso de estructuras de datos y librerías estándar

## Explicacion codigo

`registrar_hoja_de_vida():`
permite al usuario ingresar información personal para crear una hoja de vida. Los datos solicitados incluyen nombre, documento, correo, fecha de nacimiento, dirección, teléfono, habilidades y demas. 

Los datos se organizan en un diccionario (nueva_hoja) que contiene secciones para datos personales, formación, experiencia, referencias y habilidades.
Luego, intenta leer un archivo JSON existente llamado "datos.json" para cargar hojas de vida previamente registradas. Si el archivo no existe, inicializa una lista vacía. Después, añade la nueva hoja de vida a la lista y guarda todos los datos de nuevo en "datos.json", asegurándose de que se puedan visualizar correctamente caracteres especiales. Finalmente, imprime un mensaje de confirmación de que la hoja de vida ha sido registrada.

`ver_hoja_de_vida():`
Permite al usuario visualizar una hoja de vida almacenada en un archivo JSON. Primero, intenta cargar los datos desde "datos.json" y maneja el error si el archivo no se encuentra o si la lista está vacía. Luego, muestra una lista numerada de las hojas de vida disponibles y pide al usuario que elija una. Si la selección es válida, imprime los detalles de la hoja de vida seleccionada, incluyendo datos personales, formación académica, experiencia profesional, referencias y habilidades. Maneja errores de entrada no válida cuando el usuario ingresa un número incorrecto.

`eliminar_hoja_de_vida`:
Permite al usuario eliminar una hoja de vida de un archivo JSON. Primero, intenta cargar los datos; si el archivo no existe o está vacío, informa al usuario. Luego, presenta una lista de hojas de vida disponibles y solicita al usuario seleccionar una para eliminar. Tras la confirmación, elimina la hoja seleccionada del archivo y guarda los cambios, o cancela la acción si el usuario lo desea.

`actualizar_hoja_de_vida()`:
Permite al usuario actualizar una hoja de vida almacenada en un archivo JSON. Primero, intenta leer los datos del archivo "datos.json". Si no encuentra el archivo o los datos están vacíos, muestra un mensaje correspondiente y termina. Luego, presenta una lista de hojas de vida disponibles y permite al usuario seleccionar una para actualizar. Se pueden modificar los datos personales, agregar formación académica, experiencia laboral, habilidades, y referencias. Después de realizar las actualizaciones, se guarda el archivo JSON de nuevo. Si se ingresa una opción inválida o hay un error en la entrada, se muestra un mensaje de error.

`exportar_csv():`
Lee un archivo JSON llamado "datos.json", extrae información personal y habilidades de cada entrada en el archivo, y la escribe en un nuevo archivo CSV llamado "exportado.csv". La primera fila del CSV contiene los encabezados "Nombres", "Documento", "Correo" y "Habilidades", y luego itera sobre cada registro en el JSON para llenar las filas con los datos correspondientes. Finalmente, imprime un mensaje indicando que la exportación fue exitosa.

## Uso
Ejecutar `main.py` desde consola para acceder al menú principal.
Desde el menu principal encontraremos 6 opciones las cuales se enumeran de la siguiente manera.

1. Registrar hoja de vida: En esta opcion se pediran los datos necesarios para crear una hoja de vida de manera organizada, con datos tales como, Datos personales, Formacion academica, habilidades y demas.

2. Ver las hojas de vida registradas: En esta opcion Podras ver las hojas de vida registradas mediante un menu que se despliega  para con esto seleccionar un numero y acceder a todos los datos de la hoja de vida seleccionada.

3. Eliminar hoja de vida: En esta opcion Podras ver las hojas de vida registradas mediante un menu que se despliega  para con esto seleccionar un numero y eliminar la hoja de vida que se desee eliminar, al seleccionar la hoja de vida a eliminar se despliega una opcion la cual se debe confirmar si deseas o no eliminar dicha hoja de vida.

4. Actualizar hoja de vida: En esta opcion Podras ver las hojas de vida registradas mediante un menu que se despliega  para con esto seleccionar un numero y acceder ala hoja de vida seleccinada para actualizar la hoja de vida de manera organizada. ingresando cada uno de los datos que desea eliminar.

5. Exportar a CSV: Exporta los datos a el archivo "exportado.csv".

6. Salir: Hace un break para salir del bucle y parar la ejecucion del codigo.