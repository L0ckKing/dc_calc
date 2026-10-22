import sys
import typer
from typing import Optional

app = typer.Typer()

def process_tokens(tokens: list[str], stack: list[float]) -> bool:
    """Processes tokens on the in-memory stack. Returns False to signal quit."""
    for token in tokens:
        if token == "q":
            return False
        elif token == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif token == "p":
            if stack:
                typer.echo(stack[-1])
        else:
            stack.append(float(token))
    return True

@app.command()
def main(
    expression: Optional[str] = typer.Option(
        None, "-e", "--expression", help="Expression to evaluate directly."
    )
):
    stack: list[float] = []

    # Mode 1: One-shot expression flag (dc -e "3 4 + p")
    if expression:
        process_tokens(expression.split(), stack)
        return

    # Mode 2: Interactive loop / piped stream (dc)
    # This loop stays alive, keeping `stack` in memory until EOF or 'q'
    for line in sys.stdin:
        should_continue = process_tokens(line.split(), stack)
        if not should_continue:
            break
