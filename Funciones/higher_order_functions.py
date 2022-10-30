def increment(x):
    return x + 1

# Esta funcion es la que se ejecutará,
# recibiendo una variable y una función como parametros
# al momento de ejecutarlo en la linea 14 solo mandamos
# el nombre de la funcion, más no su ejecución

# La ejecución iniciará en hog y mandará a '2' como 
# parametro a increment
def hog(x,func):
    return x + func(x)

result = hog(2, increment)
print(result)


# Se puede combinar con funciones lambda
# ya sea mandando el nombre de la variable que contiene a la funcion
# o mandando la expresión lambda directamente

#increment_v2 = lambda x : x + 1

hog_v2 = lambda x,func : x + func(x)

result = hog_v2(2,lambda x : x + 1)
print(result)