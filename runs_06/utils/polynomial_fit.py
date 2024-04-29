from sympy import symbols, sqrt, series

# Define the symbols and constants
x = symbols('x')
a = 0.51  # center of the ellipse
b = 0.08  # maximum height of the ellipse

# Define the original height function
height_expr = b * sqrt(1 - ((x - a)/a)**2)

# Now we will expand the height expression into a Taylor series around x=a to the 4th degree
# The series expansion will give us a polynomial approximation of the height expression
# taylor_expansion = series(height_expr, x, a, 6).removeO()  # 4th degree will require going to the 6th term
# try 3rd degree
taylor_expansion_3 = series(height_expr, x, a, 4).removeO()  
taylor_expansion_4 = series(height_expr, x, a, 5).removeO()
taylor_expansion_5 = series(height_expr, x, a, 6).removeO()

# Simplify the expression to make it more readable
simplified_taylor_3 = taylor_expansion_3.simplify()
simplified_taylor_4 = taylor_expansion_4.simplify()
simplified_taylor_5 = taylor_expansion_5.simplify()


# plot the original height function and the polynomial approximation
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['text.usetex'] = False
plt.figure()
x = np.linspace(0, 1, 100)
height = b * np.sqrt(1 - ((x - a)/a)**2)
plt.plot(x, height, label='Original Height Function')
plt.plot(x, [simplified_taylor_3.subs('x', xi) for xi in x], label='Taylor Series Approximation 3')
plt.plot(x, [simplified_taylor_4.subs('x', xi) for xi in x], label='Taylor Series Approximation 4')
plt.plot(x, [simplified_taylor_5.subs('x', xi) for xi in x], label='Taylor Series Approximation 5')
plt.xlabel('x')
plt.ylabel('Height')
plt.legend()
plt.axis('equal')
plt.show()