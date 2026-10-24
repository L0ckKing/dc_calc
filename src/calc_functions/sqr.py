def sqr(engine):
    real, imag = engine.pop()
    engine.push((real**2 - imag**2, 2 * real * imag))