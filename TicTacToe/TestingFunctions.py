def CountDigit(element):
    if type(element) == int:
        count = 0
        while int(element) > 0:
            count += 1
            element = element // 10
    elif type(element) == str:
        count = len(element)
    return count

def FindSpaces(DigitOfCurrentNumber, SpacePerBlock, LengthPerSide): 
    NumSpaces = SpacePerBlock - DigitOfCurrentNumber
    if NumSpaces % 2 == 0:
        NumSpaceRight = NumSpaces // 2
        NumSpaceLeft = NumSpaces // 2 
    else:
        NumSpaceRight = NumSpaces // 2
        NumSpaceLeft = NumSpaceRight + 1
    return NumSpaceLeft, NumSpaceRight

def FindDashes(SpacePerBlock, LengthPerSide):
    return SpacePerBlock * LengthPerSide + (LengthPerSide - 1) 

def CreateTestBoard(board, LengthPerSide):
    output = ""
    digits = CountDigit(board[-1])
    SpacePerBlock = digits + 2
    NumDashes = FindDashes(SpacePerBlock, LengthPerSide)
    dashes = "-" * NumDashes
    for i in range(len(board)):
        DigitOfCurrentNumber = CountDigit(board[i])
        NumSpaceLeft = FindSpaces(DigitOfCurrentNumber, SpacePerBlock, LengthPerSide)[0]
        NumSpaceRight = FindSpaces(DigitOfCurrentNumber, SpacePerBlock, LengthPerSide)[1]
        output += " " * NumSpaceLeft + str(board[i]) + " " * NumSpaceRight
        if (i+1) % LengthPerSide != 0:
            output += "|"
        else:
            output += "\n" + "-" * NumDashes + "\n"
    return output
