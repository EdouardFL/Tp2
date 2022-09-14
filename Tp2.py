#Code crée par Édouard F.L.
#Ce code permet a l'utilisateur de jouer a un petit jeu de devinette
import random

min = 0
max = 10

reponse = 0 #La réponse
essaies = 0 #Le nombre d'essaies

def initiate(): #fonction qui initialize le jeu
    global reponse
    reponse = random.randint(min, max)  # Choisi un nombre entre le min et le max
    print("J'ai choisi un nombre entre",min,max,".")
    guessfunc()

def guessfunc(): #Fonction qui permet au joueur de deviner
    guess = input("Essayer de deviner ce nomber:")
    guess = int(guess)
    global essaies #globalise la variable essaies

    if guess > reponse: #Si la réponse est plus grande que la réponse:
        print("Votre reponse est plus grande que le nombre mysterieux !!")
        essaies += 1
        guessfunc()

    elif guess < reponse: #Si la réponse est plus petit que la réponse:
        print("Votre reponse est plus petit que le nombre mysterieux ")
        essaies += 1
        guessfunc()

    elif guess == reponse: #Si la réponse est egale que la réponse:
        essaies += 1
        print("VOUS AVEZ EU LA BONNE REPONSE YOUPI !!!!")
        print("Cela vous a prit:",essaies,"essaies")
        restart()

def restart(): #Re-initialze le code is le joueur veux
    retry = input("Voulez vous re-jouez ???????? (O/N)")
    if retry == "O" or retry == "o":
        initiate()
        global essaies #globalise la réponse
        essaies = 0
    else:
        print("Au revoir !!")

initiate()