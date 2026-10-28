from tests import build_calc, compare, run_cli
from src.calc import transform_number


def test_T_ACOS_CPLX1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((1.0, 1.0))
    calc.apply_operation("acos")
    compare(calc.pop(), (0.904556894, -1.061275061), tol=1e-8)

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 1+j1 ACOS pop")
    assert exit_code == 0

    # Convert compact CLI output back to a numeric tuple
    result = transform_number(output)
    compare(result, (0.904556894, -1.061275061), tol=1e-5)

def test_T_ACOS_REAL1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((1.0, 0.0))
    calc.apply_operation("acos")
    compare(calc.pop(), (0.0, 0.0), tol=1e-8)

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 1 ACOS pop")
    assert exit_code == 0

    # Convert compact CLI output to a numeric tuple
    result = transform_number(output)
    compare(result, (0.0, 0.0), tol=1e-5)

def test_T_ACOS_ERR1():
    import pytest
    from tests import build_calc
    from tests.app_test_runner import runner
    from main import app

    # 1. Unit test (stack underflow)
    calc = build_calc()

    with pytest.raises(IndexError):
        calc.apply_operation("acos")

    # 2. CLI test (error message)
    result = runner.invoke(app, input="ACOS\n")
    assert "Error: stack underflow" in result.stderr