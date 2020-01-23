import repertoire_utils_dict as repertoire_utils
import repertoire_utils_text as repertoire_utils
# import repertoire_utils_text_jl as repertoire_utils

def get_rep():
    return repertoire_utils.get_rep()


def supprimer_personne (repertoire, name):
    for i, contact in enumerate(repertoire_utils.lister_tous_les_contacts(repertoire)):
        if contact["nom"] == name:
            repertoire_utils.del_rep(repertoire, name)
            return True
    return False


def ajouter_personne (repertoire ,nom,telephone,adresse):
    for contact in repertoire_utils.lister_tous_les_contacts(repertoire):
        if telephone == contact["telephone"]:
            return False
    repertoire_utils.append_rep(repertoire,({"nom" : nom,"telephone":telephone,"adresse":adresse}))
    return True


def recherche_personnes (repertoire,recherche):
    resultats_recherche =[]
    for contact in repertoire_utils.lister_tous_les_contacts(repertoire):
        if recherche in contact["nom"]:
            resultats_recherche.append(contact)
    return resultats_recherche


def lister_contacts(repertoire):
    return repertoire_utils.lister_tous_les_contacts(repertoire)
