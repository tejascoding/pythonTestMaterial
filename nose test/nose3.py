#solution code for nose2.py assert error

#this nose1 - nose3 is agile methodology solution

class Calculator(object):
 
    def add(self, x, y):
        return x+y


#can be saved in different file and import that file

import unittest
#from app.calculator import Calculator
 
class TddInPythonExample(unittest.TestCase):
 
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)
 
 
if __name__ == '__main__':
    unittest.main()

#next check out for nose4.py for adding new test case that other than no. values are passed