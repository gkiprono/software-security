###################################################################
#Gabriel Kiprono
#September 25
#Workshop4_calc_test.py
###################################################################

import unittest
import logging
import sys
import os
from contextlib import redirect_stderr, redirect_stdout
from Workshop4_simpleCalc import *
from datetime import datetime


class Testing(unittest.TestCase):

    def testMultiply(self):
        self.assertEqual(multiplyNumbers(2,3), 6, "Should be 6")

    def testDivision(self):
        self.assertEqual(divideTwoNums(4,2),2, "Sould be 2")

    #intentional string divisiom
    def testStringDivision(self):
        self.assertEqual(divideTwoNums("abuu", 2),"could not convert string to float", ValueError)

    def testZeroDivision(self):
    #intentionally make this fail
        self.assertEqual(divideTwoNums(2,1), "Error, Division by zero!", ZeroDivisionError)

    def testDoublesDivision(self):
        self.assertEqual(divideTwoNums(4.2, 2.1),2, "Should be")

    #test wrong input multiplication
    def testWrongInputMultiplication(self):
        self.assertEqual(multiplyNumbers(2, "be"), ValueError, "wrong input")

def getDateTime():
    now = datetime.now()
    fullTime = now.strftime("%m/%d/%Y %H:%M:%S")
    return fullTime

if __name__ == "__main__":
    testOutput = unittest.TestLoader().loadTestsFromTestCase(Testing)
    originalStdOut = sys.stdout
    sys.stdout = open("Workshop4.md", 'w')
    print("Gabriel Kiprono")
    print("Run py Workshop4_calc_test.py or python3 Workshop4_calc_test.p\n\n")
    print(getDateTime())
    unittest.TextTestRunner(stream=sys.stdout).run(testOutput)
    sys.stdout = originalStdOut
    print("Output in Workshop4.md file")

