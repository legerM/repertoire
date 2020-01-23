import json

def get_rep():
    fichier = open("fichier.json","r")
    repertoire = json.loads(fichier.read())
    fichier.close()
    return repertoire



def append_rep(repertoire ,personne):
    repertoire.append(personne)
    with open("fichier.json", "w") as fichier:
        fichier.write(json.dumps(repertoire))


def del_rep(repertoire, personne):
    for contact in repertoire:
        if contact["nom"] == personne:
            repertoire.remove(contact)
        with open("fichier.json","w") as fichier:
            fichier.write(json.dumps(repertoire))


def lister_tous_les_contacts(repertoire):
    tout_les_contact = []
    for contact in repertoire:
          tout_les_contact.append(contact)
    return tout_les_contact




# repertoire = [{"nom": "george", "telephone": "32514564", "adresse": "@"},
#               {"nom": "bob", "telephone": "6", "adresse": "@"},
#               {"nom": "gnu", "telephone": "5645654", "adresse": "@"}]
# # prends le repertoire dans un fichier texte
# # ecris ou lis sur le fichier texte
# #
# fichier = open("fichier.json","a")
# fichier.write(json.dumps(repertoire))
# fichier.close()
# fichier=open("fichier.json","r")
# print (fichier.read())
# fichier.close()