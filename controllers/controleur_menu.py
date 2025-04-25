# Nouveau fichier controleur_menu.py

from views.vue_tournoi import (
    afficher_message,
    afficher_titre,
    demander_selection_menu,
    demander_selection_menu_joueurs,
    demander_selection_menu_tournois,
    afficher_au_revoir,
    afficher_aucun_tournoi_charge,
    afficher_choix_invalide
)

class ControleurMenu:
    def __init__(self, controleur_joueur, controleur_tournoi):
        self.controleur_joueur = controleur_joueur
        self.controleur_tournoi = controleur_tournoi
        self.tournoi_actuel = None

    def afficher_menu_principal(self):
        while True:
            afficher_titre("Menu Principal")
            afficher_message("1. Gérer les joueurs")
            afficher_message("2. Créer un nouveau tournoi")
            afficher_message("3. Charger un tournoi existant")
            afficher_message("4. Afficher le plan du tournoi")
            afficher_message("5. Gérer le round (créer ou continuer)")
            afficher_message("6. Afficher le récapitulatif du tournoi")
            afficher_message("7. Quitter")

            choix = demander_selection_menu()

            if choix == "1":
                self.menu_joueurs()
            elif choix == "2":
                self.tournoi_actuel = self.controleur_tournoi.creer_tournoi()
            elif choix == "3":
                self.tournoi_actuel = self.controleur_tournoi.selectionner_tournoi()
            elif choix == "4":
                if self.tournoi_actuel:
                    self.controleur_tournoi.afficher_plan_tournoi(self.tournoi_actuel)
                else:
                    afficher_aucun_tournoi_charge()
            elif choix == "5":
                if self.tournoi_actuel:
                    self.controleur_tournoi.gerer_round(self.tournoi_actuel)
                else:
                    afficher_aucun_tournoi_charge()
            elif choix == "6":
                if self.tournoi_actuel:
                    self.controleur_tournoi.afficher_recapitulatif(self.tournoi_actuel)
                else:
                    afficher_aucun_tournoi_charge()
            elif choix == "7":
                afficher_au_revoir()
                break
            else:
                afficher_choix_invalide()

    def menu_joueurs(self):
        while True:
            afficher_titre("--- GESTION DES JOUEURS ---")
            afficher_message("1. Ajouter un joueur")
            afficher_message("2. Afficher les joueurs")
            afficher_message("3. Retour")

            choix = demander_selection_menu_joueurs()

            if choix == "1":
                self.controleur_joueur.creer_joueur()
            elif choix == "2":
                self.controleur_joueur.afficher_joueurs()
            elif choix == "3":
                break
            else:
                afficher_choix_invalide()

    def menu_tournois(self):
        while True:
            afficher_titre("--- GESTION DES TOURNOIS ---")
            afficher_message("1. Créer un tournoi")
            afficher_message("2. Afficher les tournois")
            afficher_message("3. Démarrer le premier tour")
            afficher_message("4. Générer le tour suivant")
            afficher_message("5. Voir les joueurs d’un tournoi")
            afficher_message("6. Voir le plan du tournoi")
            afficher_message("7. Retour")

            choix = demander_selection_menu_tournois()

            if choix == "1":
                self.controleur_tournoi.creer_tournoi()
            elif choix == "2":
                self.controleur_tournoi.afficher_tournois()
            elif choix == "3":
                tournoi = self.controleur_tournoi.selectionner_tournoi()
                if tournoi:
                    self.controleur_tournoi.demarrer_premier_tour(tournoi)
            elif choix == "4":
                tournoi = self.controleur_tournoi.selectionner_tournoi()
                if tournoi:
                    self.controleur_tournoi.demarrer_tour_suivant(tournoi)
                    self.controleur_tournoi.saisir_resultats_tour(tournoi)
            elif choix == "5":
                self.controleur_tournoi.afficher_joueurs_dun_tournoi()
            elif choix == "6":
                tournoi = self.controleur_tournoi.selectionner_tournoi()
                if tournoi:
                    self.controleur_tournoi.afficher_plan_tournoi(tournoi)
            elif choix == "7":
                break
            else:
                afficher_choix_invalide()
