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