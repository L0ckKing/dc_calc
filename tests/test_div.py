import pytest
from tests import *
from tests.app_test_runner import runner
from main import app
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
    # 1. Unit test (isolated engine logic)
    calc = build_calc((4.0, 2.0), (1.0, 1.0))
    div(calc)
    compare(calc.pop(), (3.0, -1.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 4+j2 push 1+j1 div pop")
    assert exit_code == 0
    assert output == "3-j1"

def test_T_DIV_ERR1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((1.0, 0.0), (0.0, 0.0))
    with pytest.raises(ZeroDivisionError):
        div(calc)

    # 2. CLI test (end-to-end user experience)
    result = runner.invoke(app, input="push 1 push 0 div\n")
    assert result.exit_code == 0
    assert result.stderr.strip() == "Error: division by zero"

def test_T_DIV_ERR2():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((1.0, 0.0), (0.0, 0.0))
    with pytest.raises(ZeroDivisionError):
        div(calc)

    # 2. CLI test (end-to-end user experience)
    result = runner.invoke(app, input="push 1+j0 push 0+j0 div\n")
    assert result.exit_code == 0
    assert result.stderr.strip() == "Error: division by zero"
