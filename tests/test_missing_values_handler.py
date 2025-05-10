import unittest
import pandas as pd
from modules import missing_values_handler as mvh

class TestValoresFaltantes(unittest.TestCase):
    def test_relleno_con_media_y_moda(self):
        df = pd.DataFrame({
            'Edad': [30, None, 50],
            'Sexo': ['M', None, 'F'],
            'Target': [1, 0, 1]
        })
        df_result, completado = mvh.manejar_valores_faltantes(df.copy(), ['Edad', 'Sexo'], 'Target')
        self.assertTrue(completado)
        self.assertFalse(df_result.isnull().values.any())
