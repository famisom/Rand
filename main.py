from kivy.app import App
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import random

KV = """
MyBL:

        first: first
        end: end

        orientation: "vertical"

        Label:
                font_size: "40sp"
                text: "Randomizer"
                color: '#008f8f'
                pos: (0, 200)
                bold: True

        Label:
                font_size: "60sp"
                text: root.data_label
                color: '#ffffff'
                pos: (0, 30)
                bold: True

        TextInput:
                id: first
                multiline: False
                size_hint: (0.4, 0.07)
                pos: (0, 150)
                pos_hint: {"center_x": 0.25} 
                background_color: '#222530'
                font_size: "23sp"
                on_text: self.foreground_color = '#ffffff'

        TextInput:
                id: end
                multiline: False
                size_hint: (0.4, 0.07)
                pos: (0, 150)
                pos_hint: {"center_x": 0.75} 
                background_color: '#222530'
                color: '#ffffff'
                font_size: "23sp"
                on_text: self.foreground_color = '#ffffff'

        Button:
                text: "Get Result"
                background_color: (0, 1, 1, 1)
                font_size: "20sp"
                bold: True
                size_hint: (0.9, 0.15)
                pos: (0, 30)
                pos_hint: {"center_x": 0.5}
                on_press: root.random()
"""

class MyBL(RelativeLayout):

        Window.clearcolor = '#1f212a'

        data_label = StringProperty('Number')

        def random(self):
            number = random.randint(int(self.first.text), int(self.end.text))
            self.data_label = str(number)

class MyApp(App):

        running = True

        def build(self):

                return Builder.load_string(KV)

        def on_stop(self):
                self.running = False

MyApp().run()