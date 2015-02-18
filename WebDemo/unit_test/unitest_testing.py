import unittest
from calculate import Calculate

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.c = Calculate()

    def test_sum_calculation(self):
	self.assertEqual(self.c.calculate("1","2","+"), "3.0")
    
    def test_division_calculation(self):
	self.assertEqual(self.c.calculate("1","2","/"), "0.5")
	self.assertEqual(self.c.calculate("4","2","/"), "2.0")
	with self.assertRaises(ZeroDivisionError):
		self.c.calculate("4","0","/")


if __name__ == '__main__':
    unittest.main()
