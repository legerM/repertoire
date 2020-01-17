from repertoire_action import *

repertoire = [ {"nom": "george", "numero": "32514564", "mail": "@"},
                {"nom": "bob", "numero": "6", "mail": "@"},
                {"nom": "gnu", "numero": "5645654", "mail": "@"}]




def afficher_repertoire (repertoire):
    print(repertoire)



while True:
    choix_utilisateur = input("\nPress L pour lister , A pour ajouter et S pour supprimer un contact ou R pour rechercher un contact :").upper()

    if choix_utilisateur == "L":
        print("\nvoici les contacts")
        afficher_repertoire(repertoire)

    elif choix_utilisateur == "S":
        name=input("\nquel contact voulez vous supprimer ?")
        if supprimer_contact(repertoire, name):
            print("le contact a été supprimer")
        else:
            print("Réessaye")

    elif choix_utilisateur == "A":
        nom = input("\nquel est le nom du contact ?")
        numero = input("quel est le numero ?")
        adresse = input("quelle est l'adresse ?")
        added=ajouter_contact(repertoire, nom, numero, adresse)
        if added :
            print("\nle contact à été ajouter")
        else:
            print("le contact existe déja")




# la recherche de contact qui utilise plusieur fonctions , la recherche du contact , et l'afichage du repertoire
    elif choix_utilisateur == "R":
        recherche = input("\nveuillez entrer le nom du contact :")
        resultats_recherche= recherche_contact(repertoire, recherche)
        if resultats_recherche:
            afficher_repertoire(resultats_recherche)
        else :
            print("aucun contact a ce nom")






