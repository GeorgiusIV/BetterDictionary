
import unittest

# TODO: make main.py import from a parent directory so the tests can go in their own folder - it's harder than you think
import main


class main_tests(unittest.TestCase):
  def test_ofLength3_hasReasonableCountOfWords(self):
    
    MOST3LETTERWORDS = 1065 # SCRABBLEDICT_VOL6
    
    # check the total number of words of length 3 is less than or equal to another dictionary and greater than or equal to 0
    W = main.Words()
    self.assertLessEqual(len(W.ofLength(3)), MOST3LETTERWORDS)
    self.assertGreaterEqual(len(W.ofLength(3)), 0)


    
  def test_ofLength3_defaultArgumentWorks(self):

    W = main.Words()

    # test the default argument returns the same as the argument "=="
    self.assertListEqual(W.ofLength(3).contents, W.ofLength(3, rule="==").contents)



  def test_ofLengthL_allAreLengthL_4xTests(self):

    # test every word in the dictionary returned by ofLength, is of the stated length
    # using WHATIFs/HOWDOs/TODOs as comments

    # WHATIF: W.contents is empty
    # HOWDO:  I get print(AllTrue) to return the list in the Debug View
    r = '=='
    for l in [1,3,5,7]:
        W = main.Words()
        W.ofLength(l, r)
        AllTrue = all([True if len(word) == l  else False for word in W.contents]) # THIS TEST FAILS
        self.assertTrue(AllTrue)

 

  def test_ofLength5_followsEachRule_5xTests(self):
    
    l = 5
    for r in ['>=','>','==','<','<=']:
        W = main.Words()
        W.ofLength(l, r)

        if r == '>=': AllTrue = all([True if len(word) >= l else False for word in W.contents])
        elif r == '>': AllTrue = all([True if len(word) > l else False for word in W.contents])
        elif r == '==': AllTrue = all([True if len(word) == l else False for word in W.contents])
        elif r == '<': AllTrue = all([True if len(word) < l else False for word in W.contents])
        elif r == '<=': AllTrue = all([True if len(word) <= l else False for word in W.contents])
        else: pass

        self.assertTrue(AllTrue)



  def test_ofLength3_IsInSourceDict(self):

    # take a sample of W following the 'ofLength' rule
    W = main.Words()
    S = W.ofLength(3)

    # return a truth value per word in S.contents, then perform an AND-GATE on them all.
    AllIn = all([True if s in W.contents else False for s in S.contents])
    self.assertTrue(AllIn)


if __name__ == "__main__":
    unittest.main()


