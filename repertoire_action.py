

def supprimer_contact (repertoire, name):
    for i, contact in enumerate(repertoire):
        if contact["nom"] == name:
            repertoire.remove(contact)
            return True
    return False


def ajouter_contact (repertoire ,nom,numero,adresse):
    for contact in repertoire:
        if numero == contact["numero"]:
            return False
    repertoire.append({"nom" : nom,"numero":numero,"mail":adresse})
    return True


def recherche_contact (repertoire,recherche):
    resultats_recherche =[]
    for contact in repertoire:
        if recherche in contact["nom"]:
            resultats_recherche.append(contact)
    return resultats_recherche
