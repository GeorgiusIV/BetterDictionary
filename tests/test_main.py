
import unittest
import main

class main_tests(unittest.TestCase):
  def takeSampleSize3_HasLength3(self):
    
    W = main.Words()
    self.assertEqual( len(W.takeSample(3)), 3)
    
    
    
  def takeSampleSize3_IsInSourceDict(self):
    
    W = main.Words()
    self.assertIn(W.takeSample(), W.contents)
