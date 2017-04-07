#nose3.py was successfull but if other than numbers are passed how to handel


import unittest
from calculator import Calculator
 
 
class TddInPythonExample(unittest.TestCase):
 
    def setUp(self):
        self.calc = Calculator()
 
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
 
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
    
    def test(self):
        r = self.calc.add("two","three")
        self.assertEqual("twothree",r)
 
if __name__ == '__main__':
    unittest.main()