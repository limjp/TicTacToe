def CreateLengthPerSide():    
    global LengthPerSide
    LengthPerSide = input("What should be the length of the board?" + "\n" + ">> ") 
    while not(LengthPerSide.isdigit()) or int(LengthPerSide) > 30 or int(LengthPerSide) < 3:
        LengthPerSide = input("Please input a number between 3 and 30." + "\n" + ">> ")
    LengthPerSide = int(LengthPerSide)

def CreatePlayerOne():
    global PlayerOne
    PlayerOne = input("Enter name for Player 1:" + "\n" + ">> ")

def CreatePlayerTwo():
    global PlayerTwo
    PlayerTwo = input("Enter name for Player 2:" + "\n" + ">> ")

def CreateBoard():
    global board 
    board = [i for i in range(1, LengthPerSide**2 + 1)]

def CreateCurrentPlayer():
    global CurrentPlayer
    CurrentPlayer = PlayerOne

def CreateWinner():
    global winner 
    winner = None

def CreateGameStillGoing():
    global GameStillGoing
    GameStillGoing = True

def CreateGlobalVariables():
    CreateGameStillGoing()
    CreateWinner()
    CreateLengthPerSide()
    CreatePlayerOne()
    CreatePlayerTwo()
    CreateCurrentPlayer()
    CreateBoard()

def DisplayBoard():
    '''
        Displays the board for the user. The format of the board here would be a series of squares divided by a vertical line.
        Each row is also divided by a series of "-"
        
        Logic:
            (a) Determine the number of characters each square requires. This can be determined by finding how many digits the last (and thus greatest)
                number of the board takes up, and adding 2 spaces to that. 
            (b) Determine the number of dashes required to divide each row of the board.
            (c) Determine the number of spaces to be printed given a certain number.
            (d) Print the board with (a), (b) and (c).

        Dependent Functions: 
            (a) FindDashes
            (b) FindSpaces

        Global Variables Referenced:
            (a) LengthPerSide 
    '''
    digits = CountDigit(board[-1])
    SpacePerBlock = digits + 2
    NumOfDashes = FindDashes(SpacePerBlock)
    for i in range(len(board)):
        DigitOfCurrentNumber = CountDigit(board[i])
        NumSpaceLeft = FindSpaces(DigitOfCurrentNumber, SpacePerBlock)[0]
        NumSpaceRight = FindSpaces(DigitOfCurrentNumber, SpacePerBlock)[1]
        print(" " * NumSpaceLeft, end = "")
        print(board[i], end = "")
        print(" " * NumSpaceRight, end = "")
        if (i + 1) % LengthPerSide != 0:
            print("|", end = "")
        else:
            print("\n" + "-" * NumOfDashes) 

def CountDigit(element):
    '''
        Returns the length of element if it is a string or the number of digits if element is an int.
        Both str and int are accepted as while board starts off as an array of integers, it can be replaced 
        by either X or Y. 

        Parameters:
            element: Either an int or str 
        
        Returns:
            count (int): The lenght of element if it is a string. The number of digits if element is an int.
    '''
    if type(element) == int:
        count = 0
        while int(element) > 0:
            count += 1
            element = element // 10
    elif type(element) == str:
        count = len(element)
    return count

def FindSpaces(DigitOfCurrentNumber, SpacePerBlock):
    '''
        Returns the number of spaces to be printed on the left and right of a given number.

        Parameters:
            DigitOfCurrentNumber (int) : An integer 
            SpacePerBlock (int) : An integer
        
        Returns:
            NumSpaceLeft (int) : An integer showing the number of space to be printed on the left of the current number.
            NumSpaceRight (int) : An integer showing the number of space to be printed on the right of the current number.
    '''    
    NumSpaces = SpacePerBlock - DigitOfCurrentNumber
    if NumSpaces % 2 == 0:
        NumSpaceRight = NumSpaces // 2
        NumSpaceLeft = NumSpaces // 2 
    else:
        NumSpaceRight = NumSpaces // 2
        NumSpaceLeft = NumSpaceRight + 1
    return NumSpaceLeft, NumSpaceRight

def FindDashes(SpacePerBlock):
    '''
        Returns the number of dashes to be printed after every row.

        Parameters:
            SpacePerBlock (int) : An integer representing the amount of space each square requires.
        
        Returns 
            (int) : An integer showing the number of dashes to print.
    '''    
    return SpacePerBlock * LengthPerSide + (LengthPerSide - 1) 

def HandleTurn():
    '''
        Asks for user input for which position on the board do they wish to choose. Place user's symbol - either X or O - on that 
        position in the global variable board.
    '''    
    if CurrentPlayer == PlayerOne:
        position = input("{} choose a box to place an 'x' into:".format(CurrentPlayer) + "\n" + ">> ")
    else:
        position = input("{} choose a box to place an 'o' into:".format(CurrentPlayer) + "\n" + ">> ")
    while not(position.isdigit()):
        position = input("Please input a number" + "\n" + ">> ")
    while int(position) not in board:
        position = input("Please choose a free space on the board." + "\n" + ">> ")
    position = int(position) - 1
    if CurrentPlayer == PlayerOne:
        board[position] = "X"
    else:
        board[position] = "O"

    DisplayBoard()

