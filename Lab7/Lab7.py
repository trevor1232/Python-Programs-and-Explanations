# Import functions from given .py files
import random
from vec import dot
from GF2 import one
from vecutil import list2vec

# Create the vectors a0 & b0
a0 = list2vec([one, one, 0, one, 0, one])
b0 = list2vec([one, one, 0, 0, 0, one])


# Generate random integer values within GF2 for vector u
def randGF2():
    return random.randint(0,1) * one

# Find if the secret vector wil return the inputs s & t when multiplied by a0 & b0


def findSecretVector(s, t):
    u = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])

    # Multiply u by a0 & b0
    if a0*u == s and b0*u == t:

        # Return the vector u if the statement is true
        return u

    # Repeat until if statement is satisfied
    else:
        return findSecretVector(s, t) 
