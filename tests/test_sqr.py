from tests import build_calc, compare, run_cli


def test_T_SQR_CPLX1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((1.0, 2.0))
    calc.apply_operation("sqr")
    compare(calc.pop(), (-3.0, 4.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 1+j2 SQR pop")
    assert exit_code == 0
    assert output == "-3+j4"

def test_T_SQR_REAL1():
    # 1. Unit test (isolated engine logic)
    calc = build_calc((5.0, 0.0))
    calc.apply_operation("sqr")
    compare(calc.pop(), (25.0, 0.0))

    # 2. CLI test (end-to-end user experience)
    exit_code, output = run_cli("push 5 SQR pop")
    assert exit_code == 0
    assert output == "25+j0"

def test_T_SQR_ERR1():
    import pytest
    from tests import build_calc
    from tests.app_test_runner import runner
    from main import app

    # 1. Unit test (stack underflow)
    calc = build_calc()

    with pytest.raises(IndexError):
        calc.apply_operation("sqr")

    # 2. CLI test (error message)
    result = runner.invoke(app, input="SQR\n")
    assert "Error: stack underflow" in result.stderr