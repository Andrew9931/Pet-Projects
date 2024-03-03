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
        # Создаем тексты для вывода слева сверху и справа сверху от кнопок
        left_top_text = sg.Text("Слева сверху", size=(10, 1))
        right_top_text = sg.Text("Справа сверху", size=(10, 1))


        # Создаем кнопки для игровой доски
        top_row_buttons = [sg.Button(incomingGameBoard['top-' + col], size=(10, 5), key=('top', col)) for col in ['L', 'M', 'R']]
        mid_row_buttons = [sg.Button(incomingGameBoard['mid-' + col], size=(10, 5), key=('mid', col)) for col in ['L', 'M', 'R']]
        low_row_buttons = [sg.Button(incomingGameBoard['low-' + col], size=(10, 5), key=('low', col)) for col in ['L', 'M', 'R']]

        # Создаем кнопки "Новая игра" и "Выход"
        new_game_button = sg.Button('Новая игра')
        exit_button = sg.Button('Выход')

        # Возвращаем разметку кнопок
        return [
        [left_top_text, right_top_text],
        top_row_buttons,
        mid_row_buttons,
        low_row_buttons,
        [new_game_button, exit_button]
        ]

openWindow = TicTacToeGUI()
openWindow.initInterface()
openWindow.runMenu()