# Primos con teorema de Wilson
# (p-1)! + 1 = multiplo de p
# por lo tanto (p-1)! + 1 % p = 0
#  
def factorial(number):
    for i in range(number-1, 0, -1):
        number *=  i
    return number + 1

def run():
    # number = 1
    # while(True):
    #     if number == 1 or number < 0:
    #         print("")
    #     elif number == 0:
    #         print(number)
    #     else: 
    #         wilson = factorial(number-1) % number != 0
        
    #         if wilson == False:
    #             print(number) 
            
    #     number += 1
    number = int(input("Escribe el numero: "))

    if number == 1 or number < 0:
        print("No es primo")
    elif number == 0:
        print("Es primo")
    else: 

        wilson = factorial(number-1) % number != 0
       
        if wilson:
            print("No es primo")
        else:
            print("Es primo") 

if __name__ == '__main__':
    run()