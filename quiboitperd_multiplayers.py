from random import shuffle
from time import sleep
# infinite player mode quiperdboit
print("**CHAQUE PARTICIPANT SE VOIT ATTRIBUE UN NUMERO DE JOUEUR APRES LA SELECTION DU NOMBRE DE PARTICPANTS")
print("Combien de joueurs?")
players = int(input())
if players == 2:
    players = ['Joueur 1', 'Joueur 2']
    print("Putin vous etes deux vraies poches a gnole vous deux !")
    print(" ")
    print("Et c est partit pour Qui perd boit !")
    print(" ")
    print("Choisissez un nom pour le Joueur 1 ou Equipe 1 !")
    player1 = input()
    players = [player1, 'Joueur 2']
    print(players)
    print("Choisissez un nom pour le Joueur 2 ou Equipe 2 !")
    player2 = input()
    players = [player1, player2]
    print(players)
    print("Les Equipes sont maintenant pretes.")
    print("Le match va maintenant commencer entre " + player1 + " et " + player2)
    shuffle(players)
    winner = players[0]
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    print("C est le " + winner + " qui gagne et c est " + players[1] + " qui doit boire !")
elif players == 3:
    players = ['Joueur 1', 'Joueur 2', 'Joueur 3']
    print("Sa va encore finir en threesome cette histoire !")
    print(" ")
    print("Et c est partit pour Qui perd boit !")
    print(" ")
    print("Choisissez un nom pour le Joueur 1 ou Equipe 1 !")
    player1 = input()
    players = [player1, 'Joueur 2', 'Joueur 3']
    print(players)
    print("Choisissez un nom pour le Joueur 2 ou Equipe 2 !")
    player2 = input()
    players = [player1, player2, 'Joueur 3']
    print(players)
    print("Choisissez un nom pour le Joueur 3 ou Equipe 3 !")
    player3 = input()
    players = [player1, player2, player3]
    print(players)
    print("Les Equipes sont maintenant pretes.")
    print("Le match va maintenant commencer entre " + player1 + ", " + player2 + " et " + player3)
    shuffle(players)
    winner = players[0]
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    print("C est le  " + winner + " qui gagne, les autres GO pillavent bande de loosers !")
elif players == 4:
    players = ['Joueur 1', 'Joueur 2', 'Joueur 3', 'Joueur 4']
    print("Apres le jeu c est sure sa finit en partouze !")
    shuffle(players)
    winner = players[0]
    print("Et c est partit pour Qui perd boit !")
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    print("C est le  " + winner + " qui gagne, et les blairots restants peuvent boire !")
elif players == 5:
    players = ['Joueur 1', 'Joueur 2', 'Joueur 3', 'Joueur 4', 'Joueur 5']
    shuffle(players)
    winner = players[0]
    print("Et c est partit pour Qui perd boit !")
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    print("C est le  " + winner + " qui gagne, les loosers restants doivent ingurgiter !")
else:
    print("Erreur, veuillez rentrer une nombre.")
