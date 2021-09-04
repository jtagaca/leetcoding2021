
# [words]


def equalEdges(words):
    result = []
# compare first last of neighbor
    for i in range(1, len(words)):
        tempResult = isTheSameEndStart(words[i-1], words[i])
        result.append(tempResult)
    return tempResult


def isTheSameEndStart(neighborWord, currentWord):
    # char1StartIDX,char1EndIDX = 0, len(neighborWord)-1
    # char2StartIDX, char2EndIDX = 0, len(currentWord)-1
    char1Start, char1End = neighborWord[0], neighborWord[len(neighborWord)-1]
    char2Start, char2End = currentWord[0], currentWord[len(currentWord)-1]
    if char1Start == char2Start and char2End == char2End:
        return True
    return False
