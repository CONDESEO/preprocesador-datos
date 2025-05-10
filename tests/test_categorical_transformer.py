import unittest
import pandas as pd
import builtins
from modules import categorical_transformer as ct

class TestCategorizacion(unittest.TestCase):
    def test_label_encoding(self):
        df = pd.DataFrame({'Color': ['Rojo', 'Verde', 'Azul']})
        features = ['Color']
        # Simular entrada del usuario para elegir LabelEncoding
        original_input = builtins.input
        builtins.input = lambda _: "2"
        df_transformado, completado, cols = ct.transformar_datos_categoricos(df.copy(), features)
        builtins.input = original_input
        self.assertTrue(completado)
        self.assertTrue('Color' in df_transformado.columns)
        self.assertTrue(df_transformado['Color'].dtype in ['int32', 'int64'])
