# controllers/controleur_joueur.py

from models.joueur import Joueur
from views.vue_joueur import afficher_liste_joueurs
from views.vue_joueur import obtenir_donnees_joueur as odj
from views.vue_joueur import afficher_confirmation_creation_joueur  # Import de la nouvelle fonction


class ControleurJoueur:
    def __init__(self, db):
        self.db = db

    def creer_joueur(self):
        nom, prenom, identifiant, classement, date_naissance = odj()
        joueur = Joueur(nom, prenom, identifiant, classement,
                        id_joueur=None, date_naissance=date_naissance)
        self.db.insert_player(joueur)
        afficher_confirmation_creation_joueur()  # Utilisation de la fonction de la vue

    def afficher_joueurs(self):
        joueurs = self.db.get_all_players()
        afficher_liste_joueurs(joueurs)