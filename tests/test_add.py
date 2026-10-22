from tests import *
from src.calc_functions.add import add

def test_T_ADD_REAL1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((2.0, 0.0), (5.0, 0.0))
    add(calc)
    compare(calc.pop(), (7.0, 0.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 2 push 5 add pop")
    assert exit_code == 0
    assert output == "7+j0"


def test_T_ADD_CPLX1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((2.0, 2.0), (5.0, 5.0))
    add(calc)
    compare(calc.pop(), (7.0, 7.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 2+j2 push 5+j5 add pop")
    assert exit_code == 0
    assert output == "7+j7"

def test_T_ADD_ERR1():
        pass