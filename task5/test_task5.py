import unittest
import task5

class TestTask5(unittest.TestCase):

    def testFactors(self):
        self.assertEqual(set(task5.factors(10)), {2,5,10})
        self.assertEqual(set(task5.factors(4)), {2,4})
        self.assertEuqal(set(task5.factors(12)), {2,3,4,6,12})
        
    def testIsPrime(self):
        self.assertTrue(task5.is_prime(13))
        self.assertTrue(task5.is_prime(31))
        self.assertFalse(task5.is_prime(4))
        self.assertFalse(task5.is_prime(20))
        
    def testVowels(self):
	    self.assertEqual(set(task5.vowels('abcd')), {'a'})
	    self.assertEqual(set(task5.vowels('International language')), {'I','e','a','i','o','u'})
	    
    def testLenFunc(self):
	    self.assertEqual(len([1,2,3,4,5]), 5)
	    self.assertEqual(len('love'), 4)

if __name__ == "__main__": 
    unittest.main(verbosity=2)
        
