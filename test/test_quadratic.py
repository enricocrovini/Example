import unittest
from quadratic import quadratic_solver

class test_quadratic(unittest.TestCase):
    def test_1(self): #python has introspection anything that begins with test is run 
        #print(quadratic_solver(1,2,1))
        self.assertListEqual(quadratic_solver(1,2,1), [-1])
    def test_2(self):
        print(quadratic_solver(-1,0,1))
        #self.assertListEqual(quadratic_solver(-1,0,1), [1,-1])
        self.assertIn(1, quadratic_solver(-1,0,1))
        self.assertIn(-1, quadratic_solver(-1,0,1))
        self.assertEqual(len(quadratic_solver(-1,0,1)),2)        
    def test_4(self):
        with self.assertRaises(ZeroDivisionError):
            quadratic_solver(0,0,1)
