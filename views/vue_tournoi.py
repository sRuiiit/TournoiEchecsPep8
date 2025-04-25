# Nouveau fichier vue_tournoi.py
from models.utils import calcul_scores

def afficher_message(message):
    print(message)

def afficher_titre(message):
    print("\n" + message)

def afficher_ligne_separation():
    print("-------------------------------------------")

def afficher_liste_joueurs(joueurs):
    for i, joueur in enumerate(joueurs, 1):
        print(f"[{i}] {joueur.nom} {joueur.prenom} (ID: {joueur.id_joueur})")

def afficher_liste_tournois(tournois):
    print("\n📋 Tournois disponibles :")
    for i, tournoi in enumerate(tournois):
        print(f"[{i+1}] {tournoi.nom} ({tournoi.date_debut}→{tournoi.date_fin})")

def afficher_erreur_pas_de_joueurs():
    print("\n⛔ Enregistrer des joueurs avant de créer un tournoi.")

def afficher_erreur_selection_joueur(e):
    print(f"⚠️ Erreur lors de la sélection des joueurs : {e}")

def afficher_erreur_pas_assez_de_joueurs():
    print("⚠️ Il faut au moins 2 joueurs pour créer un tournoi.")

def afficher_confirmation_creation_tournoi(nom, nb_joueurs):
    print(f"✅ Tournoi '{nom}' créé avec {nb_joueurs} joueurs")

def demander_selection_joueurs():
    print("Entrez les numéros des joueurs à ajouter au tournoi")
    print("séparés par des virgules, ex: 1,3,5):")
    return input("> ")

def obtenir_donnees_tournoi():
    print("\nCréation d'un nouveau tournoi :")
    nom = input("Nom du tournoi : ")
    lieu = input("Lieu du tournoi : ")
    date_debut = input("Date de début (YYYY-MM-DD) : ")
    date_fin = input("Date de fin (YYYY-MM-DD) : ")
    description = input("Description du tournoi : ")
    nb_tours = input("Nombre de tours (par défaut 4) : ") or "4"
    return nom, lieu, date_debut, date_fin, nb_tours, description

def afficher_erreur_aucun_tournoi():
    print("Aucun tournoi disponible.")

def demander_selection_tournoi():
    return input("Sélectionnez un tournoi par son numéro : ")

def afficher_numero_invalide():
    print("Numéro invalide. Réessayez.")

def afficher_entree_non_valide():
    print("Entrée non valide. Entrez un nombre.")

def afficher_plan_tournoi(tournoi):
    print(f"\n📅 Plan du tournoi : {tournoi.nom}")
    afficher_ligne_separation()
    if not tournoi.tours:
        print("Aucun round encore généré pour ce tournoi.")
        return
    for i, tour in enumerate(tournoi.tours, 1):
        print(f"Round {i} :")
        for match in tour.liste_matchs:
            if match.joueur2.nom == "BYE":
                print(f" - {match.joueur1.nom} (joue seul - BYE)")
            else:
                if match.resultat:
                    print(f"- {match.joueur1.nom} vs {match.joueur2.nom}")
                    print(f"[{match.resultat[0]} - {match.resultat[1]}]")
                else:
                    print(f"- {match.joueur1.nom} vs {match.joueur2.nom} (à jouer)")
        print()

def demander_resultat_match(j1, j2):
    while True:
        print(f"\nMatch : {j1.nom} vs {j2.nom}")
        print("Qui a gagné ?")
        print(f"1. {j1.nom}")
        print(f"2. {j2.nom}")
        print("3. Match nul")
        choix = input("> ").strip()
        if choix in ["1", "2", "3"]:
            return choix
        print("⛔ Choix invalide. Veuillez taper 1, 2 ou 3.")

def afficher_matchs_a_venir(matchs):
    print("\n📋 Matchs du round à venir :")
    afficher_ligne_separation()
    for i, match in enumerate(matchs, 1):
        if match.joueur2.nom == "BYE":
            print(f"{i}. {match.joueur1.nom} (joue seul - BYE)")
        else:
            print(f"{i}. {match.joueur1.nom} vs {match.joueur2.nom}")
    afficher_ligne_separation()

def afficher_fin_round(nom_round):
    print(f"\n✅ {nom_round} terminé.")
    print("💾 Sauvegarde automatique du tournoi effectuée.")

def afficher_erreur_aucun_joueur_dans_tournoi():
    print("Ce tournoi ne contient aucun joueur.")

def afficher_joueurs_du_tournoi(tournoi):
    print(f"\n👥 Joueurs du tournoi '{tournoi.nom}' :")
    for joueur in sorted(tournoi.joueurs, key=lambda j: j.nom):
        print(f"- {joueur.nom} {joueur.prenom} (ID: {joueur.id_joueur})")
        print(f"Classement: {joueur.classement}")

def afficher_details_tournoi(tournoi):
    print(f"\n🏆 Détails du tournoi : {tournoi.nom}")
    print(f"Lieu : {tournoi.lieu}")
    print(f"Dates : {tournoi.date_debut} → {tournoi.date_fin}")
    print(f"Nombre de tours : {tournoi.nb_tours}")
    print(f"Description : {tournoi.description}")

def afficher_recapitulatif_tournoi(tournoi):
    print(f"\nRécapitulatif du tournoi : {tournoi.nom}")
    print(f"Durée : {tournoi.date_debut} → {tournoi.date_fin}")
    print(f"Nombre de tours : {tournoi.nb_tours}")
    print(f"Description : {tournoi.description}")
    scores = calcul_scores(tournoi)
    print("\nJoueurs inscrits :")
    print("------------------------------------------------------------------")
    print(f"{'Nom':<20}{'Prénom':<20}{'Score total':<15}")
    print("------------------------------------------------------------------")
    for joueur in tournoi.joueurs:
        a = f"{joueur.nom:<20}{joueur.prenom:<20}"
        b = f"{scores.get(joueur.id_joueur, 0):<15}"
        print(a + b)
    print("\nRésultats des tours :")
    print("------------------------------------------------------------------")
    aa = f"{'Tour':<10}{'Joueur 1':<20}{'Joueur 2':<20}"
    ab = f"{'Score Joueur 1':<20}{'Score Joueur 2':<20}"
    print(aa + ab)
    print("------------------------------------------------------------------")
    c = "Non joué"
    for tour in tournoi.tours:
        for match in tour.liste_matchs:
            score1 = match.resultat[0] if match.resultat is not None else c
            score2 = match.resultat[1] if match.resultat is not None else c
            a2 = f"{tour.nom:<10}{match.joueur1.nom:<20}"
            b2 = f"{match.joueur2.nom:<20}{str(score1):<20}{str(score2):<20}"
            print(a2 + b2)
    print("\nClassement final :")
    print("------------------------------------------------------------------")
    print(f"{'Nom':<20}{'Prénom':<20}{'Score final':<15}")
    print("------------------------------------------------------------------")
    classement = sorted(tournoi.joueurs, key=lambda j: scores.get(j.id_joueur, 0), reverse=True)
    for joueur in classement:
        a3 = f"{joueur.nom:<20}{joueur.prenom:<20}"
        b3 = f"{scores.get(joueur.id_joueur, 0):<15}"
        print(a3 + b3)
