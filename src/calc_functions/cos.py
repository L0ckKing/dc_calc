# src/calc_functions/cos.py
import math

def cos(engine):
    a = engine.pop()
    engine.push((math.cos(a[0]), 0.0))
    return
