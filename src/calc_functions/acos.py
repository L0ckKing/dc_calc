import cmath

def acos(engine):
    real, imag = engine.pop()
    result = cmath.acos(complex(real, imag))
    engine.push((result.real, result.imag))