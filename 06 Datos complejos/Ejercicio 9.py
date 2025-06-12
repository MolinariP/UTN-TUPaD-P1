agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Turno médico"
}

print("Agenda actual:")
for clave, evento in agenda.items():
    print(f"{clave[0].capitalize()} a las {clave[1]} → {evento}")

dia = input("\nIngrese el día a consultar: ").lower()
hora = input("Ingrese la hora (formato hh:mm): ")

clave = (dia, hora)
if clave in agenda:
    print(f"\nActividad programada: {agenda[clave]}")
else:
    print("\nNo hay ninguna actividad programada en ese día y hora.")
