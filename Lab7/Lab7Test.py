import Lab7
from GF2 import one

def main():
    ## First test case
    s = 0
    t = 0
    z = Lab7.findSecretVector(s, t)
    print("The result for the first test case is: \n")
    print(z)
    print()

    ## Second test case
    s = 1*one
    t = 1*one
    z = Lab7.findSecretVector(s, t)
    print("The result for the second test case is: \n")
    print(z)
    print()

    ## Third teste case
    s = 1*one
    t = 0
    z = Lab7.findSecretVector(s, t)
    print("The result for the third test case is: \n")
    print(z)
    print()


main()