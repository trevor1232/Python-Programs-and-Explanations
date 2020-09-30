import vecutil

def compare(sen1, sen2, votingDict):
    total = 0
    vector = vecutil.list2vec(votingDict.get(sen1))
    vector2 = vecutil.list2vec(votingDict.get(sen2))
    for k in range(len(vector.f)):
        total = total + vector.f.get(k) * vector2.f.get(k)
    return (total)

def most_similar(sen, votingDict):
    i = 0
    for k in votingDict:
        if (compare(sen, k, votingDict) < i):
            i = (compare(sen, k, votingDict))
    sameSen = ""
    for k in votingDict:
        if (compare(sen, k, votingDict) == i and k != sen and i != 0):
            sameSen = str(sameSen) + " and " + str(k)
            continue
        if (compare(sen, k, votingDict) > i and k != sen):
            i = compare(sen, k, votingDict)
            sameSen = k
    return (sameSen)
def least_similar(sen, votingDict):
    i = compare(sen, sen, votingDict)
    sameSen = ""
    for k in votingDict:
        if (compare(sen, k, votingDict) == i and k != sen and i != 0):
            sameSen = str(sameSen) + " and " + str(k) + " "
            continue
        if (compare(sen, k, votingDict) <= i and k != sen):
            i = compare(sen, k, votingDict)
            sameSen = k
    return (sameSen)
