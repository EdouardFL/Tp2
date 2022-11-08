#Code crée par Édouard F.L.
#Ce code permet a l'utilisateur de jouer a un petit jeu de devinette
import random

min = 0
max = 100

reponse = 0 #La réponse
essaies = 0 #Le nombre d'essaies

#fonction qui initialize le jeu
def initiate():
    global min,max
    min = int(input("Choisizer une borne minimale"))
    max = int(input("Choisizer une borne maximale"))

    global reponse
    reponse = random.randint(min, max)  # Choisi un nombre entre le min et le max
    print("J'ai choisi un nombre entre",min,max,".")

#Fonction qui permet au joueur de deviner
def guessfunc():
    guess = input("Essayer de deviner ce nomber:")
    guess = int(guess)
  

    #Si la réponse est plus grande que la réponse:
    if guess > reponse:
        print("Votre reponse est plus grande que le nombre mysterieux !!")
        return("Incorrect")

    #Si la réponse est plus petit que la réponse:
    elif guess < reponse:
        print("Votre reponse est plus petit que le nombre mysterieux ")
        return("Incorrect")

    #Si la réponse est egale que la réponse:
    elif guess == reponse:
        print("VOUS AVEZ EU LA BONNE REPONSE YOUPI !!!!")
        return("Correct")

#Re-initialise le code is le joueur veux
def restart():
    retry = input("Voulez vous re-jouez ???????? (O/N)")
    return retry

initiate()

playing = True

#Game loop
while playing:
    guess = guessfunc()

    #A chaque guess, on ajoute +1 a la variable essaies
    essaies += 1

    #Si le joueur devine correctement, on lui demande si il veut re-jouez. Sinon, la boucle recommence 
    if guess == "Correct":
        print("Cela vous a prit:", essaies, "essaies")
        rstart = restart()
        #Si le joueur veut re-jouez, on réinitialise le jeu et on met la variable essaies à 0
        if rstart == "O" or rstart == "o":
            essaies = 0
            initiate()
        else:
            print("Au revoir !!")
            #Tue la boucle
            playing = False

