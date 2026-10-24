from tests import *
from src.calc_functions.cos import cos

def test_T_COS_REAL1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((0.0, 0.0))
    cos(calc)
    compare(calc.pop(), (1.0, 0.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 0 COS pop")
    assert exit_code == 0
    assert output == "1+j0"
