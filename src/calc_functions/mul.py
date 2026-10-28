# src/calc_functions/mul.py

def mul(engine):
    b = engine.pop()
    a = engine.pop()
    engine.push((a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]))
    return
