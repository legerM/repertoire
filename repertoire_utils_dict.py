repertoire = [ {"nom": "george", "telephone": "32514564", "adresse": "@"},
                {"nom": "bob", "telephone": "6", "adresse": "@"},
                {"nom": "gnu", "telephone": "5645654", "adresse": "@"}]

def get_rep():
    return repertoire


def append_rep(repertoire ,nom,telephone,adresse):
    repertoire.append({"nom" : nom,"telephone":telephone,"adresse":adresse})


def del_rep(repertoire, name):
    for i, contact in enumerate(repertoire):
        if contact["nom"] == name:
            repertoire.remove(contact)
            return True
    return False

def lister_tous_les_contacts(repertoire):
    tout_les_contact = []
    for contact in repertoire:
          tout_les_contact.append(contact)
    return tout_les_contact
