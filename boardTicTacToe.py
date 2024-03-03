class boardForTicTacToe:

    def preInitBoard(self):
        self.gameBoard = {}  # Определение gameBoard как атрибута класса

    def initBoard(self):
        self.gameBoard = {'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
                          'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
                          'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' '}
        return self.gameBoard

    def printBoard(self):
        print(self.gameBoard.get('top-L') + '|' + self.gameBoard.get('top-M') + '|' + \
        self.gameBoard.get('top-R'))
        print('-+-+-')
        print(self.gameBoard.get('mid-L') + '|' + self.gameBoard.get('mid-M') + '|' + \
        self.gameBoard.get('mid-R'))
        print('-+-+-')
        print(self.gameBoard.get('low-L') + '|' + self.gameBoard.get('low-M') + '|' + \
        self.gameBoard.get('low-R'))

    victoryCombinations = [['top-L', 'top-M', 'top-R'],  #  Верхняя горизонталь
                           ['mid-L', 'mid-M', 'mid-R'],  #  Средняя горизонталь
                           ['low-L', 'low-M', 'low-R'],  #  Нижняя  горизонталь

                           ['top-L', 'mid-L', 'low-L'],  #  Левая   вертикаль
                           ['top-M', 'mid-M', 'low-M'],  #  Средняя вертикаль
                           ['top-R', 'mid-R', 'low-R'],  #  Правая  вертикаль

                           ['top-L', 'mid-M', 'low-R'],  #  Левая  Диагональ
                           ['low-L', 'mid-M', 'top-R']]  #  Правая  Диагональ

    def checkVictory(self):
        #values = set(self.gameBoard.values())
        for lst in self.victoryCombinations:
            if all(self.gameBoard[val] == 'X' for val in lst):
                return True
            elif all(self.gameBoard[val] == 'O' for val in lst):
                return True
        return False

    def victory(self):
        is_victory = self.checkVictory()
        if is_victory == True:
            print('ПЕРЕМОГА')


#createGameBoard = boardForTicTacToe()
#createGameBoard.preInitBoard()
#createGameBoard.initBoard()
#createGameBoard.printBoard()
