import pytest
from tests import *
from tests.app_test_runner import runner
from main import app
from src.calc_functions.delete import delete

def test_T_DEL_REAL1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((1.0, 0.0), (2.0, 0.0))
    delete(calc)
    compare(calc.pop(), (1.0, 0.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 1 push 2 delete pop")
    assert exit_code == 0
    assert output == "1+j0"

def test_T_DEL_CPLX1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((1.0, 1.0), (2.0, 3.0))
    delete(calc)
    compare(calc.pop(), (1.0, 1.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 1+j1 push 2+j3 delete pop")
    assert exit_code == 0
    assert output == "1+j1"

def test_T_DEL_ERR1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc()
    with pytest.raises(IndexError):
        delete(calc)

    # 2. CLI test (end-to-end user experience)
    result = runner.invoke(app, input="delete\n")
    assert result.exit_code == 0
    assert result.stderr.strip() == "Error: stack underflow"