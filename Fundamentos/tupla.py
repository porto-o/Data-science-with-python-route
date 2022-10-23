# Inmutables

numbers = (1,2,3,4)
strings = ("Ismael","Porto","Garcia", "Ismael")

print(numbers)
print(type(numbers))

''' La tupla solo es de lectura '''

print(strings.index("Ismael"))
print(strings.count("Ismael"))

numbers = list(numbers)

print(type(numbers))