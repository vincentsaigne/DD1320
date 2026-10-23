import unittest

from labb8 import LinkedQ, Syntaxfel, LETTER, letter, num


class TestMolekylSyntax(unittest.TestCase):

    def test_syntaxfel_ar_exception(self):
        self.assertTrue(issubclass(Syntaxfel, Exception))

    def test_LETTER_giltig_bokstav(self):
        q = LinkedQ()
        q.enqueue("H")
        try:
            LETTER(q)
        except Syntaxfel:
            self.fail("LETTER(q) kastade fel för en giltig stor bokstav 'H'.")

    def test_LETTER_ogiltig_bokstav(self):
        q = LinkedQ()
        q.enqueue("h")
        with self.assertRaises(Syntaxfel):
            LETTER(q)

    def test_letter_giltig_liten(self):
        q = LinkedQ()
        q.enqueue("x")
        try:
            letter(q)
        except Syntaxfel:
            self.fail("letter(q) kastade fel för en giltig liten bokstav 'x'.")

    def test_num_giltigt_tal(self):
        q = LinkedQ()
        q.enqueue("1")
        q.enqueue("2")
        try:
            num(q)
        except Syntaxfel:
            self.fail("num(q) kastade fel för en giltig siffra '12'.")

    def test_num_for_litet_tal(self):
        q = LinkedQ()
        q.enqueue("0")
        with self.assertRaises(Syntaxfel):
            num(q)


if __name__ == "__main__":
    unittest.main()