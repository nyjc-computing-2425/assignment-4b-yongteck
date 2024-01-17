import subprocess
import unittest


def strip_prompt(stdout: str) -> str:
    """Strip the prompt from stdout.
    The prompt is assumed to end with a colon (:), followed by zero or more
    whitespace characters.
    """
    if stdout.strip():
        stdout = stdout[stdout.find(':') + 1:].lstrip()
    return stdout


def invoke_main(input_: str) -> str:
    """Invoke main.py and return its output."""
    proc = subprocess.Popen(["python", "main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True)
    try:
        stdout, stderr = proc.communicate(input=input_, timeout=1)
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout, stderr = proc.communicate()
    finally:
        # Strip prompt from stdout; use colon to detect
        if stdout.strip():
            stdout = stdout[stdout.find(':') + 1:].lstrip()
        return stdout


class TestInputOutput(unittest.TestCase):

    def test_part1(self):
        testcase = "1.1x10^-3\n"
        testans = "This number in E notation is 1.1E-3.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")

    def test_part2(self):
        testcase = "-1.5x10^3\n"
        testans = "This number in E notation is -1.5E3.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")

    def test_part3(self):
        testcase = "1.2x10^3.4\n"
        testans = "Error converting to scientific E notation.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")

    def test_part4(self):
        testcase = "1.O3x10^-5\n"
        testans = "Error converting to scientific E notation.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")

    def test_part5(self):
        testcase = "1.2x10^5.1\n"
        testans = "Error converting to scientific E notation.\n"
        userans = invoke_main(testcase)
        self.assertIn(userans,
                      testans,
                      msg=f"User output {userans!r} != expected output {testans!r}")


if __name__ == '__main__':
    unittest.main()
