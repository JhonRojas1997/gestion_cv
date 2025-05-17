import json
import csv

def exportar_csv():
    with open("datos.json", "r", encoding="utf-8") as f:
        datos = json.load(f)

    with open("exportado.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nombres", "Documento", "Correo", "Habilidades"])
        for hoja in datos:
            writer.writerow([
                hoja["datos_personales"]["nombres"],
                hoja["datos_personales"]["#documento"],
                hoja["datos_personales"]["email"],
                ", ".join(hoja["habilidades"])
            ])
    print("Exportado correctamente a exportado.csv.")
