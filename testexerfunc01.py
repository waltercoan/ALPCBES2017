import unittest
import exerfunc01

class MyTestCase(unittest.TestCase):
    def test_passamparametro(self):
        exerfunc01.soma(2,1,5)
        self.assertTrue(True)
    def test_testaA(self):
        with self.assertRaises(Exception):
            exerfunc01.soma(1,1,5)
    def test_testaretorno1(self):
        retorno = exerfunc01.soma(2,1,5)
        self.assertEqual(retorno,6)


if __name__ == '__main__':
    unittest.main()
