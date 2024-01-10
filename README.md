# Assignment 4b: E notation

**Note:** This is the same as Assignment 3b, but this time you can use lists and loops.

## Part 1: E notation validation

Scientific E notation is a way of presenting very large or very small numbers in scientific notation (i.e. standard form) without the `×` symbol, superscripts, or subscripts.

### Example

The following examples show text-based scientific notation on the left and scientific E notation on the right:

1. `"1.03x10^7"` → `"1.03E7"`
2. `"2.008x10^-5"` → `"2.008E-5"`

In both examples, the letter `x` represents the 'multiply' mathematical operator, while the caret symbol (`^`) represents the 'power of' mathematical operator. In example 1, the `1.03` part of the number is called the **mantissa** (or *significand*), while the power of 10, i.e. the `7`, is called the **exponent**.

## Part 1: Processing

Write program code to:

1. Ask the user to input a number in valid scientific notation
2. Extract the mantissa and exponent from user input
3. Print the number in scientific E notation.

*Hint: You can search for the positions of special characters in scientific notation to extract substrings from user input.*

## Part 2: Validation

Modify your program code to **validate the user input** before returning the result in scientific E notation.

Valid text-based scientific notation must obey the following rules:

1. The only valid characters in scientific notation are the digits `0-9`, the letters `E` and `x`, the period symbol `.`, the hyphen symbol `-`, and the caret symbol `^`. No spaces are allowed in the string.
2. There should be no more than one period (`.`), multiply symbol (`x`), or caret symbol (`^`) in the input string.
3. The exponent should be a valid integer (no floats allowed).

The following decision table shows the validation rules and their expected result.

```
                                        ┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
                                        │             Rules             │
┍━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┿━━━┯━━━┯━━━┯━━━┯━━━┯━━━┯━━━┯━━━┥
│         |All characters valid?        │ Y | Y | Y | Y | N | N | N │ N |
|         ┝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┿━━━┿━━━┿━━━┿━━━┿━━━┿━━━┿━━━┿━━━┥
│Condition|Symbol count <= 1?           │ Y | Y | N | N | Y | Y | N | N |
|         ┝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┿━━━┿━━━┿━━━┿━━━┿━━━┿━━━┿━━━┿━━━┥
│         |Exponent is integer?         │ Y | N | Y | N | Y | N | Y | N |
┝━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┿━━━┿━━━┿━━━┿━━━┿━━━┿━━━┿━━━┿━━━┥
│ Result  |Is valid scientific notation │ T | F | F | F | F | F | F │ F |
┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┷━━━┷━━━┷━━━┷━━━┷━━━┷━━━┷━━━┷━━━┙
```
Table 1: Decision table for scientific notation input

If the input is not in valid scientific notation, print an error message informing the user and **do not report the conversion result**.

### Expected output:

    Enter a number in scientific notation: 1.1x10^-3
    This number in E notation is 1.1E-3.
    
    Enter a number in scientific notation: -1.5x10^3
    This number in E notation is -1.5E3.
    
    Enter a number in scientific notation: 1.2x10^3.4
    Error converting to scientific E notation.


# Submission

Before submission, run the tests on your final code.
