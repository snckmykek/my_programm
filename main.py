import kivy
from kivy.app import App

from kivy.config import Config
Config.set('graphics', 'resizable', '1');
Config.set('graphics', 'width', '360');
Config.set('graphics', 'height', '640');

import containers

class MainScreenApp(App):
    
    def build(self):
        pass

if __name__=="__main__":
    MainScreenApp().run() 
