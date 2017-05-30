import unittest
from Complejos import Complejo


class TestComplejos(unittest.TestCase):
    def test_sumar(self):
        n1 = Complejo(4, 4)
        n2 = Complejo(2, 2)
        n_res = Complejo(6, 6)

        self.assertEqual(n1.sumar(n2), n_res)

    def test_restar(self):
        n1 = Complejo(4, 4)
        n2 = Complejo(2, 2)
        n_res = Complejo(2, 2)

        self.assertEqual(n1.restar(n2).__str__, n_res.__str__)

    def test_multiplicar(self):
        n1 = Complejo(4, 4)
        n2 = Complejo(2, 2)
        n_res = Complejo(0, 16)
        self.assertEqual(n1.multiplicar(n2), n_res)

    def test_prueba(self):
    	self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
