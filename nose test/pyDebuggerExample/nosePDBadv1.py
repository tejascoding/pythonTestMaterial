#nose example with advanced PDB using
"""
Steps :  execute - nosetests -s file.py

nosetests -s
> /Users/user/PycharmProjects/tdd_in_python/app/calculator.py(7)add()
-> return x - y
(Pdb) list
  2          def add(self, x, y):
  3             number_types = (int, long, float, complex)
  4    
  5             if isinstance(x, number_types) and isinstance(y, number_types):
  6                 import pdb; pdb.set_trace()
  7  ->              return x - y
  8             else:
  9                 raise ValueError
[EOF]
(Pdb)

other options that can be used to interact with debbuger are:

n: step forward to next line of execution.
list: show five lines either side of where you are currently executing to see the code involved with the current execution point.
args: list the variables involved in the current execution point.
continue: run the code through to completion.
jump <line number>: run the code until the specified line number.
quit/exit: stop pdb """



class Calculator(object):
    def add(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            import pdb; pdb.set_trace()
            return x - y
        else:
            raise ValueError




#test case
import unittest
 
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
 
 
if __name__ == '__main__':
    unittest.main()