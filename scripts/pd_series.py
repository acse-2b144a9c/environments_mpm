from envtest import pd_seriess
import numpy as np

A = ["London","NewYork","Beijing"]
b = ["UK","USA","PRC"]
x = pd_seriess(A,b)
print(x)