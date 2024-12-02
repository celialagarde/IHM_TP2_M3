import sys
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


        # Si toutes les vérifications passent
        self.afficher_message("Connexion réussie.")


    # Fonction pour afficher un message dans le QLabel
    def afficher_message(self, message):
        self.label_message.setText(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = ConnexionApp()
    fenetre.show()
    sys.exit(app.exec_())
