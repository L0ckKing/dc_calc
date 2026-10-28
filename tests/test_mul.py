import pytest
from tests import *
from tests.app_test_runner import runner
from main import app
from src.calc_functions.mul import mul

def test_T_MUL_REAL1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((3.0, 0.0), (-2.0, 0.0))
    mul(calc)
    compare(calc.pop(), (-6.0, 0.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 3 push -2 mul pop")
    assert exit_code == 0
    assert output == "-6+j0"

def test_T_MUL_CPLX1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((1.0, 2.0), (3.0, -4.0))
    mul(calc)
    compare(calc.pop(), (11.0, 2.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 1+j2 push 3-j4 mul pop")
    assert exit_code == 0
    assert output == "11+j2"

def test_T_MUL_ERR1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc()
    with pytest.raises(IndexError):
        mul(calc)

    # 2. CLI test (end-to-end user experience)
    result = runner.invoke(app, input="mul\n")
    assert result.exit_code == 0
    assert result.stderr.strip() == "Error: stack underflow"