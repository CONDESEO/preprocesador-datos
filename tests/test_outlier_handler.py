import unittest
import pandas as pd
import builtins
from modules import outlier_handler as oh

class TestOutliers(unittest.TestCase):
    def test_eliminacion_outliers(self):
        df = pd.DataFrame({'Precio': [100, 200, 300, 9999]})
        features = ['Precio']
        # Simular opción 1: eliminar outliers
        original_input = builtins.input
        builtins.input = lambda _: "1"
        df_filtrado, ok = oh.manejar_valores_atipicos(df.copy(), features)
        builtins.input = original_input
        self.assertTrue(ok)
        self.assertTrue(df_filtrado['Precio'].max() < 9999)
