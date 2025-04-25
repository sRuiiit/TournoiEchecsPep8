# Nouveau fichier controleur_tournoi.py
from models.tournoi import Tournoi
from models.joueur import Joueur
from models.match import Match
from models.tour import Tour
from views.vue_tournoi import (
    obtenir_donnees_tournoi,
    afficher_message,
    afficher_liste_tournois,
    afficher_liste_joueurs,
    afficher_recapitulatif_tournoi,
    afficher_erreur_pas_de_joueurs,
    afficher_erreur_selection_joueur,
    afficher_erreur_pas_assez_de_joueurs,
    afficher_confirmation_creation_tournoi,
    demander_selection_joueurs,
    afficher_erreur_aucun_tournoi,
    demander_selection_tournoi,
    afficher_numero_invalide,
    afficher_entree_non_valide,
    afficher_plan_tournoi,
    demander_resultat_match,
    afficher_matchs_a_venir,
    afficher_fin_round,
    afficher_erreur_aucun_joueur_dans_tournoi,
    afficher_joueurs_du_tournoi
)
from collections import defaultdict
from datetime import datetime


class ControleurTournoi:
    def __init__(self, db):
        self.db = db

    def afficher_recapitulatif(self, tournoi):
        afficher_recapitulatif_tournoi(tournoi)

    def creer_tournoi(self):
        joueurs_disponibles = self.db.get_all_players()
        if not joueurs_disponibles:
            afficher_erreur_pas_de_joueurs()
            return None

        nom, lieu, date_debut, date_fin, nb_tours, description = obtenir_donnees_tournoi()
        nb_tours = int(nb_tours) if nb_tours.isdigit() else 4

        afficher_message("\nVoici les joueurs disponibles :")
        afficher_liste_joueurs(joueurs_disponibles)

        joueurs_selectionnes = []
        saisie = demander_selection_joueurs()
        try:
            indexes = [int(i.strip()) - 1 for i in saisie.split(",") if i.strip().isdigit()]
            for idx in indexes:
                if 0 <= idx < len(joueurs_disponibles):
                    joueurs_selectionnes.append(joueurs_disponibles[idx])
        except Exception as e:
            afficher_erreur_selection_joueur(e)
            return None

        if len(joueurs_selectionnes) < 2:
            afficher_erreur_pas_assez_de_joueurs()
            return None

        tournoi = Tournoi(
            nom=nom,
            lieu=lieu,
            date_debut=date_debut,
            date_fin=date_fin,
            joueurs=joueurs_selectionnes,
            tours=[],
            id_tournoi=None,
            nb_tours=nb_tours,
            tour_actuel=0,
            description=description
        )

        self.db.insert_tournament(tournoi)
        afficher_confirmation_creation_tournoi(nom, len(joueurs_selectionnes))
        return tournoi

    def selectionner_tournoi(self):
        tournois = self.db.get_all_tournaments()
        if not tournois:
            afficher_erreur_aucun_tournoi()
            return None

        afficher_liste_tournois(tournois)

        while True:
            try:
                choix = int(demander_selection_tournoi())
                if 1 <= choix <= len(tournois):
                    return tournois[choix - 1]
                else:
                    afficher_numero_invalide()
            except ValueError:
                afficher_entree_non_valide()

    def afficher_plan_tournoi(self, tournoi):
        afficher_plan_tournoi(tournoi)

    def demander_resultat_match(self, joueur1, joueur2):
        while True:
            choix = demander_resultat_match(joueur1, joueur2)
            if choix == "1":
                return (1.0, 0.0)
            elif choix == "2":
                return (0.0, 1.0)
            elif choix == "3":
                return (0.5, 0.5)

    def historique_matchs(self, tournoi):
        rencontres = set()
        for tour in tournoi.tours:
            for match in tour.liste_matchs:
                id1 = match.joueur1.id_joueur
                id2 = match.joueur2.id_joueur
                if id1 > id2:
                    id1, id2 = id2, id1
                rencontres.add((id1, id2))
        return rencontres

    def gerer_round(self, tournoi):
        numero_tour = len(tournoi.tours) + 1

        if numero_tour > int(tournoi.nb_tours):
            afficher_message("✅ Tous les tours ont déjà été joués.")
            return

        nom_round = f"Round {numero_tour}"
        date_debut = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nouveau_tour = Tour(nom_round, date_debut)

        afficher_message(f"\n🎯 Création de {nom_round}...")

        scores = self.calcul_scores(tournoi)
        joueurs = sorted(tournoi.joueurs, key=lambda j: scores.get(j.id_joueur, 0), reverse=True)
        rencontres_existantes = self.historique_matchs(tournoi)

        appariements = []
        deja_paires = set()
        i = 0

        while i < len(joueurs) - 1:
            joueur1 = joueurs[i]
            for j in range(i + 1, len(joueurs)):
                joueur2 = joueurs[j]
                paire = tuple(sorted([joueur1.id_joueur, joueur2.id_joueur]))
                if paire not in rencontres_existantes and joueur2.id_joueur not in deja_paires:
                    appariements.append((joueur1, joueur2))
                    deja_paires.update([joueur1.id_joueur, joueur2.id_joueur])
                    break
            i += 1

        joueurs_paires = set(j.id_joueur for p in appariements for j in p)
        joueur_solo = next((j for j in joueurs if j.id_joueur not in joueurs_paires), None)
        matchs = [Match(j1, j2) for j1, j2 in appariements]

        if joueur_solo:
            joueur_bye = Joueur("BYE", "", "", 0, -1)
            match_bye = Match(joueur_solo, joueur_bye)
            match_bye.resultat = (1.0, 0.0)
            matchs.append(match_bye)

        nouveau_tour.liste_matchs = matchs

        afficher_matchs_a_venir(matchs)
        afficher_message("\n📝 Saisie des résultats :")

        for match in matchs:
            if match.joueur2.nom != "BYE":
                match.resultat = self.demander_resultat_match(match.joueur1, match.joueur2)

        nouveau_tour.date_heure_fin = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tournoi.tours.append(nouveau_tour)
        self.db.update_tournament(tournoi)
        afficher_fin_round(nom_round)

    def afficher_tournois(self):
        tournois = self.db.get_all_tournaments()
        if not tournois:
            afficher_erreur_aucun_tournoi()
            return
        afficher_liste_tournois(tournois)

    def calcul_scores(self, tournoi):
        scores = defaultdict(float)
        for tour in tournoi.tours:
            for match in tour.liste_matchs:
                if match.resultat:
                    scores[match.joueur1.id_joueur] += match.resultat[0]
                    scores[match.joueur2.id_joueur] += match.resultat[1]
        return scores

    def afficher_joueurs_dun_tournoi(self):
        tournoi = self.selectionner_tournoi()
        if not tournoi:
            return

        if not tournoi.joueurs:
            afficher_erreur_aucun_joueur_dans_tournoi()
            return

        afficher_joueurs_du_tournoi(tournoi)