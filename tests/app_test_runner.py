import pytest
from typer.testing import CliRunner
from main import app
from src.calc import StackEngine

runner = CliRunner()

def run_cli(test_input: str) -> tuple[int, str]:
    """Runs the CLI and returns (exit_code, stdout_text)."""
    result = runner.invoke(app, input=test_input + "\n")
    return result.exit_code, result.stdout.strip().replace("DC Calculator operational:\n", '')

def build_calc(*values: tuple[float, float]) -> StackEngine:
    """Instantiates a StackEngine and pushes all provided values in order."""
    calc = StackEngine()
    for value in values:
        calc.push(value)
    return calc

def compare(actual: tuple[float, float], expected: tuple[float, float], tol: float = 1e-4):
    """Compares complex tuples using pytest.approx with an optional tolerance."""
    assert actual[0] == pytest.approx(expected[0], abs=tol)
    assert actual[1] == pytest.approx(expected[1], abs=tol)