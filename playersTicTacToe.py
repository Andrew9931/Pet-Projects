import random

class playerTicTacToe:
    def newPlayer(self, name):
        self.playerName = name
        sobriquetNumber = random.randint(0, 4)
        sobriquets = ['Ощипанный Петух', 'Гроза Вечеринок', 'Приманка Для Раков',\
        'Трудяга', 'Сэр']
        self.playerTytle = sobriquets[sobriquetNumber]
        self.playerScore = 0
        print(self.playerName)
        print(self.playerTytle)
        print('Кол-во очков: ' + str(self.playerScore))

    def sideChooser(self, sideNumber):
        self.playerSide = 0
        if sideNumber == 0:  #Левая Сторона
            self.playerSide = 0
            print('Левая Сторона')
        elif sideNumber == 1:  #Правая Сторона
            self.playerSide = 1
            print('Правая Сторона')
        elif sideNumber == 2:  #Случайный Выбор Стороны
            self.playerSide = random.randint(1, 2)
            print('Случайный выбор стороны, ' + 'выбрана ' + str(self.playerSide))
        else:  #Неверно выбрана сторона, повторите ввод
            print('Неверно выбрана сторона, повторите ввод')

    def moveChooser(self, moveVariant):
        self.moveSymbol = 'empty'
        if moveVariant == 0:  #O
            self.moveSymbol = 'O'
            print('Играет O')
        elif moveVariant == 1:  #X
            self.moveSymbol = 'X'
            print('Играет X')
        elif moveVariant == 2:  #Случайный Выбор
            moveVariant = random.randint(0, 1)
            if moveVariant == 0:
                self.moveSymbol = 'O'
                print('Играет O')
            else:
                self.moveSymbol = 'X'
                print('Играет X')
        else:  #Неверно выбранo, повторите ввод
            self.moveSymbol = 'error variant'
            print('Неверно выбран символ, повторите ввод')

    def newBoard(self, gameBoard):
        self.gameBoard = gameBoard.gameBoard

    def playersMove(self):
        print('Ходит ' + self.playerName)
        self.gameBoard['top-M'] = 'X'
        self.gameBoard['mid-M'] = 'X'
        self.gameBoard['low-M'] = 'X'

#createPlayer = playerTicTacToe()
#createPlayer.newPlayer('Никита')
#createPlayer.sideChooser(2)
#createPlayer.moveChooser(2)

#createPlayer.newBoard()
#createPlayer.playersMove()
















