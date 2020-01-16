repertoire = {"george": "156456456", "bob": "54564564"}

# fonction qui affiche mon repertoire


def afficher_repertoire (repertoire):
    print(repertoire)

# fonction qui supprime le contact de l'input delete_contact


def supprimer_contact (repertoire,delete_contact):
    saisie_utilisateur=delete_contact
    if saisie_utilisateur in repertoire :
        del repertoire[saisie_utilisateur]

# fonction qui ajoute un contact


def ajouter_contact (repertoire ,nom,numero):
    repertoire[nom] = numero

# fonction qui recherche un contact le stocke dans un nouveau dico  grace a ma premiere fonction ajouter contact ,
# au cas ou il y a  plusieurs contact du meme nom et qui retourne la valeur de la recherche


def recherche_contact (repertoire,recherche):
    resultats_recherche ={}
    for key,value in repertoire.items():
        if recherche==key:
            ajouter_contact(resultats_recherche,key,value)
    return resultats_recherche

# ma boucle infini qui sert de menu pour l'utilisateur


while True:
    choix_utilisateur = input("Press L pour lister , A pour ajouter et S pour supprimer un contact ou R pour rechercher un contact :").upper()

    if choix_utilisateur == "L":
        print("voici les contacts")
        afficher_repertoire(repertoire)

    elif choix_utilisateur == "S":
        delete_contact=input("quel contact voulez vous supprimer ?").upper()
        supprimer_contact(repertoire)
        print("le contact a été supprimer")

    elif choix_utilisateur == "A":
        nom=input("quel est le nom du contact ?").upper()
        numero=input("quel est le numero ?")
        ajouter_contact(repertoire, nom, numero)
        print("le contact à été ajouter")

# la recherche de contact qui utilise plusieur fonctions , la recherche du contact , et l'afichage du repertoire
    elif choix_utilisateur == "R":
        recherche = input("veuillez entrer le nom du contact :").upper()
        resultats_recherche= recherche_contact(repertoire, recherche)
        afficher_repertoire(resultats_recherche)






