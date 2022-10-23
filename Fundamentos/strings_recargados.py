frase = "Hola soy ismael y me gusta estudiar xD"

print("Javascript" in frase)  # Busca si existe la palabra dentro de la cadena

size = len("Ismael Porto Garcia")  # len() devuelve el tamaño
print(size)

print(frase)
print(frase.upper()) # Mayusculas
print(frase.lower()) # Minusculas

print(frase.count('a')) # Cuenta cuantos caracteres hay en la cadena
print(frase.swapcase()) # cambia cualquier caracter mayuscula a minuscula y viceversa

print(frase.startswith('Hola')) # Pregunta si un texto inicia con una cadena en especifico
print(frase.endswith('xD'))

print(frase.replace('ismael', 'fulano')) # Reemplaza una cadena por otra

frase_2 = 'hola soy Fulano'
print(frase_2)
print(frase_2.capitalize()) # Primer caracter en mayus
print(frase_2.title()) # Mayuscula primer letra de cada palabra
print(frase_2.isdigit()) # Pregunta si es un digito

print("398".isdigit())