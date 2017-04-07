#solution for nose4.py value error problem

class Calculator(object):
    def add(self, x, y):
        number_types = (int, long, float, complex)
 #test case for NAN arguments
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError
        
        
import unittest
#from app.calculator import Calculator
 
 
class TddInPythonExample(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
 
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
 
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
 
    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)
 
    def test_calculator_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
    
    def test_calculator_returns_error_message_if_y_arg_not_bool(self):
        print self.calc.add(True,False)
        self.assertRaises(ValueError, self.calc.add, True, False)
 
 
 
if __name__ == '__main__':
    unittest.main()