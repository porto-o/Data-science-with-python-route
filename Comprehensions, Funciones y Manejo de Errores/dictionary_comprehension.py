
# {key: value for var in iterable if condition}


'''
dict = {}
for i in range(1,5):
    dict[i] = i * 2;

print(dict)

# Se le agrega un par clave valor antes del for
dict_v2 = {i: i * 2 for i in range(1,5)}
print(dict_v2)

'''

import random
countries = ['col','mex','bol','per']
population = {}

for country in countries:
    population[country] = random.randint(1, 100);

print(population)

population = {country: random.randint(1, 100) for country in countries}

result = {country: population for (country, population) in population.items() if population > 20}

print(result)

print(population)


# Unimos 2 listas creando una lista de tuplas con la funcion zip
# Después hacemos un diccionario con cada tupla
names = ['ismael','roberto','fulano']
ages = ['19','16','8']

print(list(zip(names,ages)))

person = {name: age for (name,age) in zip(names,ages)}
print(person)


texto = "Hola, soy Ismael"

vocales = {vocal: vocal for vocal in texto if vocal in 'aeiou'}
print(vocales)