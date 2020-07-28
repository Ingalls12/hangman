import random
def main():
    titulo()
    juego()
def juego():
    jug = jugadores()
    lista = ["Ornitorrinco", "Adivinanza","Estres", "Ventilador","Modem","Ensayo", "Buenavista"]
    palabra = lista[random.randint(0,len(lista)-1)]
    print(f"Adivina la palabra {jug[1]}:")
    print(adivinar(palabra, jug))

def adivinar(palabra, jug):
    palabra = palabra.lower()
    nespacios = []
    for a in range(len(palabra)):
        nespacios.append("_")
    num = 0
    while (num <6):
        print(plano_juego(num))
        print(nespacios)
        letra = input(f"Dime que letra crees que este en la palabra {jug[1]}:\n").lower()



        if letra in nespacios:
            print("ya utilizaste esa letra")
            num += 1
        elif letra in palabra:
            for pal in range(len(palabra)):
                if letra == palabra[pal]:
                    nespacios[pal] = palabra[pal]
        else:
            print("Esa letra no esta en la palabra")
            num += 1
        if "_" not in nespacios:
            nespacios = "".join(nespacios).title()
            print(nespacios)
            return f"Feliciades Ganaste {jug[1]}"


    return f"Perdiste {jug[1]} la palabra era {palabra}"

def titulo():
    print("////////////////")
    print("///AHORCADO/////")
    print("////////////////")


def plano_juego(num):
    if num == 0:
        print()
        print("\t------------------------")
        print("\t|                      |")
        print("\t|                      |")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")
        print("-----------")
    elif num == 1:
        plano_juego1()
    elif num == 2:
        plano_juego2()
    elif num == 3:
        plano_juego3()
    elif num == 4:
        plano_juego4()
    elif num == 5:
        plano_juego5()
    elif num == 6:
        plano_juego6()
    return ""
def plano_juego6():
    print()
    print("\t------------------------")
    print("\t|                      |")
    print("\t|                      _")
    print("\t|                     |_|")
    print("\t|                    \ | / ")
    print("\t|                     \|/ ")
    print("\t|                      | ")
    print("\t|                     / \ ")
    print("\t|                    /   \ ")
    print("\t|")
    print("-----------")
def plano_juego5():
    print()
    print("\t------------------------")
    print("\t|                      |")
    print("\t|                      _")
    print("\t|                     |_|")
    print("\t|                    \ | / ")
    print("\t|                     \|/ ")
    print("\t|                      | ")
    print("\t|                     /  ")
    print("\t|                    /   ")
    print("\t|")
    print("-----------")
def plano_juego4():
    print()
    print("\t------------------------")
    print("\t|                      |")
    print("\t|                      _")
    print("\t|                     |_|")
    print("\t|                    \ | / ")
    print("\t|                     \|/ ")
    print("\t|                      | ")
    print("\t|                     ")
    print("\t|                    ")
    print("\t|")
    print("-----------")
def plano_juego3():
    print()
    print("\t------------------------")
    print("\t|                      |")
    print("\t|                      _")
    print("\t|                     |_|")
    print("\t|                      | / ")
    print("\t|                      |/ ")
    print("\t|                      | ")
    print("\t|                     ")
    print("\t|                    ")
    print("\t|")
    print("-----------")
def plano_juego2():
    print()
    print("\t------------------------")
    print("\t|                      |")
    print("\t|                      _")
    print("\t|                     |_|")
    print("\t|                      |  ")
    print("\t|                      | ")
    print("\t|                      | ")
    print("\t|                     ")
    print("\t|                    ")
    print("\t|")
    print("-----------")

def plano_juego1():
    print()
    print("\t------------------------")
    print("\t|                      |")
    print("\t|                      _")
    print("\t|                     |_|")
    print("\t|                        ")
    print("\t|                       ")
    print("\t|                       ")
    print("\t|                     ")
    print("\t|                    ")
    print("\t|")
    print("-----------")
def jugadores():
    j1 = "Computadora"
    j2 = input("Escribe tu nombre jugador: ")
    return j1,j2

if __name__ == '__main__':
    main()