import cmath

def asin(engine):
    real, imag = engine.pop()
    result = cmath.asin(complex(real, imag))
    engine.push((result.real, result.imag))