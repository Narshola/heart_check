from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty

class Seconds(Label):
    done = BooleanProperty()
    def __init__(self, seconds, **kwargs):
        self.done = False
        self.seconds = seconds
        self.current = 0
        sec_text = "Прошло секунд: " + str(self.current)
        super().__init__(text=sec_text)
    def todo(self, dt):
        self.current += 1
        self.text = "Прошло секунд: " + str(self.current)
        if self.current >= self.seconds:
            self.done = True
            return False
    def start(self):
        Clock.schedule_interval(self.todo, 1)
    def restart(self, seconds, **kwargs):
        self.done = False
        self.seconds = seconds
        self.current = 0
        self.text = "Прошло секунд: " + str(self.current)
        self.start()