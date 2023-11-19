from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty

class Runner(BoxLayout):
    value = NumericProperty(0)
    done = BooleanProperty(False)
    def __init__(self, total=10, steptime=1, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.animation = (Animation(pos_hint={'top':0.1}, duration=steptime/2) + Animation(pos_hint={'top':1.0}, duration=steptime/2))
        self.button = Button(text="Приседание", size_hint=(0.3, 0.2), pos_hint={'top' : 1.0}, background_color='blueviolet')
        self.add_widget(self.button)
        self.animation.on_progress = self.next
    def start(self):
        self.value = 0
        self.done = False
        self.animation.repeat = True
        self.animation.start(self.button)
    def next(self, button, step, *args):
        if step == 1.0:
            self.value += 1
            if self.value == self.total:
                self.animation.repeat = False
                self.done = True