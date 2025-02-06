import random 

grille=["-","-","-",
        "-","-","-",
        "-","-","-"]

joueur_actuel=""
fin_jeu=False
#jeu ordinateur
def mouvement_ordinateur(symbole):
    print("C'est le tour de l'ordinateur")
    position=[i for i,val in enumerate(grille)if val=="-"]
    if position:
        pos=random.choice(position)
        
        grille[pos]=symbole
        affichage_grille()   
#jouer

def jouer():

    global grille,fin_jeu
    grille=["-","-","-",
        "-","-","-",
        "-","-","-"]

    fin_jeu == False
    

    # Attribution des symboles : par convention, le joueur humain aura "X" et l'ordinateur "0"
    symbole_humain = "X"
    symbole_ordi = "0"

# Choix aléatoire pour savoir qui commence
    tour_actuel = random.choice(["humain", "ordinateur"])
    print("Le joueur qui commence est :", tour_actuel)
    affichage_grille()

   # choix_joueur()
    while not fin_jeu:
        if tour_actuel == "humain":
            tour_joueur(symbole_humain)
            if verifier_victoire() is not None:
                print("Félicitations, vous avez gagné!")
                break
            if verifier_match_nul():
                print("Match nul!")
                break
            tour_actuel = "ordinateur"
        else:
            mouvement_ordinateur(symbole_ordi)
            if verifier_victoire() is not None:
                print("L'ordinateur a gagné!")
                break
            if verifier_match_nul():
                print("Match nul!")
                break
            tour_actuel = "humain"


# Affichage de la grille de jeu


def affichage_grille():
        """Affiche la grille de jeu de manière lisible."""
        print("\n-----------")
        print(grille[0], "|", grille[1], "|", grille[2])
        print("--+---+---")
        print(grille[3], "|", grille[4], "|", grille[5])
        print("--+---+---")
        print(grille[6], "|", grille[7], "|", grille[8])
        print("-----------\n")
#tour de jeu 

def tour_joueur(joueur):

    print("C'est le tour du joueur :",joueur)
    while True:
        pos = input("Veuillez selectionner une case vide entre 1 et 9 :")
        if pos not in ["1","2","3","4","5","6","7","8","9"] :
            print("Veuillez saisir un chiffre entre 1 et 9")
            continue
   
        pos=int(pos)-1

        if grille[pos] !='-':
                 print("postion occupée")
        else:
            grille[pos] = joueur
            break

    affichage_grille()

#savoir qui a gagné

def verifier_victoire():
    global fin_jeu
    global gagnant 
   #declaration combinaison gagnante
    
    combinaison=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in combinaison :
        if grille[a]==grille[b]==grille[c] and grille [c]!="-":
            fin_jeu=True
            gagnant=grille[c]

            return gagnant
    return None
#savoir si match nul 

def verifier_match_nul():
    global fin_jeu
    if "-" not in grille:
        fin_jeu=True
        return True
    return False


jouer()