def CheckGameOver():
    '''
        Determines whether the game is still ongoing.
        
        Dependent Functions:
            (a) CheckWinner
            (b) CheckTie
        
        Note
            Order of the function must be CheckWinner followed by CheckTie.
            The latter cannot occur without the former. 
    '''    
    CheckWinner()
    CheckTie()

def CheckWinner():
    '''
        Determines if there is a winner. If there is, change the global variable winner from None to 
        the name of the winner.

        Dependent Functions:
            (a) RowWinner
            (b) ColumnWinner
            (c) DiagonalWinner
    '''    
    global winner 
    RowWinner = CheckRows()
    ColumnWinner = CheckColumns()
    DiagonalWinner = CheckDiagonals()

    if RowWinner:
        winner = RowWinner
    elif ColumnWinner:
        winner = ColumnWinner
    elif DiagonalWinner:
        winner = DiagonalWinner
    else:
        winner = None
    return

def CheckRows():
    '''
        Check each row to determine if there are 3 squares with the same character.

        Logic:
            (a) Starting from the 2nd square of each row till the 2nd last square of each row, check whether the current 
                square matches the ones before and after it.
            (b) If yes, there is a win. Change global variable GameStillGoing from True to False
        
        Returns
            If no winner, returns None.
            If winner, returns name of player. 
        
        Note:
            (a) Count represents the number of rows required to be checked.
            (b) Start and end refer to the index of global variable board which represents the element in each square. 
                Does not represent the current number within the board.
    '''    
    global GameStillGoing
    start = 1
    end = LengthPerSide - 1
    count = 0
    while count < LengthPerSide:
        for i in range(start + (LengthPerSide * count), end + (LengthPerSide * count)):
            row = board[i] == board[i - 1] == board[i + 1]
            if row:
                GameStillGoing = False
                if board[i] == "X":
                    return PlayerOne
                else:
                    return PlayerTwo
        count += 1

def CheckColumns():
    '''
        Check each column to determine if there are 3 squares with the same character.

        Logic:
            (a) Starting from the 2nd square of each column till the 2nd last square of each column, check whether the current 
                square matches the ones before and after it.
            (b) If yes, there is a win. Change global variable GameStillGoing from True to False
        
        Returns
            If no winner, returns None.
            If winner, returns name of player. 
        
        Note:
            (a) Count represents the number of columns required to be checked.
            (b) Start and end refer to the index of global variable board which represents the element in each square. 
                Does not represent the current number within the board.
    '''      
    global GameStillGoing
    start = LengthPerSide
    end = LengthPerSide * 2
    count = 0

    while count < LengthPerSide - 2:
        for i in range(start + (LengthPerSide * count), end + (LengthPerSide * count)):
            column = board[i] == board[i - LengthPerSide] == board[i + LengthPerSide]
            if column:
                GameStillGoing = False
                if board[i] == "X":
                    return PlayerOne
                else:
                    return PlayerTwo
        count += 1

def CheckDiagonals():
    '''
        Check each diagonal to determine if there are 3 squares with the same character.

        Logic:
            (a) Starting from the 2nd row of the 2nd column till the 2nd last square row of the 2nd last column
                check whether the squares diagonal to the current square are of the same character. 
            (b) If yes, there is a win. Change global variable GameStillGoing from True to False
        
        Returns
            If no winner, returns None.
            If winner, returns name of player. 
        
        Note:
            (a) Count represents the number of diagonals required to be checked.
            (b) Start and end refer to the index of global variable board which represents the element in each square. 
                Does not represent the current number within the board.
    '''      
    global GameStillGoing
    start = LengthPerSide + 1
    end = LengthPerSide * 2 - 1
    count = 0 

    while count < LengthPerSide - 2:
        for i in range(start + (LengthPerSide * count), end + (LengthPerSide * count)):
            diagonal1 = board[i] == board[i - LengthPerSide - 1] == board[i + LengthPerSide + 1]
            diagonal2 = board[i] == board[i - LengthPerSide + 1] == board[i + LengthPerSide - 1]
            if diagonal1 or diagonal2:
                GameStillGoing = False
                if board[i] == "X":
                    return PlayerOne
                else:
                    return PlayerTwo
        count += 1

def CheckTie():
    '''
        Check if a tie has occured. If yes, change the gloabl variable GameStillGoing from True to False.
    '''     
    global GameStillGoing
    for element in board:
        if type(element) == int:
            return
    GameStillGoing = False

def ChangeTurn():
    '''
        Change the global variable CurrentPlayer so that HandleTurn works correctly.
    '''     
    global CurrentPlayer
    if CurrentPlayer == PlayerOne:
        CurrentPlayer = PlayerTwo
    elif CurrentPlayer == PlayerTwo:
        CurrentPlayer = PlayerOne
    return

def PlayGame():
    '''
        Starts the game.
    '''     
    CreateGlobalVariables()
    DisplayBoard()
    while GameStillGoing:
        HandleTurn()
        CheckGameOver()
        ChangeTurn()
    
    if winner == PlayerOne or winner == PlayerTwo:
        print("Congratulations", winner + "!", "You have won.")
    elif winner == None:
        print("The game is tied!")
