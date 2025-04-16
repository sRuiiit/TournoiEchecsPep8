# models/joueur.py


class Joueur:
    def __init__(self, nom, prenom, dn, idn, classement, id_joueur):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = dn
        self.identifiant_national = idn
        self.classement = classement
        self.id_joueur = id_joueur

    def to_dict(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_naissance,
            "identifiant_national": self.identifiant_national,
            "classement": self.classement,
            "id_joueur": self.id_joueur,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["nom"],
            data["prenom"],
            data["date_naissance"],
            data["identifiant_national"],
            data["classement"],
            data["id_joueur"],
        )

    def __str__(self):
        a = f"{self.nom} {self.prenom} (Né(e) le {self.date_naissance}"
        b = f"Classement: {self.classement}, ID: {self.id_joueur})"
        return a+b


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
    date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
    identifiant = input("Identifiant national : ")
    classement = int(input("Classement : "))
    return nom, prenom, date_naissance, identifiant, classement


# controllers/controleur_joueur.py


class ControleurJoueur:
    def __init__(self, db):
        self.db = db

    def creer_joueur(self):
        nom, prenom, dn, identifiant, classement = obtenir_donnees_joueur()
        joueur = Joueur(nom, prenom, dn,
                        identifiant, classement, None)
        self.db.insert_player(joueur)
        print("Joueur créé avec succès.")

    def afficher_joueurs(self):
        joueurs = self.db.get_all_players()
        afficher_liste_joueurs(joueurs)
