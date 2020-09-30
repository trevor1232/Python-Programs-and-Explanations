import Lab5
import vecutil

thisDict = {
    "Senator 1": [-1, 1, 1, -1],
    "Senator 2": [1, 1, 1, -1],
    "Senator 3": [-1, -1, 1, -1]
    }
thisDict2 = {
    "Dude 1": [1, 1, 1, -1],
    "Dude 2": [-1, 1, -1, 1],
    "Dude 3": [1, -1, -1, 1]
    }
thisDict3 = {
    "Politician 1": [1, -1, 1, -1],
    "Politician 2": [1, -1, -1, 1],
    "Politician 3": [1, -1, 1, -1]
    }

#compares thisDict using Senator 1 as the base comparison
x = Lab5.compare("Senator 1", "Senator 2", thisDict);
print("The score from comparing these senators is " + str(x))
x = Lab5.most_similar("Senator 1", thisDict);
print("The most similar senator is " + str(x))
x = Lab5.least_similar("Senator 1", thisDict);
print("The least similar senator is " + str(x))

print()

#compares thisDict2 using Dude 2 as the base comparison
x = Lab5.compare("Dude 2", "Dude 1", thisDict2);
print("The score from comparing these senators is " + str(x))
x = Lab5.most_similar("Dude 2", thisDict2);
print("The most similar senator is " + str(x))
x = Lab5.least_similar("Dude 2", thisDict2);
print("The least similar senator is " + str(x))

print()

#compares thisDict3 using Politician 3 as the base comparison
x = Lab5.compare("Politician 3", "Politician 2", thisDict3);
print("The score from comparing these senators is " + str(x))
x = Lab5.most_similar("Politician 3", thisDict3);
print("The most similar senator is " + str(x))
x = Lab5.least_similar("Politician 3", thisDict3);
print("The least similar senator is " + str(x))

"""
print(thisDict.get("Senator 1"))
print(vecutil.Vec.__repr__(vecutil.list2vec(thisDict.get("Senator 1"))))
"""
