import unittest
from io import StringIO
from unittest.mock import patch
from CalcularHorasTrabalhadas import Calculo, randomizarHorarios

class TestCalculo(unittest.TestCase):
    def setUp(self):
        self.horarios = [
            ('07:51', '12:02'),
            ('07:53', '12:02'),
            ('07:58', '12:01'),
            ('07:47', '12:11'),
            ('07:51', '12:04'),
            ('07:49', '12:08'),
            ('07:58', '12:01'),
            ('07:58', '12:01'),
            ('07:58', '12:01'),
            ('07:49', '12:07'),
            ('08:00', '12:00'),
            ('08:00', '12:00'),
            ('07:49', '12:08'),
            ('08:00', '12:05'),
            ('07:58', '12:01'),
            ('08:00', '12:00'),
            ('08:00', '12:00'),
            ('08:00', '12:00'),
            ('08:00', '12:00'),
            ('07:45', '12:03'),
            ('07:58', '12:01'),
            ('07:58', '12:01'),
            ('07:49', '12:07'),
            ('08:00', '12:00'),
            ('08:00', '12:00'),
            ('07:49', '12:08'),
            ('08:00', '12:05'),
            ('07:58', '12:01'),
        ]

    def test_Calculo(self):
      
        with patch('builtins.input', return_value='10'):
            horariosSelecionados = randomizarHorarios(self.horarios)
           
            with patch('sys.stdout', new=StringIO()) as fake_out:
                Calculo(horariosSelecionados)
       
                output = fake_out.getvalue().strip()
                
                self.assertTrue("Total de horas trabalhadas:" in output)

# Executa os testes
if __name__ == '__main__':
    unittest.main()
