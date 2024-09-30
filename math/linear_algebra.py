from numpy import arraypad
from numpy.linalg import det, inv

# adding
v = array([3, 2])
w = array([2, -1])
v_and_w = v + w
print(v_and_w)

# scaling
v = array([3, 1])
scale_v = 2.0 * v
print(scale_v)

# i-hat & j-hat
i_hat = array([2, 0])
j_hat = array([0, 3])

basis = array([i_hat, j_hat]).transpose()

v = array([2, 1])

w = basis.dot(v)

print(w)

# rotation & inversions
i_hat = array([1, 2])
j_hat = array([-4, -1])

basis = array([i_hat, j_hat]).transpose()

v = array([1, 1])

w = basis.dot(v)

print(w)

# determinant
i_hat = array([3, 0])
j_hat = array([-0, 2])

basis = array([i_hat, j_hat]).transpose()

d = det(basis)

print(d)

# zero determinant
i_hat = array([-1, 1])
j_hat = array([1, -1])

basis = array([i_hat, j_hat]).transpose()

d = det(basis)

print(d)

# matrix multiplication
# Transformation 1
i_hat_1 = array([0, 1])
j_hat_1 = array([-1, 0])
transform_1 = array([i_hat_1, j_hat_1]).transpose()

# Transformation 2
i_hat_2 = array([1, 0])
j_hat_2 = array([1, 1])
transform_2 = array([i_hat_2, j_hat_2]).transpose()

combined = transform_2 @ transform_1

print(combined)

# system of equationd
A = array([[4, 2, 4],
           [5, 3, 7],
           [9, 3, 6]])
print(inv(A))
print('identity:')
print(inv(A).dot(A))

# Matrix Decomposition
