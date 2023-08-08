# Nos solicitaron que realicemos un programa que le pida al usuario un numero y mostrar si el numero que ingreso tiene un solo digito, 
# si tiene dos digitos o mas de dos.
# # Luego nos solicitaron que sumemos una mejora, que consta de que muestre si el numero es negativo

numero = int(input("Ingrese un número: "))

if numero < 0:
    print("El número es negativo.")
elif len(str(numero)) == 1:
    print("El número tiene un solo dígito.")
elif len(str(numero)) == 2:
    print("El número tiene dos dígitos.")
else:
    print("El número tiene más de dos dígitos.")

