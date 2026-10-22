# src/calc_functions/add.py

def add(engine):
    b = engine.pop()
    a = engine.pop()
    engine.push((a[0] + b[0], a[1] + b[1]))
    return