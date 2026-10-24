from tests import build_calc, compare, run_cli
from src.calc import transform_number


def test_T_ASIN_CPLX1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((1.0, 1.0))
    calc.apply_operation("asin")
    compare(calc.pop(), (0.666239432, 1.061275061), tol=1e-8)

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 1+j1 ASIN pop")
    assert exit_code == 0

    # Convert compact CLI output back to a numeric tuple
    result = transform_number(output)
    compare(result, (0.666239432, 1.061275061), tol=1e-5)

def test_T_ASIN_ERR1():
    import pytest
    from tests import build_calc
    from tests.app_test_runner import runner
    from main import app

    # 1. Unit test (stack underflow)
    calc = build_calc()

    with pytest.raises(IndexError):
        calc.apply_operation("asin")

    # 2. CLI test (error message)
    result = runner.invoke(app, input="ASIN\n")
    assert "Error: stack underflow" in result.stderr