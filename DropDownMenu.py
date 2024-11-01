# Program to explain how to create drop-down in kivy

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# Importing Drop-down from the module to use in the program
from kivy.uix.dropdown import DropDown

# The Button is a Label with associated actions
# that are triggered when the button is pressed
# (or released after a click / touch)
from kivy.uix.button import Button

# another way used to run kivy app
from kivy.base import runTouchApp

# create a dropdown with 10 buttons
dropdown = DropDown()
for index in range(10):

    # Adding buttons in drop down list
    button = Button(text = 'Value % d' % index, size_hint_y = None, height = 40)

    # Binding button to show text when selected
    button.bind(on_release = lambda button: dropdown.select(button.text))

    # Add button inside dropdown
    dropdown.add_widget(button)

# create a big main button
main_button = Button(text = 'Main Menu', size_hint = (None, None), pos = (350, 300))

# show the dropdown menu when the main button is released
# note: all the bind() calls pass the instance of the caller
# (here, the mainbutton instance) as the first argument of the callback
# (here, dropdown.open.).
main_button.bind(on_release = dropdown.open)

# listen for the selection in the
# dropdown list and assign the data to the button text.
main_button.bind(on_select = lambda instance, x: setattr(main_button, 'text', x))

# If you pass only a widget in runtouchApp(), a Window will
# be created and your widget will be added to the window
# as the root widget.
runTouchApp(main_button)
