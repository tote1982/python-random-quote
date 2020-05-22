import random

def principal():

    i = 0

    while i == 0:
        pregunta=input("Leer(L), Escribir(E) o Salir(S): ")
        if pregunta == "L":
            leer()
        elif pregunta == "E":
            escribir()
        elif pregunta == "S":
            i = 1
        else:
            print("Opción no válida(L/E/S)")

    print("Adios....")

def escribir():

  f = open("quotes.txt","at")

  item=input("Introduce una frase: ")
  f.write(str(item) + "\n")
  f.close()

def leer():
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    items = len(quotes)
    #seleccion = input(f"Elige un numero del 1 al {items}: ")
    #i = int(seleccion) - 1
    i = random.randint(0,items-1)
    print(quotes[i])


if __name__== "__main__":
  principal()


#EOF
