ints_str_lst = ["95 85", "85 95", "80 70", "70 65", "60 70"]

# Read ints.
x = []
y = []
for ints_str in ints_str_lst:
    ints = [int(x) for x in ints_str.split()]
    x.append( ints[0] )
    y.append( ints[1] )
print("x = ", x)
print("y = ", y)

# Y = ax+b

# Calculate all sums and means.
n = len(ints_str_lst)
s_x = sum(x)
s_xs = sum([i**2 for i in x])
s_y = sum(y)
s_xy = sum([i*j for (i,j) in zip(x,y)])
# Calculate a
a = (n * s_xy - s_x * s_y ) / ( n*s_xs - s_x**2)
print("a =", a)

# Calculate independent term.
b = s_y/n - a * s_x/n
print("b =", b)

# Print value for 80.
print(a*80 + b)
