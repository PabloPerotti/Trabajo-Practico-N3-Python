# Escribir un programa que almacene la cadena de caracteres digitalmind en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable

variable = "digitalmind"

contraseña = input("Ingrese su contraseña:")

if contraseña == variable:
    print("la contraseña coincide con la guardada en la variable") 
else: 
    print("contraseña incorrecta")
