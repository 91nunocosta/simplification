"""Implement algebraic simplification by function substitution.

Algebraic expressions are defined as follows:

    1. The expected operations are standard arithmetic:
        +   addition,
        -   subtraction,
        *  multiplication,
        /  division, or
        **  exponentiation.

    2. The expected terms are:
        a) constants,
        b) the variable x, or
        c) a function name f<number>.

In expressions, function names are interpreted as applying the function to variable x.
For example, f1 is interpreted as f1(x).

Example:
    0.5 - f4 is interpreted as 0.5 - f4(x)
    

The functions are defined by equations represented using a dict where: 
 - keys are the function names.
 - values are the expressions defining the functions.

Example:

    f1(x) = f2(x) + f5(x)
    f2(x) = 0.5 - f4(x)
    f3(x) = f1(x) * f2(x)
    f4(x) = x
    f5(x) = 90 + 1

is represented as

   {
        "f1": "f2 + f5",
        "f2": "0.5 - f4",
        "f3": "f1 * f2",
        "f4": "x",
        "f5": "90 + 1",
    }
"""
from typing import Dict
import re


def is_simplifiable(_expression: str, _functions: Dict[str, str]) -> bool:
    """Returns True iff expression is simplifiable given the functions definition."""
    # Assume implementation is already here
    return True


OPERATORS = {"+", "-", "*", "/", "**"}


def simplify(expression: str, functions: Dict[str, str]) -> str:
    """Simplify an algebraic expression by function substitutions,
     given the functions definition.

    Args:
         expression: the expression to simplify.
         functions: the functions definition.

     Returns:
         The simplified expression without function applications.
         I.e., an expression where all terms are constants or the variable x.

     Raises:
         ValueError: if any expression is invalid or the simplification isn't possible.
    """
    if not is_simplifiable(expression, functions):
        raise ValueError("Not simplifiable!")

    # solution begins here
    ref_regex = re.compile(r"f\d+")

    refs = re.findall(ref_regex, expression)

    outmost = True
    while refs:
        for ref in refs:
            def_ = functions.get(ref)

            if def_ is None:
                raise ValueError(f"{ref} is undefined.")

            if outmost and all(op not in expression for op in OPERATORS):
                sub_expr = def_
            else:
                sub_expr = f"({def_})"

            expression = expression.replace(ref, sub_expr)

        refs = re.findall(ref_regex, expression)
        outmost = False

    return expression
    # solution ends here


def test_simplify() -> None:
    """Test simplify implementation."""
    functions = {
        "f1": "f2 + f5",
        "f2": "0.5 - f4",
        "f3": "f1 * f2",
        "f4": "x",
        "f5": "90 + 1",
    }

    assert simplify("f1", functions) == "(0.5 - (x)) + (90 + 1)"

    assert simplify("f3", functions) == "((0.5 - (x)) + (90 + 1)) * (0.5 - (x))"

    assert (
        simplify("f1 + f3", functions)
        == "((0.5 - (x)) + (90 + 1)) + (((0.5 - (x)) + (90 + 1)) * (0.5 - (x)))"
    )


if __name__ == "__main__":
    test_simplify()
