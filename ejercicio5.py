# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y 
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 80 ARS y si es mayor de 18 años, 150 ARS.

edad = int(input("Ingrese la edad del usuario: "))

if edad < 4:
    print("El precio de la entrada es gratis")
elif edad >=4 and edad <= 18:
    print("El precio de la entrada que debe pagar es de 80 ARS")
else:
    print("El precio de la entrada que debe pagar es de 150 ARS")
    