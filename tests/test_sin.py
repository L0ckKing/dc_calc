import pytest
from tests import *
from tests.app_test_runner import runner
from main import app
from src.calc_functions.sin import sin

def test_T_SIN_REAL1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((0.0, 0.0))
    sin(calc)
    compare(calc.pop(), (0.0, 0.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 0 SIN pop")
    assert exit_code == 0
    assert output == "0+j0"

def test_T_SIN_CPLX1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((1.0, 1.0))
    sin(calc)
    compare(calc.pop(), (1.298457581, 0.634963915))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 1+j1 SIN pop")
    assert exit_code == 0
    assert output == "1.298457581+j0.634963915"

def test_T_SIN_ERR1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc()
    with pytest.raises(IndexError):
        sin(calc)

    # 2. CLI test (end-to-end user experience)
    result = runner.invoke(app, input="SIN\n")
    assert result.exit_code == 0
    assert result.stderr.strip() == "Error: stack underflow"