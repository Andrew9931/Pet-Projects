from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from musicTicTacToe import SoundPlayer

from kivy.config import Config
Config.set('graphics', 'width', 1920)
Config.set('graphics', 'height', 1080)

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')

        sound_player = SoundPlayer()  #  Музыка
        layout.add_widget(sound_player)

        buttonStart = Button(text = 'Начать игру', 
                      font_size = 30,
                      bold = True,
                      on_press = self.start_btn_press,
                      background_color = [0, 0, 0, 0],
                      color=[.32, .10, 1, 1])
        
        buttonProfile = Button(text = 'Профиль', 
                      font_size = 30,
                      bold = True,
                      on_press = self.profile_btn_press,
                      background_color = [0, 0, 0, 0],
                      color=[.32, .10, 1, 1])

        buttonCheckConnection = Button(text = 'Проверить соединение', 
                      font_size = 30,
                      bold = True,
                      on_press = self.check_connect_btn_press,
                      background_color = [0, 0, 0, 0],
                      color=[.32, .10, 1, 1])

        buttonExit = Button(text = 'Выход', 
                      font_size = 30,
                      bold = True,
                      on_press = self.exit_btn_press,
                      background_color = [0, 0, 0, 0],
                      color=[.32, .10, 1, 1])

        layout.add_widget(buttonStart)
        layout.add_widget(buttonProfile)
        layout.add_widget(buttonCheckConnection)
        layout.add_widget(buttonExit)

        #  Установка изображения в качестве фона приложения
        with layout.canvas.before:
            background = Image(source='C:\pyProgramming\pyProjects\TicTacToeImages\mainMenuWallpaper.jpg', 
                               allow_stretch=True,
                               size=(1920, 1080))
            layout.bind(size=background.setter('size'))
            layout.bind(pos=background.setter('pos'))

        #  Загрузка и воспроизведения музыки в главно меню

        return layout
    
    def start_btn_press(self, instance):
        print('Кнопка Начать игру была нажата')
        instance.text = 'Игра начата'

    def profile_btn_press(self, instance):
        print('Кнопка Профиль была нажата')
        instance.text = 'Переход к Профилю'

    def check_connect_btn_press(self, instance):
        print('Кнопка Проверить соединение была нажата')
        instance.text = 'Кнопка Проверить соединение была нажата'

    def exit_btn_press(self, instance):
        print('Кнопка Выход была нажата')
        instance.text = 'Выход из игры'
        self.stop()

MyApp().run()



