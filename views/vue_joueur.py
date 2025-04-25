import re
from datetime import datetime

def afficher_confirmation_creation_joueur():
    print("✅ Joueur ajouté avec succès.")

def valider_identifiant_national(identifiant):
    """Valide l'identifiant national selon le format 'ID12345'"""
    pattern = r'^[A-Z]{2}[0-9]{5}$'
    if re.match(pattern, identifiant):
        return True
    else:
        print("Erreur : L'identifiant national doit être au format 'ID12345' (deux lettres majuscules + cinq chiffres).")
        return False

def valider_date_naissance(date_naissance):
    """Valide la date de naissance au format 'YYYY-MM-DD'"""
    try:
        datetime.strptime(date_naissance, '%Y-%m-%d')
        return True
    except ValueError:
        print("Erreur : La date de naissance doit être au format 'YYYY-MM-DD'.")
        return False

def afficher_joueur(joueur):
    """Affiche les informations d'un joueur"""
    print(f"{joueur.nom} {joueur.prenom} (Identifiant National: {joueur.identifiant_national}, "
          f"Classement: {joueur.classement}, Né(e) le: {joueur.date_naissance})")

def afficher_liste_joueurs(joueurs):
    """Affiche la liste de tous les joueurs"""
    print("\nListe des joueurs :")
    for i, joueur in enumerate(joueurs, 1):
        afficher_joueur(joueur)

def obtenir_donnees_joueur():
    """Demande à l'utilisateur de saisir les données d'un joueur avec validation"""
    print("\nCréation d'un nouveau joueur :")
    nom = input("Nom : ")
    prenom = input("Prénom : ")

    # Validation de l'identifiant national
    while True:
        identifiant = input("Identifiant national : ")
        if valider_identifiant_national(identifiant):
            break  # Sortie de la boucle si l'identifiant est valide

    classement = input("Classement : ")

    # Validation de la date de naissance
    while True:
        date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
        if valider_date_naissance(date_naissance):
            break  # Sortie de la boucle si la date est valide

    return nom, prenom, identifiant, classement, date_naissance