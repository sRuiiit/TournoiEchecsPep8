# views/vue_joueur.py

def afficher_joueur(joueur):
    print(joueur)


def afficher_liste_joueurs(joueurs):
    print("\nListe des joueurs :")
    for i, joueur in enumerate(joueurs, 1):
        print(f"{i}. {joueur.nom} {joueur.prenom} "
              f"(ID: {joueur.id_joueur}, Classement: {joueur.classement}, "
              f"Né(e) le:{getattr(joueur, 'date_naissance', 'Non indiqué')})")




def obtenir_donnees_joueur():
    print("\nCréation d'un nouveau joueur :")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    identifiant = input("Identifiant national : ")
    classement = input("Classement : ")
    date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
    return nom, prenom, identifiant, classement, date_naissance  # Correct ordre





'''def obtenir_donnees_joueur():
    print("\nCréation d'un nouveau joueur :")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
    identifiant = input("Identifiant national : ")
    classement = int(input("Classement : "))
    return nom, prenom, date_naissance, identifiant, classement'''