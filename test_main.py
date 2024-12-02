import unittest
from main import ConnexionApp
from PyQt5.QtWidgets import QApplication
import sys
app = QApplication(sys.argv)


app = QApplication(sys.argv)


class TestConnexionApp(unittest.TestCase):
    def setUp(self):
        self.form = ConnexionApp()


    def test_champs_vides(self):
        # Test avec tous les champs vides
        self.form.lineEdit_identifiant.setText("")
        self.form.lineEdit_motDePasse.setText("")
        self.form.lineEdit_email.setText("")
        self.form.valider_formulaire()
        self.assertEqual(self.form.label_message.text(), "Erreur : veuillez remplir correctement tous les champs.")


    def test_email_invalide(self):
        # Test avec un email invalide
        self.form.lineEdit_identifiant.setText("testuser")
        self.form.lineEdit_motDePasse.setText("Password1!")
        self.form.lineEdit_email.setText("emailinvalide")
        self.form.valider_formulaire()
        self.assertEqual(self.form.label_message.text(), "Erreur : l'adresse e-mail n'est pas valide.")


    def test_mot_de_passe_faible(self):
        # Test avec un mot de passe faible
        self.form.lineEdit_identifiant.setText("testuser")
        self.form.lineEdit_motDePasse.setText("abc")
        self.form.lineEdit_email.setText("test@example.com")
        self.form.valider_formulaire()
        self.assertEqual(self.form.label_message.text(), "Le mot de passe doit contenir au moins 8 caractères.")


    def test_connexion_reussie(self):
        # Test avec toutes les informations correctes
        self.form.lineEdit_identifiant.setText("testuser")
        self.form.lineEdit_motDePasse.setText("Password1!")
        self.form.lineEdit_email.setText("test@example.com")
        self.form.valider_formulaire()
        self.assertEqual(self.form.label_message.text(), "Connexion réussie.")


if __name__ == "__main__":
    unittest.main()
