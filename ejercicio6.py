# Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario introduce el divisor cero debera imprimir un mensaje de error.

##### Nota: Este es un poco mas complicado, pero con lo que vimos hasta la fecha, lo pueden resolver. #####

numero1 = float(input("Ingrese el dividendo de la division: "))
numero2 = float(input("Ingrese el divisor de la division: "))

if numero2 == 0:
    print("El divisor de la division no puede ser 0")
else:
    print(numero1 / numero2)
    