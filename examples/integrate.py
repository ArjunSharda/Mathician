import mathician

def f(x):
  return 4 / (1 + x*x)

# Integrate f(x) from 0 to 1 with precision 500
print(mathician.integrate(f, 0, 1, 500))

# Using lambda functions
print(mathician.integrate(lambda x: 4/(1+x*x), 0, 1, 500))