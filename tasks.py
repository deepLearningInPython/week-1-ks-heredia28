import numpy as np



# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# Task 1: 
# Instructions:
#Write a function that takes one numeric argument as input. 
#If the number is larger than zero, the function should return 1, otherwise it should return -1.
#The name of the function should be step

# Your code here:
# -----------------------------------------------

def step(a):
    if a > 0:
        return 1
    else:
        return -1

def test_step_positive():
    assert step(5) == 1, "Failed on positive input"

def test_step_negative():
    assert step(-3) == -1, "Failed on negative input"

def test_step_zero():
    assert step(0) == -1, "Failed on zero input"

# Run the tests
test_step_positive()
test_step_negative()
test_step_zero()

print("All tests passed.")


# -----------------------------------------------


# Task 2:
# Instructions:
#Write a function that takes in two arguments: a numpy array, and an integer (call argument "cutoff" and set default to 0).
#The function should return a numpy array of the same length, with all elements smaller than the cutoff being set to cutoff.
#The name of the function should be ReLu


# Your code here:
# -----------------------------------------------
def ReLU(array, cutoff = 0):
    return np.maximum(array, cutoff)

# -----------------------------------------------


# Task 3:
# Instructions:
#Write a function that takes in a two-dimensional numpy array of size (n, p) and a one-dimensional numpy array of size p.
#The function should start by multiplying the two numpy arrays (matrix multiplication).
#Next, apply the ReLu function from above to the resulting matrix and return the result.
#Name the function neural_net_layer

# Your code here:
# -----------------------------------------------

def neural_net_layer(matrix, vector):
    result = np.dot(matrix, vector)
    return ReLU(result)

# ------------------------------------------