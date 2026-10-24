import pytest
from tests import *
from tests.app_test_runner import runner
from main import app
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

def test_T_COS_CPLX1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((1.0, 1.0))
    cos(calc)
    compare(calc.pop(), (0.833730025, -0.988897706))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 1+j1 COS pop")
    assert exit_code == 0
    assert output == "0.833730025-j0.988897706"

def test_T_COS_ERR1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc()
    with pytest.raises(IndexError):
        cos(calc)

    # 2. CLI test (end-to-end user experience)
    result = runner.invoke(app, input="COS\n")
    assert result.exit_code == 0
    assert result.stderr.strip() == "Error: stack underflow"
