from tests import *
from typer.testing import CliRunner
from src.calc import StackEngine
import pytest
from main import app

def test_T_POP_ERR1():
         # 1. Unit test (isolated engine logic)
        calc = build_calc()
        with pytest.raises(Exception):
                calc.pop()

        # 2. CLI test (end-to-end user experience)
        result = CliRunner().invoke(app, input="pop\n")
        assert result.exit_code == 0
        assert result.stderr.strip() == "Error: stack underflow"
