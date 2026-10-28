# src/calc.py
from src.calc_functions.add import add
from src.calc_functions.sub import sub
from src.calc_functions.mul import mul
from src.calc_functions.div import div
from src.calc_functions.delete import delete
from src.calc_functions.sin import sin
from src.calc_functions.cos import cos

def transform_number(token: str) -> tuple[float, float]:
        token = token.replace(" ", "")
        
        # 1. Pure Real: No 'j' present
        if "j" not in token:
            return (float(token), 0.0)

        # 2. Split on 'j'
        left, right = token.split("j")

        # If right is empty or just a sign, 'j' might have an implicit coefficient of 1
        if right == "" or right == "+":
            imag_val = 1.0
        elif right == "-":
            imag_val = -1.0
        else:
            imag_val = float(right)

        # 3. Pure Imaginary: e.g., 'j5', '-j2', '+j4'
        if left == "" or left == "+":
            return (0.0, imag_val)
        if left == "-":
            return (0.0, -imag_val)

        # 4. Full Complex: e.g., '3+j4' -> left='3+', right='4'
        sign = left[-1]
        real_val = float(left[:-1])

        if sign == "-":
            imag_val = -imag_val

        return (real_val, imag_val)

def format_num(n: float) -> str:
    # Normalize -0.0 to 0.0
    if n == 0.0 or n == -0.0:
        return "0"
    # Format to int string if it's an exact integer, otherwise normal float
    if n.is_integer():
        return str(int(n))
    return f"{n:.9f}".rstrip("0").rstrip(".")

def format_canonical(value: tuple[float, float]) -> str:
    real, imag = value
    real_str = format_num(real)
    
    # Handle the sign and magnitude of the imaginary part
    if imag < 0 and imag != -0.0:
        imag_str = format_num(abs(imag))
        return f"{real_str}-j{imag_str}"
    else:
        imag_str = format_num(abs(imag))
        return f"{real_str}+j{imag_str}"

class StackEngine:
    def __init__(self):
        self.stack: list[tuple[float, float]] = []

    def push(self, value: tuple[float, float]):
        self.stack.append(value)

    def pop(self) -> tuple[float, float]:
        return self.stack.pop()

    def pop_and_print(self):
        val = self.pop()
        print(format_canonical(val))

    # Add your operations here
    operations: dict = {
        "push": push,
        "pop": pop_and_print,
        "add": add,
        "mul": mul,
        "div": div,
        "delete": delete,
        "sin": sin,
        "cos": cos,
        "sub": sub
    }

    def apply_operation(self, token: str):
        if token in self.operations:
            self.operations[token](self)
        else:
            raise SyntaxError(f"Invalid operation: {token}")

    def apply_operations(self, tokens: list[str]):
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == "push":
                i += 1
                if i >= len(tokens):
                    raise SyntaxError("Missing number argument after push")
                self.push(transform_number(tokens[i]))
            else:
                self.apply_operation(token)
            i += 1

