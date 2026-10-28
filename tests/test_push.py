from tests import *
from src.calc import StackEngine

def test_T_PUSH_REAL1():
        # 1. Unit test (isolated engine logic)
        calc = build_calc()
        calc.push((5,0))
        assert calc.pop() == (5,0)

        # 2. CLI test (end-to-end user experience)
        result = run_cli("push 5 pop")
        assert result[0] == 0
        assert result[1] == "5+j0"

def test_T_PUSH_CPLX1():
        # 1. Unit test (isolated engine logic)
        calc = build_calc()
        calc.push((-2.5,-0.25))
        assert calc.pop() == (-2.5,-0.25)

        # 2. CLI test (end-to-end user experience)
        result = run_cli("push -2.5-j0.25 pop")
        assert result[0] == 0
        assert result[1] == "-2.5-j0.25"

def test_T_PUSH_CPLX2():
        # CLI test (end-to-end user experience)
        result = run_cli("push 3 + j 4 pop")
        assert result[0] == 0
        assert result[1] == "3+j4"





