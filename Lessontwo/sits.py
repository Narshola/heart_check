from kivy.uix.label import Label

class Sits(Label):
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        self.text = "Осталось приседаний: " + str(self.total)
        super().__init__(text=self.text, **kwargs)
    def next(self, *args):
        self.current += 1
        self.text = "Осталось приседаний: " + str(max(0, self.total - self.current))