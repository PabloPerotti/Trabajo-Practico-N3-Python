# Cree un programa que calcule el IMC (Indice de masa corporal). Formula --> IMC=Peso/Altura2 (Peso sobre altura al cuadrado)
# El usuario debera ingresar su peso y su altura (su nombre si quieren y despues imprimirlo concatenado) y el programa ademas de 
# calcular el IMC debera decir en que clasificacion se encuentra.
# La clasificacion la encontraran el archivo de imagen: IMC_clasificacion.jpg

nombre = input("Ingrese su Nombre y Apellido: ")
peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura**2)

if imc >= 40:
    print(f"{nombre} usted tiene Obesidad grado 3")
elif imc >=35.0 and imc <= 39.9:
    print(f"{nombre} usted tiene Obesidad grado 2")
elif imc >=30.0 and imc <=34.9:
    print(f"{nombre} usted tiene Obesidad grado 1")
elif imc >=25.0 and imc <= 29.9:
    print(f"{nombre} usted tiene Sobrepeso")
elif imc >=18.5 and imc <= 24.9:
    print(f"{nombre} usted tiene un Peso Adecuado")
else:
    print(f"{nombre} usted tiene Bajo Peso")
        

