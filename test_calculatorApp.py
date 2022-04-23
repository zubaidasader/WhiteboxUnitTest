import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *
import calculatorApp

class Uni_Test(unittest.TestCase):
#SetUp and TearDown
    def setUp(self): 
        print("Setup .. ")
        return super().setUp()
        
    def tearDown(self) -> None:
        print("TearDown .. ")
        return super().tearDown()

#Testing Add Method
    def test_Add(self):
        # Positive + Positive
        self.assertEqual(add(10,10), 20)
        self.assertEqual(calculate('1',10,10), 20)
        # Positive + Negative
        self.assertEqual(add(10,-20), -10)
        self.assertEqual(calculate('1',10,-20), -10)
        # Negative + Negative
        self.assertEqual(add(-10,-10), -20)
        self.assertEqual(calculate('1',-10,-10), -20)
        #Not equal
        self.assertNotEqual(calculate('1',9,3), 9)

#Testing Subtract Method
    def test_Subtract(self):
        # Positive - Positive
        self.assertEqual(subtract(20,10), 10)
        self.assertEqual(calculate('2',20,10), 10)
        # Positive - Negative
        self.assertEqual(subtract(30,-20), 50)
        self.assertEqual(calculate('2',30,-20), 50)
        # Negative - Positive
        self.assertEqual(subtract(-20, 30), -50)
        self.assertEqual(calculate('2',-20, 30), -50)
        # Negative - Negative
        self.assertEqual(subtract(-10,-10), 0)
        self.assertEqual(calculate('2',-10,-10), 0)
        #Not equal
        self.assertNotEqual(calculate('2',9,3), 9)

#Testing Multiply Method
    def test_Multiply(self):
        # Positive * Positive
        self.assertEqual(multiply(3,3), 9)
        result1 = 3 , "*", 3, "=", 9
        self.assertEqual(calculate('3',3,3), result1 )
        # Positive * Negative
        self.assertEqual(multiply(3,-3), -9)
        result2 = 3 , "*", -3, "=", -9
        self.assertEqual(calculate('3',3,-3),result2)
        # Negative * Negative
        self.assertEqual(multiply(-3,-3), 9)
        result3 = -3 , "*", -3, "=", 9
        self.assertEqual(calculate('3',-3,-3), result3)
        #Not equal
        result4 = -3 , "*", -3, "=", 10
        self.assertNotEqual(calculate('3',-3,-3), result4)

#Testing Division Method
    def test_Divide(self):
        # Positive / Positive
        self.assertEqual(divide(3,3), 1)
        res1= 3 , "/", 3, "=", 1
        self.assertEqual(calculate('4',3,3), res1)
        # Positive / Negative
        self.assertEqual(divide(3,-3), -1)
        res2= 3 , "/", -3, "=", -1
        self.assertEqual(calculate('4',3,-3), res2)
        # Negative / Positive
        self.assertEqual(divide(-3, 3), -1)
        res3= -3 , "/", 3, "=", -1
        self.assertEqual(calculate('4',-3, 3), res3)
        # Negative / Negative
        self.assertEqual(divide(-3,-3), 1)
        res4 = -3 , "/", -3, "=", 1
        self.assertEqual(calculate('4',-3,-3), res4)
        #ِ Any Number / Zero
        self.assertRaises(ZeroDivisionError,divide, 3,0)
        self.assertRaises(ZeroDivisionError, calculate, '4','3','0')   
        # Zero / Any Number
        self.assertEqual(divide(0, 3), 0)
        res6 = 0 , "/", 3, "=", 0
        self.assertEqual(calculate('4', '0', 3), res6)
        #Not equal
        res8 = -3 , "/", -3, "=", 10
        self.assertNotEqual(calculate('4',-3,-3), res8)     

#Testing check user input Method
    def test_check_user_input(self):
        # Empty input
        self.assertRaises(ValueError, check_user_input, '')        
        # integer  input 
        self.assertEqual(check_user_input("10"),10)
        # float  input 
        self.assertEqual(check_user_input("10.2"),10.2)
        # string  input 
        self.assertRaises(ValueError, check_user_input, 'ok')
 

#Testing isExit Method
    def test_isExit(self):
        # no input
        self.assertEqual(isExit("no"),True)
        # yes input 
        self.assertEqual(isExit("yes"),False)
        # No input 
        self.assertRaises(ValueError, isExit, 'No')
        # Yes input 
        self.assertRaises(ValueError, isExit, 'Yes')
        # Empty input 
        self.assertRaises(ValueError, isExit, ' ')
        # another string input
        self.assertRaises(ValueError, isExit, 'Maybe')

#Testing calculate Method
    def test_calculate_add(self):
        self.patcher1 = patch('calculatorApp.add', return_value = 8)
        self.MockClass1 = self.patcher1.start()

        assert calculatorApp.add is self.MockClass1
        self.assertEqual(calculate('1',2,6), 8)

        self.addCleanup(self.patcher1.stop)

    def test_calculate_subtract(self):
        self.patcher1 = patch('calculatorApp.subtract', return_value = 8)
        self.MockClass1 = self.patcher1.start()

        assert calculatorApp.subtract is self.MockClass1
        self.assertEqual(calculate('2',10,2), 8)
        self.addCleanup(self.patcher1.stop)
    
    def test_calculate_multiply(self):
        self.patcher1 = patch('calculatorApp.multiply', return_value = 9)
        self.MockClass1 = self.patcher1.start()

        res = 3 ,'*',3,"=",9
        assert calculatorApp.multiply is self.MockClass1
        self.assertEqual(calculate('3',3,3), res)

        self.addCleanup(self.patcher1.stop)

    def test_calculate_divide(self):
        self.patcher1 = patch('calculatorApp.divide', return_value = 2)
        self.MockClass1 = self.patcher1.start()

        res = 4 ,'/',2,"=",2
        assert calculatorApp.divide is self.MockClass1
        self.assertEqual(calculate('4',4,2), res)

        self.addCleanup(self.patcher1.stop)

    def test_calculate_divideZero(self):
        self.patcher1 = patch('calculatorApp.divide', return_value = ZeroDivisionError)
        self.MockClass1 = self.patcher1.start()

        res = 4 ,'/',0,"=",0
        assert calculatorApp.divide is self.MockClass1
        self.assertRaises(ZeroDivisionError, calculate, '4','4','0')

        self.addCleanup(self.patcher1.stop)

    def test_calculate_invalid_choice(self):
        self.patcher1 = patch('calculatorApp.calculate', return_value = Exception)
        self.MockClass1 = self.patcher1.start()

        assert calculatorApp.calculate is self.MockClass1
        self.assertRaises(Exception, calculate, 'x','1','2')

        self.addCleanup(self.patcher1.stop)
    
    def test_calculate_null_value(self):
        self.patcher1 = patch('calculatorApp.calculate', return_value = ValueError)
        self.MockClass1 = self.patcher1.start()

        assert calculatorApp.calculate is self.MockClass1
        self.assertRaises(ValueError, calculate, '2','','')

        self.addCleanup(self.patcher1.stop)

if __name__ == "__main__":
    unittest.main()