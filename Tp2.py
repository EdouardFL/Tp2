import random

min = 0
max = 10

reponse = 0
tries = 0

def initiate():
    global reponse
    reponse = random.randint(min, max)  # Choisi un nombre entre le min et le max
    print("J'ai choisi un nombre entre",min,max,".")
    guessfunc()

def guessfunc():
    guess = input("Essayer de deviner ce nomber:")
    guess = int(guess)
    global tries

    if guess > reponse:
        print("Votre reponse est plus grande que le nombre mysterieux !!")
        tries += 1
        guessfunc()

    elif guess < reponse:
        print("Votre reponse est plus petit que le nombre mysterieux ")
        tries += 1
        guessfunc()

    elif guess == reponse:
        tries += 1
        print("VOUS AVEZ EU LA BONNE REPONSE YOUPI !!!!")
        print("Cela vous a prit:",tries,"essaies")
        restart()

def restart():
    retry = input("Voulez vous re-jouez ???????? (O/N)")
    if retry == "O" or retry == "o":
        initiate()
    else:
        print("Au revoir !!")

initiate()