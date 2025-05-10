import unittest
import pandas as pd
import builtins
from modules import normalization_scaling as ns

class TestNormalizacion(unittest.TestCase):
    def test_minmax_scaling(self):
        df = pd.DataFrame({'Ingreso': [100, 200, 300], 'Binaria': [0, 1, 1]})
        features = ['Ingreso', 'Binaria']
        columnas_a_ignorar = []
        # Simular Min-Max Scaling
        original_input = builtins.input
        builtins.input = lambda _: "1"
        df_result, ok = ns.normalizar_escalar_datos(df.copy(), features, columnas_a_ignorar)
        builtins.input = original_input
        self.assertTrue(ok)
        self.assertTrue(df_result['Ingreso'].max() <= 1.0)
