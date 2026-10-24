from math import hypot

def abs(engine):
    real, imag = engine.pop()
    engine.push((hypot(real, imag), 0.0))

