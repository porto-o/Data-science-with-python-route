'''
    The map() function applies a given function 
    to each item of an iterable (list, tuple etc.) 
    and returns an iterator.

    map(function, iterable, ...)

'''

numbers = [1,2,3]
result = map(lambda x:x*x, numbers)
print(result)
print(list(result))

names = ["Ismael ","Tadeo ","Judas "]
apellidos = ["Porto","Garcia","Lopez"]

full_names = list(map(lambda x,y : x + y, names, apellidos))
print(full_names)