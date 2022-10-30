def increment_fun(x):
    return x+1

increment = lambda x : x+1

result = print(increment(2))
result = print(increment_fun(2))

# lambda parametros : return       -> son funciones anónimas

full_name = lambda name,last : f'Hola, {name.title()} {last.title()}!!'

text = print(full_name('ismael','porto'))