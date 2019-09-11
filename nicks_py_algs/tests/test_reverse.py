import unittest
import src.nicks_py_algs

from src.nicks_py_algs import reverse

class TestReverse(unittest.TestCase):

    def test_reverse_0(self):
        self.assertEqual(reverse.reverse_0("olleh"), "hello")
    
    def test_reverse_1(self):
        self.assertEqual(reverse.reverse_1("olleh"), "hello")

    def test_reverse_2(self):
        self.assertEqual(reverse.reverse_2("olleh"), "hello")

    def test_reverse_3(self):
        self.assertEqual(reverse.reverse_3("olleh"), "hello")

    def test_reverse_4(self):
        self.assertEqual(reverse.reverse_4("olleh"), "hello")

    def test_reverse_5(self):
        self.assertEqual(reverse.reverse_5("olleh"), "hello")
        
if __name__ == '__main__':
    unittest.main()