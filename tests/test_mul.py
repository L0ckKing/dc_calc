from tests import *
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
        pass

def test_T_MUL_ERR1():
        pass