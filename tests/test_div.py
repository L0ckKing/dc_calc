from tests import *
from src.calc_functions.div import div

def test_T_DIV_REAL1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((8.0, 0.0), (2.0, 0.0))
    div(calc)
    compare(calc.pop(), (4.0, 0.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 8 push 2 div pop")
    assert exit_code == 0
    assert output == "4+j0"

def test_T_DIV_CPLX1():
        pass

def test_T_DIV_ERR1():
        pass
