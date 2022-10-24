# es otra forma de llenar listas
numbers = []
for element in range(1,11):
    numbers.append(element)

print(numbers)

'''
            Notacion List comprehension

    [element for element in iterable if condition]
    
    * La condicion no es necesaria
'''

numbers_v2 = [element for element in range(1,101) if element % 2 == 0]
print(numbers_v2)