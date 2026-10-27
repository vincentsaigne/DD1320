import unittest

# Importera din funktion från din huvudfil (ersätt 'molekyl' med namnet på din Python-fil)
from labb9 import kontrollera_formel


class TestMolekylBNF(unittest.TestCase):

    def test_korrekta_formler(self):
        """Testar ett urval av korrekta molekylformler."""
        korrekta_exempel = [
            "H2",
            "P21",
            "Ag3",
            "Fe12",
            "H2O",
            "Si(C3H7)4",
            "Na3PO4",
            "Fe(CO)5",
        ]
        for formel in korrekta_exempel:
            with self.subTest(formel=formel):
                resultat = kontrollera_formel(formel)
                self.assertEqual(resultat, "Formeln är syntaktiskt korrekt")

    def test_felaktig_atom(self):
        """Testar atomer som inte finns i periodiska systemet eller har fel skiftläge."""
        # 'a' börjar inte med stor bokstav
        self.assertEqual(
            kontrollera_formel("a"), "Saknad stor bokstav vid radslutet a"
        )
        # 'Xx' finns inte i listan över godkända atomer
        self.assertEqual(
            kontrollera_formel("Xx5"), "Okänd atom vid radslutet 5"
        )

    def test_felaktiga_tal(self):
        """Testar för små tal (0 eller 1 ensamt)."""
        self.assertEqual(
            kontrollera_formel("Cr0"), "För litet tal vid radslutet "
        )
        self.assertEqual(
            kontrollera_formel("Pb1"), "För litet tal vid radslutet "
        )

    def test_parentesfel(self):
        """Testar felaktig hantering av parenteser."""
        # Saknad slutparentes
        self.assertEqual(
            kontrollera_formel("(H2O"), "Saknad högerparentes vid radslutet "
        )
        # Saknad siffras efter parentes
        self.assertEqual(
            kontrollera_formel("(H2O)"), "Saknad siffra vid radslutet "
        )


if __name__ == "__main__":
    unittest.main()