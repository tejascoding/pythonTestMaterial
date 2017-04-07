#nose1.py error is resolved by creating Calculator class
#nosetests nose2.py

class Calculator(object):
 
    def add(self, x, y):
        pass
        


import unittest
#from app.calculator import Calculator     --- if calculator class is stored in folder app->name of file calculator.py
 
class TddInPythonExample(unittest.TestCase):
 
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)
 
 
if __name__ == '__main__':
    unittest.main()
    
    
#next nose3.py for solution of assertion error