
import unittest

# TODO: make main.py import from a parent directory so the tests can go in their own folder - it's harder than you think
import main


class main_tests(unittest.TestCase):
  def test_takeSampleSize3_HasLength3(self):
    
    W = main.Words()
    self.assertEqual( len(W.takeSample(3)), 3)
    
    
    
  def test_takeSampleSize3_IsInSourceDict(self):
    
    W = main.Words()
    self.assertIn(W.takeSample(3).contents, W.contents)


if __name__ == "__main__":
    unittest.main()

