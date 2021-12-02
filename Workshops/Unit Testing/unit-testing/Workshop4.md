Gabriel Kiprono
Run py Workshop4_calc_test.py or python3 Workshop4_calc_test.p


09/25/2021 02:46:06
...EEF
======================================================================
ERROR: testStringDivision (__main__.Testing)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Gabriel\School\Coursework\Fall 21\4585\Workshops\Unit Testing\unit-testing\Workshop4_simpleCalc.py", line 30, in divideTwoNums
    argA = int(a)
ValueError: invalid literal for int() with base 10: 'abuu'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Gabriel\School\Coursework\Fall 21\4585\Workshops\Unit Testing\unit-testing\Workshop4_calc_test.py", line 26, in testStringDivision
    self.assertEqual(divideTwoNums("abuu", 2),"could not convert string to float", ValueError)
  File "C:\Gabriel\School\Coursework\Fall 21\4585\Workshops\Unit Testing\unit-testing\Workshop4_simpleCalc.py", line 32, in divideTwoNums
    argA = float(a)
ValueError: could not convert string to float: 'abuu'

======================================================================
ERROR: testWrongInputMultiplication (__main__.Testing)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Gabriel\School\Coursework\Fall 21\4585\Workshops\Unit Testing\unit-testing\Workshop4_simpleCalc.py", line 18, in multiplyNumbers
    argB = int(b)
ValueError: invalid literal for int() with base 10: 'be'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Gabriel\School\Coursework\Fall 21\4585\Workshops\Unit Testing\unit-testing\Workshop4_calc_test.py", line 37, in testWrongInputMultiplication
    self.assertEqual(multiplyNumbers(2, "be"), ValueError, "wrong input")
  File "C:\Gabriel\School\Coursework\Fall 21\4585\Workshops\Unit Testing\unit-testing\Workshop4_simpleCalc.py", line 20, in multiplyNumbers
    ArgB = float(b)
ValueError: could not convert string to float: 'be'

======================================================================
FAIL: testZeroDivision (__main__.Testing)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Gabriel\School\Coursework\Fall 21\4585\Workshops\Unit Testing\unit-testing\Workshop4_calc_test.py", line 30, in testZeroDivision
    self.assertEqual(divideTwoNums(2,1), "Error, Division by zero!", ZeroDivisionError)
AssertionError: 2.0 != 'Error, Division by zero!' : <class 'ZeroDivisionError'>

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (failures=1, errors=2)
