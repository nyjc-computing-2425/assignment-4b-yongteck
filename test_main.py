import sys
import unittest

# autograding submodule might not be successfully pulled on init
# if unsuccessful, we have to pull it manually
# limit number of retries
MAX_RETRIES = 5
retries = 0
while "autograding" not in sys.modules:
    try:
        import autograding
        from autograding.case import FuncCall, InOut
    except ImportError:
        import subprocess
        subprocess.run(["git", "submodule", "update", "--init"])
        retries += 1
    if retries >= MAX_RETRIES:
        sys.exit("[import autograding] Too many retries, exiting")


class TestSciNotation(autograding.TestInputOutput):
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
