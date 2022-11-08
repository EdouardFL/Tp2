#Code crée par Édouard F.L.
#Ce code permet a l'utilisateur de jouer a un petit jeu de devinette
import random

min = 0
max = 100

reponse = 0 #La réponse
essaies = 0 #Le nombre d'essaies

def initiate(): #fonction qui initialize le jeu
    global min,max
    min = int(input("Choisizer une borne minimale"))
    max = int(input("Choisizer une borne maximale"))

    global reponse
    reponse = random.randint(min, max)  # Choisi un nombre entre le min et le max
    print("J'ai choisi un nombre entre",min,max,".")

def guessfunc(): #Fonction qui permet au joueur de deviner
    guess = input("Essayer de deviner ce nomber:")
    guess = int(guess)
    #globalise la variable essaies

    if guess > reponse: #Si la réponse est plus grande que la réponse:
        print("Votre reponse est plus grande que le nombre mysterieux !!")
        return("Incorrect")

    elif guess < reponse: #Si la réponse est plus petit que la réponse:
        print("Votre reponse est plus petit que le nombre mysterieux ")
        return("Incorrect")

    elif guess == reponse: #Si la réponse est egale que la réponse:
        print("VOUS AVEZ EU LA BONNE REPONSE YOUPI !!!!")
        return("Correct")

def restart(): #Re-initialze le code is le joueur veux
    retry = input("Voulez vous re-jouez ???????? (O/N)")
    return retry

initiate()

playing = True

while playing:
    guess = guessfunc()
    essaies += 1

    if guess == "Correct":
        print("Cela vous a prit:", essaies, "essaies")
        rstart = restart()
        if rstart == "O" or rstart == "o":
            essaies = 0
            initiate()
        else:
            print("Au revoir !!")
            playing = False

