from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout

class SoundPlayer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.play_sound()

    def play_sound(self):
        sound = SoundLoader.load('mainMenuTheme.wav')
        if sound:
            sound.play()