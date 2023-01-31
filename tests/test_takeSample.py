
import unittest

# TODO: make main.py import from a parent directory so the tests can go in their own folder - it's harder than you think
import main


class main_tests(unittest.TestCase):
  def test_takeSampleSize3_HasLength3(self):
    
    # take a sample of W, and check the sample is of the correct length
    W = main.Words()
    self.assertEqual( len(W.takeSample(3)), 3)
    
    
    
  def test_takeSampleSize3_IsInSourceDict(self):

    # take a sample of W
    W = main.Words()
    S = W.takeSample(3)

    # check each word in the sample is contained in W
    for s in S.contents:
        self.assertIn(s, W.contents)


if __name__ == "__main__":
    unittest.main()

