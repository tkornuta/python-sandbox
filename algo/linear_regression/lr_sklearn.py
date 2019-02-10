from sklearn.linear_model import LinearRegression
import numpy as np

ints_str_lst = ["95 85", "85 95", "80 70", "70 65", "60 70"]

# Read ints.
x = []
y = []
for ints_str in ints_str_lst:
    ints = [int(x) for x in ints_str.split()]
    x.append( [ ints[0] ] )
    y.append( ints[1] )
print("x = ", x)
print("y = ", y)


# Fit linear regression model.
lm = LinearRegression()
lm.fit(x, y)
# Y = ax+b

# Print coefficients.
a = lm.coef_[0]
b = lm.intercept_
print("a =", a)
print("b =", b)


# Print value for 80.
x1 = np.asarray([80]).reshape(-1, 1)
print(lm.predict(x1))
print(a*80 + b)


