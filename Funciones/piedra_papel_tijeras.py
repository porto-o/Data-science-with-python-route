import random

opciones = ("1 -> piedra","2 -> papel","3 -> tijeras")
computer_wins = 0
global user_wins

def procesamiento(opcion_user):
    opcion_p = opcion_pc()
    if opcion_user == opcion_p:
        print("*** Empate ***\n")
        round()
    elif opcion_user == 1 and opcion_p == 2:
        computer_wins += 1
        round() 
    elif opcion_user == 1 and opcion_p == 3:
        user_wins += 1
        round()
    elif opcion_user == 2 and opcion_p == 1:
        user_wins += 1
        round()
    elif opcion_user == 2 and opcion_p == 3:
        computer_wins += 1
        round()
    elif opcion_user == 3 and opcion_p == 1:
        computer_wins += 1
        round()
    else:
        user_wins += 1
        round()

def start():
    
    while(computer_wins < 2 or user_wins < 2):
        print("Round ",computer_wins+1)
        opcion_user = input(f"Escribe el numero {opciones}: \n")
        procesamiento(opcion_user)
    
    if(computer_wins > user_wins):
        print("PC GANÓ")
    else:
        print("Ganaste")



def opcion_pc():
    opcion = random.randint(1, 3)
    return opcion

start()