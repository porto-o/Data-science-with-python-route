def table(number):
    for i in range(11):
        result = i * number
        print(f'{number} * {i} = {result}')

def run():
    number = int(input("Ingresa el numero para obtener su tabla de multiplicar: "))
    table(number)

if __name__ == '__main__':
    run()