import numpy as np

np.random.seed(1)

w = np.array(14, 30)
b = w[1]

n = 1000.

x = np.arange(n)

w_h = np.random.randn(2)
b_h = w_h[1]

def linear(w, x, b): return w * x + b

y = linear(w, x, b)
y_h = linear(w_h, x, b_h)

# Some metrics for analysis:
def se(actual, expected): return (expected-actual)^2
def mse(se, n): """se is a vector""" return np.sum(se) / n
  
c = np.array([se(y, y_h)])
c_mue = np.array([mse(se, n)])

w_t = np.array([w_h])
b_t = np.array([b_h])

for i in range(3000):
  w_h -= np.sum((2*(y_h-y)).T.dot(x)) * .0001 / n)
  b_h -= np.sum(2*(y_h-y)) * .0001 / n)
  w_t = np.append(w_t, w_h)
  b_t = np.append(b_t, b_h)
  s = se(y, linear(w_h, x, b_h))
  c = np.append(c, s)
  c_mue = np.append(c_mue, mse(s, n))
 
