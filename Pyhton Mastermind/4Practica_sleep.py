from time import sleep
import _random
import os

def my_function ():
    letra = input("Inserta una letra: ").upper()
    if letra == "Z":
        print("La letra oculta era Z")
    else:
        my_function()

def main():
    my_function()
    sleep(2)
    os.system("clear")

if __name__ == "__main__":
    main()
