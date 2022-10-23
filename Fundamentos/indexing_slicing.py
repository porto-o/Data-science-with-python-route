text = "Ismael Porto Garcia"

'''
    Al insertar numeros negativos dentro del index de
    la palabra, nos devuelve la posicion del tamaño de
    la cadena MENOS el parametro ingresado.

    Las instrucciones de abajo, nos devuelven la misma salida.
'''

print(text[-15])
print(text[len(text) - 15])

# Slicing
'''
    El slicing nos sirve para devolver la cadena dentro de 
    determinados índices.
'''


print(text[0:10])
print(text[:10]) # Si no se envia primer parametro, python lo toma como 0

print(text[5:]) # si no recibe parametro, python llega hasta el final

print(text[:]) # Inicio al final

'''
    El slicing también puede recibir 3 parametros, siendo este tercero
    el número de saltos que dará python.

    El ultimo parametro es incluyente
'''

print(text[::2])