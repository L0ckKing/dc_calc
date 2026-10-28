import cmath

def sqrt(engine):
    real, imag = engine.pop()
    result = cmath.sqrt(complex(real, imag))
    engine.push((result.real, result.imag))