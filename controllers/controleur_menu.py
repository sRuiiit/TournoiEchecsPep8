# controllers/controleur_menu.py

class ControleurMenu:
    def __init__(self, controleur_joueur, controleur_tournoi):
        self.controleur_joueur = controleur_joueur
        self.controleur_tournoi = controleur_tournoi
        self.tournoi_actuel = None

    def afficher_menu_principal(self):
        while True:
            print("\nMenu Principal")
            print("1. Gérer les joueurs")
            print("2. Créer un nouveau tournoi")
            print("3. Charger un tournoi existant")
            print("4. Afficher le plan du tournoi")
            print("5. Gérer le round (créer ou continuer)")
            print("6. Afficher le récapitulatif du tournoi")
            print("7. Quitter")

            choix = input("Choisissez une option : ")

            if choix == "1":
                self.menu_joueurs()
            elif choix == "2":
                self.tournoi_actuel = self.controleur_tournoi.creer_tournoi()
            elif choix == "3":
                a1 = self.controleur_tournoi.selectionner_tournoi()
                self.tournoi_actuel = a1
            elif choix == "4":
                if self.tournoi_actuel:
                    self.controleur_tournoi.afficher_plan_tournoi(
                        self.tournoi_actuel)
                else:
                    print("⚠️ Aucun tournoi chargé.")
            elif choix == "5":
                if self.tournoi_actuel:
                    self.controleur_tournoi.gerer_round(self.tournoi_actuel)
                else:
                    aa = "⚠️ Aucun tournoi chargé."
                    ab = "Veuillez en créer ou en charger un d'abord."
                    print(aa+" "+ab)
            elif choix == "6":
                if self.tournoi_actuel:
                    self.controleur_tournoi.afficher_recapitulatif(
                        self.tournoi_actuel)
                else:
                    print("⚠️ Aucun tournoi chargé.")
            elif choix == "7":
                print("Au revoir !")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    def menu_joueurs(self):
        while True:
            print("\n--- GESTION DES JOUEURS ---")
            print("1. Ajouter un joueur")
            print("2. Afficher les joueurs")
            print("3. Retour")

            choix = input("Votre choix : ")

            if choix == "1":
                self.controleur_joueur.creer_joueur()
            elif choix == "2":
                self.controleur_joueur.afficher_joueurs()
            elif choix == "3":
                break
            else:
                print("Choix invalide.")

    def menu_tournois(self):
        while True:
            print("\n--- GESTION DES TOURNOIS ---")
            print("1. Créer un tournoi")
            print("2. Afficher les tournois")
            print("3. Démarrer le premier tour")
            print("4. Générer le tour suivant")
            print("5. Voir les joueurs d’un tournoi")
            print("6. Voir le plan du tournoi")
            print("7. Retour")

            choix = input("Votre choix : ")

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
                print("Choix invalide.")
