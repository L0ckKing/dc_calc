# src/calc_functions/div.py

def div(engine):
    b = engine.pop()
    a = engine.pop()
    denom = b[0] * b[0] + b[1] * b[1]
    engine.push(((a[0] * b[0] + a[1] * b[1]) / denom, (a[1] * b[0] - a[0] * b[1]) / denom))
    return
