from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

from musicTicTacToe import SoundPlayer

from kivy.config import Config
Config.set('graphics', 'width', 1920)
Config.set('graphics', 'height', 1080)

# Создаем экраны
class MainMenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

# Управление экранами
class ScreenManagement(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()

        main_menu = MainMenuScreen(name='main')
        layout_main = BoxLayout(orientation = 'vertical')  #  Захуярить текст с левой стороны

        self.sound_player = SoundPlayer()  #  Музыка
        self.sound_player.play_ambient_sound('mainMenuTheme.wav')

        buttonStart = Button(text = 'Начать игру', 
                      font_size = 50,
                      bold = True,
                      on_press = self.start_btn_press,
                      background_color = [0, 0, 0, 0],
                      color=[0, 0.26, 0.26, 1])
        
        buttonProfile = Button(text = 'Профиль', 
                      font_size = 50,
                      bold = True,
                      on_press = self.profile_btn_press,
                      background_color = [0, 0, 0, 0],
                      color=[0, 0.26, 0.26, 1])

        buttonCheckConnection = Button(text = 'Проверить соединение', 
                      font_size = 50,
                      bold = True,
                      on_press = self.check_connect_btn_press,
                      background_color = [0, 0, 0, 0],
                      color=[0, 0.26, 0.26, 1])

        buttonExit = Button(text = 'Выход', 
                      font_size = 50,
                      bold = True,
                      on_press = self.exit_btn_press,
                      background_color = [0, 0, 0, 0],
                      color=[0, 0.26, 0.26, 1])

        layout_main.add_widget(buttonStart)
        layout_main.add_widget(buttonProfile)
        layout_main.add_widget(buttonCheckConnection)
        layout_main.add_widget(buttonExit)

        #  Установка изображения в качестве фона приложения
        with layout_main.canvas.before:
            background = Image(source='C:\pyProgramming\pyProjects\TicTacToeImages\mainMenuWallpaper.jpg', 
                               allow_stretch=True,
                               size=(1920, 1080))
            layout_main.bind(size=background.setter('size'))
            layout_main.bind(pos=background.setter('pos'))

        #  Загрузка и воспроизведения музыки в главно меню

        return layout_main

    def start_btn_press(self, instance):
        self.sound_player.play_choicen_sound('clickSound.wav')
        print('Кнопка Начать игру была нажата')
        instance.text = 'Игра начата'

    def profile_btn_press(self, instance):
        self.sound_player.play_choicen_sound('clickSound.wav')
        print('Кнопка Профиль была нажата')
        instance.text = 'Переход к Профилю'

    def check_connect_btn_press(self, instance):
        self.sound_player.play_choicen_sound('clickSound.wav')
        print('Кнопка Проверить соединение была нажата')
        instance.text = 'Кнопка Проверить соединение была нажата'

    def exit_btn_press(self, instance):
        print('Кнопка Выход была нажата')
        instance.text = 'Выход из игры'
        self.stop()

MyApp().run()
