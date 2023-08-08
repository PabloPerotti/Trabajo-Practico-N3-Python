# Escribí un programa que solicite al usuario el ingreso de dos números diferentes y muestre en pantalla al mayor de los dos.

##### Nota: Este es un poco mas complicado, pero con lo que vimos hasta la fecha, lo pueden resolver. #####

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

if numero1 == numero2:
    print("los numeros son iguales")
elif numero1 >= numero2:
    print(f"{numero1} es el mayor entre los dos numeros")
else:
    print(f"{numero2} es el mayor entre los dos numeros")
