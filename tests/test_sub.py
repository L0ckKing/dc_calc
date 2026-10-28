from tests import *
from typer.testing import CliRunner
from src.calc import StackEngine

import pytest
from main import app

def test_T_SUB_REAL1():
        # 1. Unit test (isolated engine logic)
        calc = build_calc((5.0, 0.0), (2.0, 0.0))
        sub(calc)
        compare(calc.pop(), (3.0, 0.0))

        # 2. CLI test (end-to-end user experience)
        result = run_cli("push 5 push 2 sub pop")
        assert result[0] == 0
        assert result[1] == "3+j0"

def test_T_SUB_CPLX1():
        # 1. Unit test (isolated engine logic)
        calc = build_calc((5.0, 3.0), (2.0, 2.0))
        sub(calc)
        compare(calc.pop(), (3.0, 1.0))

        # 2. CLI test (end-to-end user experience)
        result = run_cli("push 5+j3 push 2+j2 sub pop")
        assert result[0] == 0
        assert result[1] == "3+j1"

def test_T_SUB_ERR1():
        # 1. Unit test (isolated engine logic)
        calc = build_calc((3,0))
        with pytest.raises(Exception):
                sub(calc)

        # 2. CLI test (end-to-end user experience)
        result = CliRunner().invoke(app, input="push 3 sub\n")
        assert result.exit_code == 0
        assert result.stderr.strip() == "Error: stack underflow"