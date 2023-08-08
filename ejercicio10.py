# Dos equipos de futbol están disputando el saque inicial del juego. 
# Los capitanes de cada equipo deciden jugar el clásico juego "Piedra, papel o tijera" para definir quien hace el saque. 
# Las reglas son las usuales: Piedra vence a Tijera, Tijera vence a Papel y Papel vence a Piedra.
# Juegan una sola vez.

opciones = ["piedra", "papel", "tijera"]

equipo1 = input("Equipo 1, elijan piedra, papel o tijera: ").lower()
equipo2 = input("Equipo 2, elijan piedra, papel o tijera: ").lower()

if equipo1 == equipo2:
    print("Empate!!, jueguen nuevamente.")
elif (equipo1 == "piedra" and equipo2 == "tijera") or (equipo1 == "papel" and equipo2 == "piedra") or (equipo1 == "tijera" and equipo2 == "papel"):
    print("Gano el equipo 1!!Hace el saque inicial")
else:
    print("Gano el equipo 2!!Hace el saque inicial")
    