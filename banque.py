from tkinter import *
import csv
import os
import datetime 

root=Tk()
root.title("Gestionnaire de Comptes")
#creation des classes
class Compte ():

    def __init__(self, numCompte=0, nomCompte="", solde=0) :
        self.solde=solde
        self.nomCompte=nomCompte
        self.numCompte=numCompte
        

#creation fonction pour creer compte
    def creeCompte(self):
        try:
            self.numCompte=int(input("Entrez le numero du compte "))
            self.nomCompte=input("Entrez le nom du compte ")
            self.solde=float(input("Entrez le solde du initial "))
            print(f"\n Compte créé : {self.numCompte},{self.nomCompte},Solde : {self.solde} XAF\n")
            return True
        except ValueError:
            print("Veuillez entrer un nombre valide")
            return False
        


       
          
#creation fonction pour afficher compte
    def afficherCompte(self):
        print("Compte Numéro:",self.numCompte)
        print("Nom Numéro:",self.nomCompte)
        print("Solde disponible:",self.solde)

    
#Fonction pour déposer de l'argent
    def depot(self,montant):

        if montant <= 0:
            print("Veuillez entrer un montant positif")
            return
        
        self.solde += montant
        print("Dépôt de", montant, "XAF effectué avec succès")
        self.afficheSolde()
    
    #creation fonction pour retrait argent
    def retrait(self,montant):
        if montant <= 0:
            print("Veuillez entrer un montant positif")
            return
        if (self.solde  <= 25000):
            print("solde insuffisant,ajoutez au minimum 25 000 fcfa")
            return
        if self.solde < montant:
            print("Solde insuffisant")
            return
        
        self.solde -=montant
        print("Retrait de", montant, "XAF effectué avec succès")
        self.afficheSolde()
    

    #creation fonction pour afficher solde

    def afficheSolde(self):
        print("Votre solde est de :",self.solde)

           
    #suppression du compte
    def suppCompte(self):
    
        print("le compte a été supprimé:")


    #Fonction pour sauvegarder le compte

    def listeCompte(self, fichier_comptes='Comptes.csv'):

        try:

            file_exists = os.path.isfile(fichier_comptes)

            with open(fichier_comptes, "a",newline='',encoding='utf-8') as f_out:
                fields = ["numCompte", "nomCompte","solde"]
                writer = csv.DictWriter(f_out, fieldnames=fields, delimiter="\t")
                if not file_exists:
                    writer.writeheader()
                          
                writer.writerow({
                    "numCompte": self.numCompte, 
                    "nomCompte":self.nomCompte,
                    "solde":self.solde

                    })
            print(f"Compte {self.numCompte} enregistré avec succès dans '{fichier_comptes}' .\n")
        except Exception as e:
            print(f"Erreur lors de l'enregistrement du compte : {e}\n")
    
