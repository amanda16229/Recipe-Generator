from docutils.parsers.rst.directives.tables import align
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.icon_definitions import md_icons


class HelloKivyApp(MDApp):

#build is the 'public static' like in java but for kivy
    def build(self):
        #create screen object
        screen = Screen()

        #create buttons
        #MD's below are classes imported from the kivymd package

        button1 = MDFlatButton(text = "Hello Kivy", pos_hint={'center_x': 0.5, 'center_y': 0.8})

        button2 = MDFloatingActionButton(icon = "android", pos_hint={'center_x': 0.5, 'center_y': 0.5})

        label = MDLabel(text = "Hello World!", pos_hint={'center_x': .95, 'center_y': 0.2}, font_size = '20sp', color = (0.41, 0.42, 0.74, 1))

        labelFont = MDLabel(text = "Label with Different Font", theme_text_color = "Custom", text_color =(0.5, 0, 0.5, 1), font_style = 'H2')

        screen.add_widget(labelFont)

        screen.add_widget(label)

        screen.add_widget(button1)
        screen.add_widget(button2)

        return screen



#HelloKivyApp().run()

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class Kivy(App):
    def build(self):
        b = BoxLayout(orientation='vertical')

        t = TextInput(font_size = 50, size_hint_y = None, height = 100)
        b.add_widget(t)

        f = FloatLayout()
        b.add_widget(f)
        s = Scatter()
        b.add_widget(s)
        # l = Label(text = "Hello!", font_size = 50)
        # f.add_widget(s)
        # s.add_widget(l)
        #
        # b.add_widget(t)
        # b.add_widget(f)
        #
        # # Binding it with the label
        # t.bind(text=l.setter('text'))

        return b

Kivy().run()