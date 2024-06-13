import os

# Chemin vers le fichier de contacts
FICHIER_CONTACTS = "contacts.txt"

def ajouter_contact(nom, telephone):
    with open(FICHIER_CONTACTS, "a") as fichier:
        fichier.write(f"{nom},{telephone}\n")
    print(f"Contact {nom} ajouté avec succès.")

def afficher_contacts():
    if os.path.exists(FICHIER_CONTACTS):
        with open(FICHIER_CONTACTS, "r") as fichier:
            contacts = fichier.readlines()
            if contacts:
                print("Liste des contacts :")
                for contact in contacts:
                    nom, telephone = contact.strip().split(",")
                    print(f"Nom : {nom}, Téléphone : {telephone}")
            else:
                print("Aucun contact trouvé.")
    else:
        print("Aucun contact trouvé.")

def rechercher_contact(nom_recherche):
    if os.path.exists(FICHIER_CONTACTS):
        with open(FICHIER_CONTACTS, "r") as fichier:
            contacts = fichier.readlines()
            for contact in contacts:
                nom, telephone = contact.strip().split(",")
                if nom.lower() == nom_recherche.lower():
                    print(f"Contact trouvé : Nom : {nom}, Téléphone : {telephone}")
                    return
            print("Contact non trouvé.")
    else:
        print("Aucun contact trouvé.")

def mettre_a_jour_contact(nom_recherche, nouveau_nom, nouveau_telephone):
    if os.path.exists(FICHIER_CONTACTS):
        with open(FICHIER_CONTACTS, "r") as fichier:
            contacts = fichier.readlines()

        with open(FICHIER_CONTACTS, "w") as fichier:
            contact_trouve = False
            for contact in contacts:
                nom, telephone = contact.strip().split(",")
                if nom.lower() == nom_recherche.lower():
                    fichier.write(f"{nouveau_nom},{nouveau_telephone}\n")
                    contact_trouve = True
                    print(f"Contact {nom_recherche} mis à jour avec succès.")
                else:
                    fichier.write(contact)

            if not contact_trouve:
                print("Contact non trouvé.")
    else:
        print("Aucun contact trouvé.")

def menu():
    while True:
        print("\nGestionnaire de Contacts")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Mettre à jour un contact")
        print("5. Quitter")

        choix = input("Choisissez une option (1-5) : ")

        if choix == "1":
            nom = input("Entrez le nom du contact : ")
            telephone = input("Entrez le numéro de téléphone du contact : ")
            ajouter_contact(nom, telephone)
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            nom_recherche = input("Entrez le nom du contact à rechercher : ")
            rechercher_contact(nom_recherche)
        elif choix == "4":
            nom_recherche = input("Entrez le nom du contact à mettre à jour : ")
            nouveau_nom = input("Entrez le nouveau nom : ")
            nouveau_telephone = input("Entrez le nouveau numéro de téléphone : ")
            mettre_a_jour_contact(nom_recherche, nouveau_nom, nouveau_telephone)
        elif choix == "5":
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu()