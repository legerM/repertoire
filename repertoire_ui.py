import repertoire_action as action
from terminaltables import AsciiTable

def afficher_tableau(repertoire):
    tableau = [["nom", "numeros", "adresse"]]
    liste_contacts = (action.lister_contacts(repertoire))
    for contacts in liste_contacts:
        tableau.append([contacts["nom"], contacts["telephone"], contacts["adresse"]])
    print(AsciiTable(tableau).table)


def afficher_tout_les_contacts(repertoire):
    afficher_tableau(repertoire)


def supprimer_personne():
    name = input("\nquel contact voulez vous supprimer ?")
    if action.supprimer_personne(repertoire, name):
        print("le contact a été supprimer")
        afficher_tout_les_contacts(repertoire)
    else:
        print("Réessaye")


def ajouter_personne():
    nom = input("\nquel est le nom du contact ?")
    telephone = input("quel est le numero ?")
    adresse = input("quelle est l'adresse ?")
    added = action.ajouter_personne(repertoire, nom, telephone, adresse)
    if added:
        print("\nle contact à été ajouter")
        afficher_tout_les_contacts(repertoire)
    else:
        print("le contact existe déja")

def afficher_recherche(resultats_recherche):
    print(resultats_recherche)




def rechercher_personne():
    recherche = input("\nveuillez entrer le nom du contact :")
    resultats_recherche = action.recherche_personnes(repertoire, recherche)
    if resultats_recherche:
        afficher_recherche(resultats_recherche)
    else:
        print("aucun contact a ce nom")


while True:
    repertoire = action.get_rep()
    choix_utilisateur = input("\nPress L pour lister , A pour ajouter et S pour supprimer un contact ou R pour "
                              "rechercher un contact :").upper()

    if choix_utilisateur == "L":
        print("\nvoici les contacts")
        afficher_tout_les_contacts(repertoire)

    elif choix_utilisateur == "S":
        supprimer_personne()

    elif choix_utilisateur == "A":
        ajouter_personne()

    elif choix_utilisateur == "R":
        rechercher_personne()

    elif choix_utilisateur =="Q":
        break