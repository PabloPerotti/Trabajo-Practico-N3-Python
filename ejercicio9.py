# Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. 
# Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.

##### Si hacen este son genios!!!! #####
##### Nota: Este es un poco mas complicado, pero con lo que vimos hasta la fecha, lo pueden resolver. ##### 

letra = str(input("ingrese una letra del abecedario: "))
letra_m = letra.lower()

if len(letra_m) > 1:
    print("Usted ingreso mas de una letra")
elif letra_m == "a" or letra_m == "e" or letra_m == "i" or letra_m == "o" or letra_m == "u":
    print(f"{letra_m} es una vocal!")
else:
    print(f"{letra_m} es una consonante")