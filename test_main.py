import contextlib
import subprocess
import sys
import unittest

# limit number of retries
MAX_RETRIES = 5
retries = 0

# Force reload of autograding submodule
# This allows it to be updated even after students have accepted an assignment
# It would otherwise require them to delete and re-accept the assignment
# (or alternatively update the submodule manually)
def unload():
    global autograding
    if "autograding" in sys.modules:
        del sys.modules["autograding"]
    with contextlib.suppress(NameError):
        del autograding

unload()
subprocess.run(["git", "submodule", "update", "--init", "--remote"])
import autograding
from autograding.case import FuncCall, InOut


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
