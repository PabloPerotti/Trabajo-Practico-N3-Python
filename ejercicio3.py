# Para pagar un determinado impuesto se debe ser mayor de 18 años y tener unos 
# ingresos iguales o superiores a 20000 ARS mensuales. Escribir un programa que pregunte 
# al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que pagar un impuesto o no.


edad = int(input("Ingrese su edad: "))
ingresos = int(input("Ingrese sus ingresos mensuales: "))

if edad >= 18 and ingresos >= 20000:
    print("Usted tiene que pagar inpuestos")
else:
    if edad <= 18 and ingresos >= 20000:
        print("Usted tiene que ser mayor de 18 años para pagar inpuestos")
    else:
        print("No paga inpuestos por ser pobre")