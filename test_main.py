import unittest


from autograding import TestInputOutput, TestFunction
from autograding.case import InOut, FuncCall


class TestSciNotation(TestInputOutput):
    def setUp(self):
        self.testcases = [
            InOut(input="1.1x10^-3", output="This number in E notation is 1.1E-3."),
            InOut(input="-1.5x10^3", output="This number in E notation is -1.5E3."),
            InOut(input="1.2x10^3.4", output="Error converting to scientific E notation."),
            InOut(input="1.O3x10^-5", output="Error converting to scientific E notation."),
            InOut(input="1.2x10^5.1", output="Error converting to scientific E notation."),
        ]


if __name__ == '__main__':
    unittest.main()