#Gestion des comptes
class Banque:
    def __init__(self,fichier_comptes='Comptes.csv'):
        self.fichier_comptes = fichier_comptes
        self.comptes = self.chargerComptes()
        
    #charger comptes
    def chargerComptes(self):
        comptes = {}
        if not os.path.isfile(self.fichier_comptes):
            return comptes
        try:
            with open(self.fichier_comptes, "r",encoding='utf-8') as f_in:
                reader = csv.DictReader(f_in, delimiter="\t")
                for row in reader:
                    numCompte = int(row["numCompte"])
                    nomCompte = row["nomCompte"]
                    solde = float(row["solde"])
                    comptes[numCompte] = Compte(numCompte, nomCompte, solde)
            return comptes
        except Exception as e:
            print(f"Erreur lors du chargement des comptes : {e}")
            return comptes
        
    #sauvegarder comptes
    def sauvegarderComptes(self):
        try:
            with open(self.fichier_comptes, "w",newline='',encoding='utf-8') as f_out:
                fields = ["numCompte", "nomCompte","solde"]
                writer = csv.DictWriter(f_out, fieldnames=fields, delimiter="\t")
                writer.writeheader()
                for compte in self.comptes.values():
                    writer.writerow({
                        "numCompte": compte.numCompte, 
                        "nomCompte":compte.nomCompte,
                        "solde":compte.solde
                    })
            print(f"Comptes enregistrés avec succès dans '{self.fichier_comptes}' .\n")
        except Exception as e:
            print(f"Erreur lors de l'enregistrement des comptes : {e}\n")

    #Créer un nouveau compte
    def creerCompte(self):
        com= Compte()
        if com.creeCompte():
            if com.numCompte in self.comptes:
                print("Ce numero de compte existe déjà")
                return
            self.comptes[com.numCompte] = com
            com.listeCompte(self.fichier_comptes)

    #Effectuer un dépôt
    def depot(self):
        try:
            numCompte = int(input("Entrez le numero du compte : "))
            if numCompte not in self.comptes:
                print("Ce numero de compte n'existe pas")
                return
            montant = float(input("Entrez le montant à deposer : "))
            self.comptes[numCompte].depot(montant)
        except ValueError:
            print("Veuillez entrer un nombre valide. \n")

    #Effectuer un retrait
    def retrait(self):
        try:
            numCompte = int(input("Entrez le numero du compte : "))
            if numCompte not in self.comptes:
                print("Ce numero de compte n'existe pas")
                return
            montant = float(input("Entrez le montant à retirer : "))
            self.comptes[numCompte].retrait(montant)
        except ValueError:
            print("Veuillez entrer un nombre valide. \n")

    #Afficher solde
    def afficherSolde(self):
        try:
            numCompte = int(input("Entrez le numero du compte : "))
            if numCompte not in self.comptes:
                print("Ce numero de compte n'existe pas")
                return
            self.comptes[numCompte].afficheSolde()
        except ValueError:
            print("Veuillez entrer un nombre valide. \n")

    #Supprimer un compte
    def supprimerCompte(self):
        try:
            numCompte = int(input("Entrez le numero du compte : "))
            if numCompte in self.comptes:
                nomCompte = self.comptes[numCompte].nomCompte
                del self.comptes[numCompte]
                self.sauvegarderComptes()
                print(f"Compte {numCompte} {nomCompte} supprimé avec succès.\n")
            else:
                print("Ce numero de compte n'existe pas")
        
        except ValueError:
            print("Veuillez entrer un nombre valide. \n")

    #listing des comptes
    def listerComptes(self):
        if not self.comptes:
            print("Il n'y a aucun compte.\n")
            return
        print("----Liste des comptes:--------")
        for compte in self.comptes.values():
            compte.afficherCompte()
#Transactions

#def transactions(self):
   # print("self.comptes[numCompte].afficheSolde()")
    #print("del self.comptes[numCompte]")
    #print("self.comptes[numCompte].retrait(montant)")



    #Quitter l'application 
    def quitter(self):
        self.sauvegarderComptes()
        print("Merci d'avoir utilisé notre application. Au revoir!\n")
        exit()

    

#Menu
def main():
    banque=Banque()
    while True:
        print("___________________________________")
        print("1.Creer compte\n2.Depot\n3.Retrait\n4.Solde\n5.Supprimer compte\n6.listing\n7.Transactions\n8.Quitter")

        try:
            choix= int(input("Selectionner une operation "))
        except ValueError:
            print("Veuillez entrer un nombre valide entre 1 et 7. \n")
            continue
        
        #choix creation compte
        if (choix==1):
            banque.creerCompte()

        #choix Depot
        elif (choix==2):
            
            banque.depot()

        #choix retrait
        elif(choix==3):
            banque.retrait()

        #choix solde
        elif (choix==4):
            banque.afficherSolde()

            #choix suppression compte
        elif (choix==5):

            print("votre compte a été supprimé:")
            banque.supprimerCompte()

        elif (choix==6):

            banque.listerComptes()

        #choix transcactions

        #elif (choix==7):

           # banque.transactions(self)

        #else:
            print("R.A.S \n")

            #choix quitter
            
        elif (choix==7):

            banque.quitter()

    else:
        print("Choix INVALIDE !!! Veuillez entrer un nombre valide entre 1 et 8. \n")
if __name__ == "__main__":
    main()



