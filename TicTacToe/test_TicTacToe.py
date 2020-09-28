import unittest
from unittest.mock import patch
import moves
from io import StringIO
import TestingFunctions 
import sys

class TestTicTacToe(unittest.TestCase):
    
    @patch("moves.CreateLengthPerSide")
    @patch("moves.CreatePlayerOne")
    @patch("moves.CreatePlayerTwo")
    @patch("moves.CreateBoard")
    @patch("moves.CreateCurrentPlayer")
    @patch("moves.CreateWinner")
    @patch("moves.CreateGameStillGoing")
    def test_CreateGlobalVariables(self, mock_CreateLengthPerSide, mock_CreatePlayerOne, mock_CreatePlayerTwo, mock_CreateBoard, mock_CreateCurrentPlayer, mock_CreateWinner, mock_CreateGameStillGoing):
        moves.CreateGlobalVariables()
        self.assertTrue(mock_CreateLengthPerSide.called)
        self.assertTrue(mock_CreatePlayerOne.called)
        self.assertTrue(mock_CreatePlayerTwo.called)
        self.assertTrue(mock_CreateBoard.called)
        self.assertTrue(mock_CreateCurrentPlayer.called)
        self.assertTrue(mock_CreateWinner.called)
        self.assertTrue(mock_CreateGameStillGoing.called)

    def test_CountDigit(self): 
        self.assertEqual(moves.CountDigit(100), 3)
        self.assertEqual(moves.CountDigit(10), 2)
        self.assertEqual(moves.CountDigit(1), 1)
        self.assertEqual(moves.CountDigit("X"), 1)
        self.assertEqual(moves.CountDigit("Y"), 1)
    
    def test_FindSpaces(self):
        self.assertEqual(moves.FindSpaces(1, 4), (2,1))
        self.assertEqual(moves.FindSpaces(2, 4), (1,1))
        self.assertEqual(moves.FindSpaces(1, 5), (2,2))
        self.assertEqual(moves.FindSpaces(2, 5), (2,1))
    
    def test_FindDashes(self):
        moves.LengthPerSide = 4
        self.assertEqual(moves.FindDashes(3),15)
        self.assertEqual(moves.FindDashes(4),19)
        self.assertEqual(moves.FindDashes(5),23)

    def test_FindDashes(self):
        moves.LengthPerSide = 15
        self.assertEqual(moves.FindDashes(3),59)
        self.assertEqual(moves.FindDashes(4),74)
        self.assertEqual(moves.FindDashes(5),89)

    def test_DisplayBoard(self):
        ExpectedOutput = TestingFunctions.CreateTestBoard([i for i in range(1,10)], 3)

        moves.LengthPerSide = 3
        moves.board = [i for i in range(1, moves.LengthPerSide ** 2 + 1)]
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        moves.DisplayBoard()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), ExpectedOutput)

    def test_DisplayBoard(self):
        ExpectedOutput = TestingFunctions.CreateTestBoard([i for i in range(1,17)], 4)
        
        moves.LengthPerSide = 4
        moves.board = [i for i in range(1, moves.LengthPerSide ** 2 + 1)]
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        moves.DisplayBoard()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), ExpectedOutput)

    def test_DisplayBoard(self):
        ExpectedOutput = TestingFunctions.CreateTestBoard([i for i in range(1,226)], 15)
        
        moves.LengthPerSide = 15
        moves.board = [i for i in range(1, moves.LengthPerSide ** 2 + 1)]
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        moves.DisplayBoard()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), ExpectedOutput)  

    @patch("moves.CheckWinner")
    @patch("moves.CheckTie")
    def test_CheckGameOver(self, mock_CheckWinner, mock_CheckTie):
        moves.CheckGameOver()
        self.assertTrue(mock_CheckWinner.called)
        self.assertTrue(mock_CheckTie.called)
    
    @patch("moves.CheckRows")
    @patch("moves.CheckColumns")
    @patch("moves.CheckDiagonals")
    def test_CheckWinner(self, mock_CheckRows, mock_CheckColumns, mock_CheckDiagonals):
        moves.CheckWinner()
        self.assertTrue(mock_CheckRows.called)
        self.assertTrue(mock_CheckColumns.called)
        self.assertTrue(mock_CheckDiagonals.called)
    
    def test_CheckRows(self):
        moves.PlayerOne = "PlayerOne"
        moves.PlayerTwo = "PlayerTwo"
        moves.GameStillGoing = True
        moves.LengthPerSide = 4
        moves.board = [i for i in range(1,17)]
        moves.board[1] = "X"
        moves.board[2] = "X"
        moves.board[3] = "X"
        moves.CheckRows()
        self.assertFalse(moves.GameStillGoing)
        self.assertEqual(moves.CheckRows(), moves.PlayerOne)

    def test_CheckRows(self):
        moves.PlayerOne = "PlayerOne"
        moves.PlayerTwo = "PlayerTwo"
        moves.GameStillGoing = True
        moves.LengthPerSide = 4
        moves.board = [i for i in range(1,17)]
        moves.board[4] = "O"
        moves.board[5] = "O"
        moves.board[6] = "O"
        moves.CheckRows()
        self.assertFalse(moves.GameStillGoing)
        self.assertEqual(moves.CheckRows(), PlayerTwo)

    def test_CheckRows(self):
        moves.PlayerOne = "PlayerOne"
        moves.PlayerTwo = "PlayerTwo"
        moves.GameStillGoing = True
        moves.LengthPerSide = 4
        moves.board = [i for i in range(1,17)]
        moves.board[0] = "X"
        moves.board[1] = "X"
        moves.board[4] = "X"
        moves.CheckRows()
        self.assertTrue(moves.GameStillGoing)
        self.assertIsNone(moves.CheckRows()) 
    
    def test_CheckColumns(self):
        moves.PlayerOne = "PlayerOne"
        moves.PlayerTwo = "PlayerTwo"
        moves.GameStillGoing = True
        moves.LengthPerSide = 4
        moves.board = [i for i in range(1,17)]
        moves.board[0] = "X"
        moves.board[4] = "X"
        moves.board[8] = "X"
        moves.CheckColumns()
        self.assertFalse(moves.GameStillGoing)    
        self.assertEqual(moves.CheckColumns(), moves.PlayerOne)

    def test_CheckColumns(self):
        moves.PlayerOne = "PlayerOne"
        moves.PlayerTwo = "PlayerTwo"
        moves.GameStillGoing = True
        moves.LengthPerSide = 4
        moves.board = [i for i in range(1,17)]
        moves.board[0] = "O"
        moves.board[4] = "O"
        moves.board[8] = "O"
        moves.CheckColumns()
        self.assertFalse(moves.GameStillGoing)    
        self.assertEqual(moves.CheckColumns(), moves.PlayerTwo)

    def test_CheckColumns(self):
        moves.PlayerOne = "PlayerOne"
        moves.PlayerTwo = "PlayerTwo"
        moves.GameStillGoing = True
        moves.LengthPerSide = 4
        moves.board = [i for i in range(1,17)]
        moves.board[0] = "X"
        moves.board[6] = "X"
        moves.board[8] = "O"
        moves.CheckColumns()
        self.assertTrue(moves.GameStillGoing)    
        self.assertIsNone(moves.CheckColumns())

    def test_CheckDiagonals(self):
        moves.PlayerOne = "PlayerOne"
        moves.PlayerTwo = "PlayerTwo"
        moves.GameStillGoing = True
        moves.LengthPerSide = 4
        moves.board = [i for i in range(1,17)]
        moves.board[0] = "X"
        moves.board[5] = "X"
        moves.board[10] = "X"
        moves.CheckDiagonals()
        self.assertFalse(moves.GameStillGoing)    
        self.assertEqual(moves.CheckDiagonals(), moves.PlayerOne)

    def test_CheckDiagonals(self):
        moves.PlayerOne = "PlayerOne"
        moves.PlayerTwo = "PlayerTwo"
        moves.GameStillGoing = True
        moves.LengthPerSide = 4
        moves.board = [i for i in range(1,17)]
        moves.board[0] = "O"
        moves.board[5] = "O"
        moves.board[10] = "O"
        moves.CheckDiagonals()
        self.assertFalse(moves.GameStillGoing)    
        self.assertEqual(moves.CheckDiagonals(), moves.PlayerTwo)

    def test_CheckDiagonals(self):
        moves.PlayerOne = "PlayerOne"
        moves.PlayerTwo = "PlayerTwo"
        moves.GameStillGoing = True
        moves.LengthPerSide = 4
        moves.board = [i for i in range(1,17)]
        moves.board[0] = "X"
        moves.board[6] = "X"
        moves.board[8] = "O"
        moves.CheckColumns()
        self.assertTrue(moves.GameStillGoing)    
        self.assertIsNone(moves.CheckDiagonals())
    
    def test_CheckTie(self):
        for x in range(3, 31):
            moves.board = [i for i in range(1, x ** 2 + 1)]
            moves.GameStillGoing = True
            moves.CheckTie()
            self.assertTrue(moves.GameStillGoing)
     
    def test_CheckTie(self):
        for x in range(3,31):
            moves.GameStillGoing = True
            moves.board = [i for i in range(1, x ** 2 + 1)]
            moves.board[x] == "X"
            moves.CheckTie()
            self.assertTrue(moves.GameStillGoing) 

    def test_CheckTie(self):
        moves.GameStillGoing = True
        moves.board = ["X", "Y", "X",
                           "Y", "X", "Y", 
                           "X", "X", "Y"]
        self.assertTrue(moves.GameStillGoing)
    
    def test_ChangeTurn(self):
        moves.PlayerOne = "PlayerOne"
        moves.PlayerTwo = "PlayerTwo"
        moves.CurrentPlayer = moves.PlayerOne
        moves.ChangeTurn()
        self.assertEqual(moves.CurrentPlayer, moves.PlayerTwo)

    def test_ChangeTurn(self):
        moves.PlayerOne = "PlayerOne"
        moves.PlayerTwo = "PlayerTwo"
        moves.CurrentPlayer = moves.PlayerTwo
        moves.ChangeTurn()
        self.assertEqual(moves.CurrentPlayer, moves.PlayerOne)

    @patch("moves.CreateGlobalVariables")
    @patch("moves.DisplayBoard")
    @patch("moves.HandleTurn")
    @patch("moves.CheckGameOver")
    @patch("moves.ChangeTurn")
    def test_PlayGame(self, mock_CreateGlobalVariables, mock_DisplayBoard, mock_HandleTurn, mock_CheckGameOver, mock_ChangeTurn):
        moves.PlayGame()
        self.assertTrue(mock_CreateGlobalVariables.called)
        self.assertTrue(mock_DisplayBoard.called)
        self.assertTrue(mock_HandleTurn.called)
        self.assertTrue(mock_CheckGameOver.called)
        self.assertTrue(mock_ChangeTurn.called)

    @patch("moves.CreateGlobalVariables")
    @patch("moves.DisplayBoard")    
    def test_PlayGame(self, mock_CreateGlobalVariables, mock_DisplayBoard):
        moves.PlayerOne = "PlayerOne"
        moves.GameStillGoing = False
        moves.winner = moves.PlayerOne
        ExpectedOutput = "Congratulations PlayerOne! You have won.\n"
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        moves.PlayGame()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), ExpectedOutput)

    @patch("moves.CreateGlobalVariables")
    @patch("moves.DisplayBoard")    
    def test_PlayGame(self, mock_CreateGlobalVariables, mock_DisplayBoard):
        moves.PlayerTwo = "PlayerTwo"
        moves.GameStillGoing = False
        moves.winner = moves.PlayerTwo
        ExpectedOutput = "Congratulations PlayerTwo! You have won.\n"
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        moves.PlayGame()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), ExpectedOutput)

if __name__ == '__main__':
    unittest.main() 