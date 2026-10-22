import sys
import typer

from src.calc import StackEngine

app = typer.Typer()

@app.command()
def run():
    engine = StackEngine()
    keywords = engine.operations.keys()

    for line in sys.stdin:
        raw_tokens = line.lower().split()
        if not raw_tokens:
            continue

        try:
            tokens = merge_number_tokens(raw_tokens, keywords)
            engine.apply_operations(tokens)
        except IndexError:
            typer.echo("Error: stack underflow", err=True)
        except ZeroDivisionError:
            typer.echo("Error: division by zero", err=True)
        except (SyntaxError, ValueError):
            typer.echo("Error: invalid token", err=True)

## Transforms tokens {1, +j, 5} or {1+, j, 5} into {1+j5}        
def merge_number_tokens(tokens: list[str], command_keywords: set[str]) -> list[str]:
    merged = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        merged.append(token)
        
        if token == "push":
            i += 1
            number_parts = []
            # Collect all parts until the next command keyword or end of list
            while i < len(tokens) and tokens[i] not in command_keywords:
                number_parts.append(tokens[i])
                i += 1
            
            if not number_parts:
                raise SyntaxError("Missing argument for push")
                
            merged.append("".join(number_parts))
            continue
        i += 1
        
    return merged

if __name__ == "__main__":
    app()