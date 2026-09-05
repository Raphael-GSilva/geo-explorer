import unittest
import sys
import os

# Avisa o Python onde procurar a pasta 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.comandos import carregar_trilhas

class TestGeoExplorer(unittest.TestCase):

    def test_carregar_json(self):
        trilhas = carregar_trilhas()
        self.assertIsInstance(trilhas, list)
        self.assertTrue(len(trilhas) > 0)
        print("✅ Teste aprovado: O banco de dados JSON foi lido com sucesso!")

if __name__ == '__main__':
    unittest.main()
