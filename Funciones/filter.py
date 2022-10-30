# filter() filtra aquellos elementos
# de un iterable que cumple con cierta condición
#
#           filter(function, iterable, ...)
#
# No modifica el estado original, crea una nueva lista


numbers = [1,2,3,4]

new_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(new_numbers)

