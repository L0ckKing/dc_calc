from tests import build_calc, compare, run_cli


def test_T_SQRT_CPLX1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((-1.0, 0.0))
    calc.apply_operation("sqrt")
    compare(calc.pop(), (0.0, 1.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push -1 SQRT pop")
    assert exit_code == 0
    assert output == "0+j1"

def test_T_SQRT_REAL1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((4.0, 0.0))
    calc.apply_operation("sqrt")
    compare(calc.pop(), (2.0, 0.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 4 SQRT pop")
    assert exit_code == 0
    assert output == "2+j0"

def test_T_SQRT_ERR1():
    import pytest
    from tests import build_calc
    from tests.app_test_runner import runner
    from main import app

    # 1. Unit test (stack underflow)
    calc = build_calc()

    with pytest.raises(IndexError):
        calc.apply_operation("sqrt")

    # 2. CLI test (error message)
    result = runner.invoke(app, input="SQRT\n")
    assert "Error: stack underflow" in result.stderr