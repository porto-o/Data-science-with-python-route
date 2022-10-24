'''
    1. Son mutables
    2. No tienen orden
    3. No permiten duplicados
        => Si se ingresan duplicados, al momento de consultarlo
        se eliminan en la consulta
'''

set_countries = {"Mexico", "Francia", "Belgica"}

print(type(set_countries))
print(set_countries)

set_numbers = {1,2,3,4,5,6,7,8,9}
print(set_numbers)

set_types = {True, False, "Ismael"}
print(set_types)

set_from_string = set("Hola") # Convierte en conjunto la cadena
print(set_from_string)

tuple = (1,2,3,4,5)
set_from_tuple = set(tuple)
print(set_from_tuple)

numbers = [1,2,3,4]
set_from_list = set(numbers)
print(numbers)

# Conjuntos CRUD

size = len(set_countries);
print(size)

print('col' in set_countries)
print('Mexico' in set_countries) 

# add
set_countries.add('Peru')
print(set_countries)

# update
set_countries.update({'Argentina','Ecuador'})
print(set_countries)

# remove
set_countries.remove('Mexico')
print(set_countries)

# discard
print(set_countries.discard('Mexico'))

# clear
print(set_countries.clear())

# Operaciones de teoría de conjuntos

set_shopping = {'Platanos','Manzanas','Carne'}
set_refri = {'Refrescos','Carne','Cervezas'}

set_union = set_shopping.union(set_refri)
print(set_union)

set_intersection = set_shopping.intersection(set_refri)
print(set_intersection)

set_difference = set_shopping.difference(set_refri)
print(set_difference)

set_symmetric_difference = set_shopping.symmetric_difference(set_refri)
print(set_symmetric_difference)