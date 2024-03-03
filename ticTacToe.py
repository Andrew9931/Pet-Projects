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

import PySimpleGUI as sg
from boardTicTacToe import boardForTicTacToe
from playersTicTacToe import playerTicTacToe

class TicTacToeGUI:
    def initInterface(self):
        self.layoutMainMenu = [
            [sg.Text('Добро пожаловать в игру крестики-нолики!', size=(14, 1), justification='center', font=('Helvetica', 20), relief=sg.RELIEF_RIDGE)],
            [sg.Button('Начать игру', size=(20, 2), font=('Helvetica', 14))],
            [sg.Button('Профиль', size=(20, 2), font=('Helvetica', 14))],
            [sg.Button('Выход', size=(20, 2), font=('Helvetica', 14))]
        ]

    def initProfile(self):
        self.layoutProfile = [
            [sg.Button('Nice day my lord!', size=(20, 2), font=('Helvetica', 14))],
            [sg.Text('Введите имя, мой лорд', size=(20, 2), font=('Helvetica', 14))],
            [sg.InputText(size=(20, 1), key='-NAME-', tooltip='Введите ваше имя в это поле')],
            [sg.Button('Выберите Аватарку, милорд', key='-AVATAR-', size=(20, 2), font=('Helvetica', 14))],
            [sg.Button('Возвращение в замок', size=(20, 2), font=('Helvetica', 14))]
        ]

    def runProfile(self):
        windowProfile = sg.Window('Профиль', self.layoutProfile)
        while True:
            event, values = windowProfile.read()
            if event == sg.WIN_CLOSED or event == 'Возвращение в замок':
                windowProfile.close()
                break
            if event == '-AVATAR-' and values['-NAME-'] != '':
                profileName = values['-NAME-']  # Получаем текст из поля ввода
                self.createProfile = playerTicTacToe()  #  Экземпляр класса
                self.createProfile.newPlayer(profileName)

                message = f"""
                Милорд, вот краткая информация о Вашем Сиятельстве:
                {self.createProfile.playerName}
                {self.createProfile.playerTytle}
                Число очков на данный момент:{self.createProfile.playerScore}.
                На этом всё, ваша светлость.
                """
                sg.popup(message, font=('Helvetica', 14), title='Информация')
                #self.createGameBoard.victory()  ##########################  and event == '-NAME-'
            windowProfile.close()


    def runMenu(self):
        windowMainMenu = sg.Window('Главное меню', self.layoutMainMenu)
        while True:
            event, values = windowMainMenu.read()
            if event == sg.WIN_CLOSED or event == 'Выход':
                break
            if event == 'Начать игру':
                windowMainMenu.close()
                self.runGame()
            if event == 'Профиль':
                self.initProfile()
                self.runProfile()
        windowMainMenu.close()

    def runGame(self):
        self.createGameBoard = boardForTicTacToe()  #  Короче тут мы создаём экземпляр класса, затем инициируем доску
        self.createGameBoard.initBoard()
        gameBoard = self.createGameBoard.gameBoard  #  Передаём доску в переменную, над которой совершаем действия
        layoutGame = self.createGameLayout(gameBoard) #  Создаём окно вызывая функцию класса, и в качестве аргумента передаём доску
        window = sg.Window('Крестики-нолики', layoutGame)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Выход':
                break
            if event == 'Новая игра':
                gameBoard = self.createGameBoard.initBoard()  #  чистим доску
                self.updateBoard(window)  #  вызываем функцию очищающую кнопки
                #print(gameBoard)

            #  Здесь нужно добавить ходы
            if isinstance(event, tuple):  # Если залетаем кортеж из event, то мы его ловим
                row, col = event  # передаём/распаковываем его данные в row, col
                window[event].update('X')  # Здесь мы ловим кнопку на которую нажали (event) и присваеваем Х вместо " "
                gameBoard[row + '-' + col] = 'X'  # gameBoard - это доска, row-col - координаты, например как top-L или low-R в словаре.
                print('Нажата кнопка в ячейке: ', {row}, {col})  # а здесь просто выводим распакованную информацию
                self.checkWin()
        window.close()

    # Метод для проверки победы
    def checkWin(self):
        self.createGameBoard.victory()

    def updateBoard(self, window):  # Метод для очистки кнопок доски
        gameBoard = self.createGameBoard.gameBoard
        for row in ['top', 'mid', 'low']:
            for col in ['L', 'M', 'R']:
                window[(row, col)].update(gameBoard[row + '-' + col])

    # Метод для переключения игрока (пример, нужно доработать)
    def switch_player(self):
        self.current_player = 'X' if self.current_player == 'O' else 'O'

    def createGameLayout(self, incomingGameBoard):
        return [
            [sg.Button(incomingGameBoard[row + '-' + col], size=(10, 5), key=(row, col)) for col in ['L', 'M', 'R']] for row in ['top', 'mid', 'low']
        ] + [[sg.Button('Новая игра'), sg.Button('Выход')]]

openWindow = TicTacToeGUI()
openWindow.initInterface()
openWindow.runMenu()
