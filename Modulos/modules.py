import sys
print(sys.path)

import re
text = "My telephone number is: 1234"
print(re.findall('[0-9]+', text)) # busca todas las coincidencias de numeros en text

import time
time_stamp = time.time()
local_hour = time.localtime()
print(time_stamp) # Formato unix
print(time.asctime(local_hour)) # Formato normal

import collections
numbers = [1,2,1,1,1,1,1,2,3,3,4,4,5,56,]
counter = collections.Counter(numbers) # Cuenta el numero de repeticiones de los elementos de la lista
print(counter)


