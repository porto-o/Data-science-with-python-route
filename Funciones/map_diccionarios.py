items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

prices = list(map(lambda item: item['price'], items))
print(items)
print(prices)

def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items = list(map(add_taxes, items))

# Aquí podemos ver que ambos diccionarios se modificaron
# Para evitar que el original se modifique debemos de poner
# tención a lo que hacemos en la funcion add_taxes
# Estamos modificando el original o la referencia en memoria
print(new_items)
print(items)

# Para evitar esta modificación hacemos uso de la funcion
# copy()
# new_item = item.copy()
# new_item['taxes'] = new_item['prices'] *.19
