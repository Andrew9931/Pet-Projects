from playersTicTacToe import playerTicTacToe
from boardTicTacToe import boardForTicTacToe

createGameBoard = boardForTicTacToe()
createGameBoard.preInitBoard()
createGameBoard.initBoard()

createPlayer = playerTicTacToe()
createPlayer.newBoard(createGameBoard)

createPlayer.newPlayer('Никита')
createPlayer.sideChooser(2)
createPlayer.moveChooser(2)

createPlayer.playersMove()

createGameBoard.printBoard()
createGameBoard.victory()
