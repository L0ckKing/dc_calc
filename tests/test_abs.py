def test_T_ABS_CPLX1():
    from tests import build_calc, compare, run_cli

    # 1. Unit test (isolated engine logic)
    calc = build_calc((3.0, 4.0))
    calc.apply_operation("abs")
    compare(calc.pop(), (5.0, 0.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 3+j4 ABS pop")
    assert exit_code == 0
    assert output == "5+j0"

def test_T_ABS_REAL1():
    from tests import build_calc, compare, run_cli

    # 1. Unit test (isolated engine logic)
    calc = build_calc((3.0, 0.0))
    calc.apply_operation("abs")
    compare(calc.pop(), (3.0, 0.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 3 ABS pop")
    assert exit_code == 0
    assert output == "3+j0"

def test_T_ABS_ERR1():
    import pytest
    from tests import build_calc
    from tests.app_test_runner import runner
    from main import app

    # 1. Unit test (stack underflow)
    calc = build_calc()

    with pytest.raises(IndexError):
        calc.apply_operation("abs")

    # 2. CLI test (error message)
    result = runner.invoke(app, input="ABS\n")
    assert "Error: stack underflow" in result.stderr

#Extra test besides the ones recommended in the instructions
def test_T_ABS_NEGATIVE_REAL():
    from tests import build_calc, compare, run_cli

    # 1. Unit test (isolated engine logic)
    calc = build_calc((-3.0, 0.0))
    calc.apply_operation("abs")
    compare(calc.pop(), (3.0, 0.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push -3 ABS pop")
    assert exit_code == 0
    assert output == "3+j0"