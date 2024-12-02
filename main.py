import sys
import re  # Importer re pour les expressions régulières
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface_connexion import Ui_Form  # Importer l'IHM


class ConnexionApp(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Connecter le bouton Valider à une fonction
        self.bouton_valider.clicked.connect(self.valider_formulaire)


    def valider_formulaire(self):
        # Récupérer les valeurs des champs de saisie
        identifiant = self.lineEdit_identifiant.text()
        mot_de_passe = self.lineEdit_motDePasse.text()
        email = self.lineEdit_email.text()


        # Vérifier si les champs sont correctement remplis
        if not identifiant or not mot_de_passe or '@' not in email:
            self.afficher_message("Erreur : veuillez remplir correctement tous les champs.")
            return


        # Analyser la robustesse du mot de passe
        resultat_analyse = self.analyser_mot_de_passe(mot_de_passe)
        if resultat_analyse != "Le mot de passe est robuste.":
            self.afficher_message(resultat_analyse)
            return


        # Si toutes les vérifications passent
        self.afficher_message("Connexion réussie.")


    def analyser_mot_de_passe(self, mot_de_passe):
        # Vérifier la longueur du mot de passe
        if len(mot_de_passe) < 8:
             self.afficher_message("Erreur : Mot de passe trop court")
             return "Erreur : Mot de passe trop court"
        else :
             self.afficher_message("Le mot de passe est robuste.")
             return "Le mot de passe est robuste."

    # Fonction pour afficher un message dans le QLabel
    def afficher_message(self, message):
        self.label_message.setText(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = ConnexionApp()
    fenetre.show()
    sys.exit(app.exec_())
