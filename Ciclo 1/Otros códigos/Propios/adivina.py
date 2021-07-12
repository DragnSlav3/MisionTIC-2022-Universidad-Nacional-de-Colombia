from random import randint

def adivina():
    a = randint(0, 100)
    b = randint(100, 1000)
    x = (randint(a, b))
    try:
        y = int(input(f"Trata de adivinar el número. Una pista: Está entre {a} y {b}: "))

        while y != x:
            if y > x:
                y = int(input("Intenta con un número más bajo: "))
            if y < x:
                y = int(input("Intenta con un número más grande: "))
        print(f"Felicitaciones!, adivinaste el número: {x}")
    
    except ValueError:
        print("No ingresaste un número. Ingresa un número.")
        adivina()

adivina()