# src/calc_functions/div.py

def div(engine):
    b = engine.pop()
    a = engine.pop()
    engine.push((a[0] / b[0], 0.0))
    return
