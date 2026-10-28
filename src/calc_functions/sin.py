# src/calc_functions/sin.py
import cmath

def sin(engine):
    a = engine.pop()
    result = cmath.sin(complex(a[0], a[1]))
    engine.push((result.real, result.imag))
    return
