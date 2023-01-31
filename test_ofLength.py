
import unittest

# TODO: make main.py import from a parent directory so the tests can go in their own folder - it's harder than you think
import main


class main_tests(unittest.TestCase):
  def test_ofLength3_HasReasonableCountOfWords(self):
    
    MOST3LETTERWORDS = 1065 # SCRABBLEDICT_VOL6
    
    # check the total number of words of length 3 is less than or equal to another dictionary and greater than or equal to 0
    W = main.Words()
    self.assertLessEqual(len(W.ofLength(3)), MOST3LETTERWORDS)
    self.assertGreaterEqual(len(W.ofLength(3)), 0)

    
  def test_ofLength3_DefaultArgumentWorks(self):

    W = main.Words()

    # test the default argument returns the same as the argument "=="
    self.assertListEqual(W.ofLength(3), W.ofLength(3, rule="=="))


  def test_takeSampleofLength3_LessEquals(self):

    # given a sample S
    W = main.Words()

    S1 = W.takeSample(10).ofLength(3)
    S2 = W.ofLength(3).takeSample(10) #which would typically be fixed
    # are all word contained in S, ofLength 3


    self.assertRaises(W.ofLength(), Exception)

  def test_takeSampleofLength3_LessThan(self):
    
    self.assertRaises(W.ofLength(), Exception)

  def test_takeSampleofLength3_EqualTo(self):
    
    self.assertRaises(W.ofLength(), Exception)

  def test_takeSampleofLength3_GreaterThan(self):
    
    self.assertRaises(W.ofLength(), Exception)

  def test_takeSampleofLength3_GreaterEquals(self):
    
    self.assertRaises(W.ofLength(), Exception)


    
  def test_ofLength3_IsInSourceDict(self):

    # take a sample of W following the 'ofLength' rule
    W = main.Words()
    S = W.ofLength(3)

    # check each word in the sample is contained in W
    for s in S.contents:
        self.assertIn(s, W.contents)


if __name__ == "__main__":
    unittest.main()


