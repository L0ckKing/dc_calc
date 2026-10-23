# src/calc_functions/mul.py

def mul(engine):
    b = engine.pop()
    a = engine.pop()
    engine.push((a[0] * b[0], 0.0))
    return
