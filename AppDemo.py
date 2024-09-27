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
from uix.floatL

class Kivy(App):
    def build(self):
        label1 = Label(text="[color = ff3333][b]'Label'[/b] is Added [/color]\n[color = 3333ff]Screen !!:):):):)[ / color]",font_size = '20sp', markup = True)
        return label1
label = Kivy()
#label.run()

