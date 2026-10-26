from tests import *
from typer.testing import CliRunner
from src.calc import StackEngine
import pytest
from main import app

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
         # 1. Unit test (isolated engine logic)
        calc = build_calc((3,0))
        with pytest.raises(Exception):
                add(calc)

        # 2. CLI test (end-to-end user experience)
        result = CliRunner().invoke(app, input="push 3 add\n")
        assert result.exit_code == 0
        assert result.stderr.strip() == "Error: stack underflow"