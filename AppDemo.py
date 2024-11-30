from docutils.parsers.rst.directives.tables import align
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.icon_definitions import md_icons
from kivy.lang import Builder
import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.config import Config
Config.set('graphics', 'resizable', True)

class HelloKivyApp(MDApp):

#build is the 'public static' like in java but for kivy
    def build(self):
        #create screen object
        screen = Screen()

        #create buttons
        #MD's below are classes imported from the kivymd package

       #button1 = MDFlatButton(text = "Welcome to the Recipe Generator", pos_hint={'center_x': 0.5, 'center_y': 0.8})

        #button2 = MDFloatingActionButton(icon = "android", pos_hint={'center_x': 0.5, 'center_y': 0.5})

        #label = MDLabel(text = "Hello World!", pos_hint={'center_x': .95, 'center_y': 0.2}, font_size = '20sp', color = (0.41, 0.42, 0.74, 1))

        #screen.add_widget(label)

        #screen.add_widget(button1)
        #screen.add_widget(button2)

        # add button in corner for users to switch btwn themes?
        self.theme_cls.theme_style = "Dark"

        labelFont = MDLabel(text = "Welcome to the Recipe Generator", theme_text_color = "Custom", text_color =(0.5, 0.5, 0.5, 1), font_style = 'H3', pos_hint={'center_x': 0.56, 'center_y': 0.9})

        screen.add_widget(labelFont)

        screen.add_widget(self.pictures())

        return screen

    def pictures(self):
        screen = Screen()

        self.img = Image(source='recipe.jpg')

        self.img.size_hint_x = 1
        self.img.size_hint_y = 1

        self.img.pos = (450,500)

        pic = Widget()
        pic.add_widget(self.img)
        return pic

HelloKivyApp().run()
