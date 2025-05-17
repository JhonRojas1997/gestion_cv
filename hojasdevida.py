import json

def registrar_hoja_de_vida():
    nombre = input("Nombre: ")
    documento = input("Documento: ")
    correo = input("Correo: ")
    nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    habilidades = input("Habilidades (separadas por coma): ").split(",")

    nueva_hoja = {
        "datos_personales": {
            "nombres": nombre,
            "#documento": documento,
            "email": correo,
            "nacimiento": nacimiento,
            "direccion": direccion,
            "telefono": telefono
        },
        "formacion": [],
        "experiencia": [],
        "referencias": [],
        "habilidades": [h.strip() for h in habilidades]
    }

    try:
        with open("datos.json", "r", encoding="utf-8") as f:
            datos = json.load(f)
    except FileNotFoundError:
        datos = []

    datos.append(nueva_hoja)

    with open("datos.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    print("Hoja de vida registrada.")

def ver_hoja_de_vida():
    try:
        with open("datos.json", "r", encoding="utf-8") as f:
            datos = json.load(f)
    except FileNotFoundError:
        print("No hay hojas de vida registradas.")
        return

    if not datos:
        print("Esta lista se encuentra vacía actualmente.")
        return

    print("\nSelecciona una hoja de vida:")
    for i, hoja in enumerate(datos):
        print(f"{i + 1}. {hoja['datos_personales']['nombres']}")

    try:
        seleccion = int(input("Ingresa el número de la hoja de vida que quieres ver: ")) - 1
        if seleccion < 0 or seleccion >= len(datos):
            print("Esta opción está fuera del rango.")
            return

        hoja = datos[seleccion]

        print("\nEsta es la hoja de vida seleccionada:\n")

        print("Datos personales:")
        for k, v in hoja['datos_personales'].items():
            print(f"  {k.capitalize()}: {v}")

        print("\nFormación académica:")
        for f in hoja['formacion']:
            print(f"  - {f['titulo']} en {f['institucion']} ({f['años']})")

        print("\nExperiencia profesional:")
        for e in hoja['experiencia']:
            print(f"  - {e['cargo']} en {e['empresa']} ({e['duracion']}): {e['funciones']}")

        print("\nReferencias:")
        for r in hoja['referencias']:
            print(f"  - {r['nombre']} ({r['relacion']}): {r['telefono']}")

        print("\nHabilidades:")
        print("  " + ", ".join(hoja['habilidades']))

    except ValueError:
        print("Entrada inválida.")

def actualizar_hoja_de_vida():
    try:
        with open("datos.json", "r", encoding="utf-8") as f:
            datos = json.load(f)
    except FileNotFoundError:
        print("No hay hojas de vida registradas.")
        return

    if not datos:
        print("Lista vacía.")
        return

    print("\nSeleccione la hoja de vida a actualizar:")
    for i, hoja in enumerate(datos):
        print(f"{i + 1}. {hoja['datos_personales']['nombres']}")

    try:
        seleccion = int(input("Ingrese el número de la hoja de vida: ")) - 1
        if seleccion < 0 or seleccion >= len(datos):
            print("Opción inválida.")
            return

        hoja = datos[seleccion]

        print("\n¿Qué desea actualizar?")
        print("1. Datos personales")
        print("2. Formación académica")
        print("3. Experiencia laboral")
        print("4. Habilidades")
        print("5. Referencias")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for campo in hoja['datos_personales']:
                nuevo_valor = input(f"{campo.capitalize()} actual: {hoja['datos_personales'][campo]}. Nuevo (Enter para mantener): ")
                if nuevo_valor.strip():
                    hoja['datos_personales'][campo] = nuevo_valor.strip()

        elif opcion == "2":
            institucion = input("Institución: ")
            titulo = input("Título: ")
            años = input("Años: ")
            hoja['formacion'].append({
                "institucion": institucion,
                "titulo": titulo,
                "años": años
            })

        elif opcion == "3":
            empresa = input("Empresa: ")
            cargo = input("Cargo: ")
            funciones = input("Funciones: ")
            duracion = input("Duración: ")
            hoja['experiencia'].append({
                "empresa": empresa,
                "cargo": cargo,
                "funciones": funciones,
                "duracion": duracion
            })

        elif opcion == "4":
            nuevas = input("Ingrese nuevas habilidades separadas por coma: ").split(",")
            hoja['habilidades'].extend([h.strip() for h in nuevas if h.strip()])

        elif opcion == "5":
            nombre = input("Nombre: ")
            relacion = input("Relación: ")
            telefono = input("Teléfono: ")
            hoja['referencias'].append({
                "nombre": nombre,
                "relacion": relacion,
                "telefono": telefono
            })

        elif opcion == "0":
            return

        else:
            print("Opción inválida.")
            return

        with open("datos.json", "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

        print("Hoja de vida actualizada correctamente.")

    except ValueError:
        print("Entrada inválida.")

def eliminar_hoja_de_vida():
    try:
        with open("datos.json", "r", encoding="utf-8") as f:
            datos = json.load(f)
    except FileNotFoundError:
        print("No hay hojas de vida registradas.")
        return

    if not datos:
        print("No hay registros para eliminar.")
        return

    print("\nSeleccione la hoja de vida a eliminar:")
    for i, hoja in enumerate(datos):
        print(f"{i + 1}. {hoja['datos_personales']['nombres']}")

    try:
        seleccion = int(input("Ingrese el número de la hoja de vida a eliminar: ")) - 1
        if seleccion < 0 or seleccion >= len(datos):
            print("Opción inválida.")
            return

        confirmacion = input(f"¿Está seguro que desea eliminar la hoja de vida de {datos[seleccion]['datos_personales']['nombres']}? (s/n): ").lower()
        if confirmacion == 's':
            eliminado = datos.pop(seleccion)
            with open("datos.json", "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
            print(f"Hoja de vida de {eliminado['datos_personales']['nombres']} eliminada correctamente.")
        else:
            print("Eliminación cancelada.")

    except ValueError:
        print("Entrada inválida.")