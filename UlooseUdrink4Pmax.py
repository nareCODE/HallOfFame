from random import shuffle
from time import sleep

NbrPlayers = int(input("Combien de joueurs ?"))

if NbrPlayers == 2:
    playerNames = ['Joueur 1', 'Joueur 2']
    print("Putin vous etes deux vraies poches a gnole vous deux !")
    print(" ")
    print("Et c est partit pour Qui perd boit !")
    print(" ")
    print("Choisissez un nom pour le Joueur 1 ou Equipe 1 !")
    player1 = input()
    playerNames = [player1, 'Joueur 2']
    print(playerNames)
    print("Choisissez un nom pour le Joueur 2 ou Equipe 2 !")
    player2 = input()
    playerNames = [player1, player2]
    print(playerNames)
    print("Les Equipes sont maintenant pretes.")
    print("Le match va maintenant commencer entre " + player1 + " et " + player2)
    shuffle(playerNames)
    winner = playerNames[0]
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    print("C est " + winner + " qui gagne et c est " + playerNames[1] + " qui doit boire !")
    print(" ")
    print("Le jeu a prit fin")
    print(" ")
elif NbrPlayers == 3:
    playerNames = ['Joueur 1', 'Joueur 2', 'Joueur 3']
    print("Sa va encore finir en threesome cette histoire !")
    print(" ")
    print("Et c est partit pour Qui perd boit !")
    print(" ")
    print("Choisissez un nom pour le Joueur 1 ou Equipe 1 !")
    player1 = input()
    playerNames = [player1, 'Joueur 2', 'Joueur 3']
    print(playerNames)
    print("Choisissez un nom pour le Joueur 2 ou Equipe 2 !")
    player2 = input()
    playerNames = [player1, player2, 'Joueur 3']
    print(playerNames)
    print("Choisissez un nom pour le Joueur 3 ou Equipe 3 !")
    player3 = input()
    playerNames = [player1, player2, player3]
    print(playerNames)
    print("Les Equipes sont maintenant pretes.")
    print("Le match va maintenant commencer entre " + player1 + ", " + player2 + " et " + player3)
    shuffle(playerNames)
    winner = playerNames[0]
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    print("C est le  " + winner + " qui gagne, les autres GO pillavent bande de loosers !")
    print(" ")
    print(" ")
elif NbrPlayers == 4:
    playerNames = ['Joueur 1', 'Joueur 2', 'Joueur 3', 'Joueur 4']
    print("Apres le jeu c est sure sa finit en partouze !")
    print(" ")
    print("Et c est partit pour Qui perd boit !")
    print(" ")
    print("Choisissez un nom pour le Joueur 1 ou Equipe 1 !")
    player1 = input()
    playerNames = [player1, 'Joueur 2', 'Joueur 3', 'Joueur 4']
    print(playerNames)
    print("Choisissez un nom pour le Joueur 2 ou Equipe 2 !")
    player2 = input()
    playerNames = [player1, player2, 'Joueur 3']
    print(playerNames)
    print("Choisissez un nom pour le Joueur 3 ou Equipe 3 !")
    player3 = input()
    playerNames = [player1, player2, player3]
    print(playerNames)
    print("Choisissez un nom pour le Joueur 4 ou Equipe 4 !")
    player4 = input()
    playerNames = [player1, player2, player3, player4]
    print(playerNames)
    print("Les Equipes sont maintenant pretes.")
    print("Le match va maintenant commencer entre " + player1 + ", " + player2 + ", " + player3 + " et " + player4)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    shuffle(playerNames)
    winner = playerNames[0]
    print("C est le  " + winner + " qui gagne, et les blairots restants peuvent boire !")
    print(" ")
    print(" ")

else:
    print("Erreur, veuillez rentrer une nombre.")
    print(" ")
    print(" ")

play_again = input("Voulez vous rejouez ? Oui ou Non?\n")

if play_again == "Oui":
    exec(open("./quiboitperd_multiplayers.py").read())
if play_again == "oui":
    exec(open("./quiboitperd_multiplayers.py").read())
else:
    exit()