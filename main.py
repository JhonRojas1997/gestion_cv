from hojasdevida import registrar_hoja_de_vida
from hojasdevida import ver_hoja_de_vida
from hojasdevida import actualizar_hoja_de_vida
from hojasdevida import eliminar_hoja_de_vida
from reportes import exportar_csv

#nombre=input("¿Cual es tu Nombre?")
#print(f"Bienvenido {nombre} seleccione ¿que opcion requiere el dia de hoy?")

def menu():
    while True:
        print("\n--- VitaeConsole ---")
        print("1. Registrar hoja de vida")
        print("2. Ver las hojas de vida registradas")
        print("3. Eliminar hoja de vida")
        print("4. Actualizar hoja de vida")
        print("5. Exportar a CSV")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_hoja_de_vida()
        elif opcion == "2":
            ver_hoja_de_vida()
        elif opcion == "3":
            eliminar_hoja_de_vida()
        elif opcion == "4":
            actualizar_hoja_de_vida()
        elif opcion == "5":
            exportar_csv()
        elif opcion == "0":
            break
        else:
            print("Esta opcion no es valida ingresa un numero.")

if __name__ == "__main__":
    menu()
