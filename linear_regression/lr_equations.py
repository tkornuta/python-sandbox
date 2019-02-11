# Copyright (C) tkornuta, 2019
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
