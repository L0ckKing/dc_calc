# src/calc_functions/cos.py
import cmath

def cos(engine):
    a = engine.pop()
    result = cmath.cos(complex(a[0], a[1]))
    engine.push((result.real, result.imag))
    return
