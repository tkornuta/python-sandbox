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


