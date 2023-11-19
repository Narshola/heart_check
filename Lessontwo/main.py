from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from instructions import *
from ruffier import test
from seconds import Seconds
from sits import Sits
from runner import Runner

p1, p2, p3 = 0, 0, 0
age = 7
name = ""

darkpurple = (.06, 0, .12, 1)
Window.clearcolor = darkpurple

def check_int(in_, int_):
    try:
        int_ = int(in_.text)
        return int_
    except:
        return False


class InstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.in_name = TextInput(multiline=False)
        self.in_age = TextInput(text='7', multiline=False) 
        self.button = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x' : 0.5}, background_color='blueviolet')
        self.button.on_press = self.next
        vl = BoxLayout(orientation='vertical')
        hl1 = BoxLayout(orientation='horizontal', size_hint=(0.8, None), height=30)
        hl2 = BoxLayout(orientation='horizontal', size_hint=(0.8, None), height=30)
        hl1.add_widget(Label(text='Имя: '))
        hl1.add_widget(self.in_name)
        hl2.add_widget(Label(text='Возраст: '))
        hl2.add_widget(self.in_age)
        vl.add_widget(Label(text = txt_instruction))
        vl.add_widget(hl1)
        vl.add_widget(hl2)
        vl.add_widget(self.button)
        self.add_widget(vl)
    def next(self):
        global name, age
        name = self.in_name.text
        age = check_int(self.in_age, age)
        if age == False or age < 7:
            print('age = False or age < 7\n')
            age = 7
        else:
            self.manager.current = 'pulse1'


class PulseOneScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timer = Seconds(15)
        self.timer.bind(done=self.timeout)
        self.in_p1 = TextInput(text='0', multiline=False)
        self.in_p1.set_disabled(True)
        self.button = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x' : 0.5}, background_color='blueviolet')
        self.button.on_press = self.start_timer
        vl = BoxLayout(orientation='vertical')
        hl = BoxLayout(orientation='horizontal', size_hint=(0.8, None), height=30)
        hl.add_widget(Label(text='Введите результат:'))
        hl.add_widget(self.in_p1)
        vl.add_widget(Label(text=txt_test1))
        vl.add_widget(self.timer)
        vl.add_widget(hl)
        vl.add_widget(self.button)
        self.add_widget(vl)
    def start_timer(self):
        self.timer.start()
        self.button.set_disabled(True)
    def timeout(self, *args):
        self.in_p1.set_disabled(False)
        self.button.text = "Продолжить"
        self.button.on_press = self.next
        self.button.set_disabled(False)
    def next(self):
        global p1
        p1 = check_int(self.in_p1, p1)
        if p1 == False or p1 <= 0:
            print('p1 = False or p1 <= 0\n')
            p1 = 0
        else:
            self.manager.current = 'squats'


class SquatsScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sits = Sits(30)
        self.runner = Runner(total=30, steptime=1.5, size_hint=(0.4, 1))
        self.runner.bind(value=self.sits.next)
        self.runner.bind(done=self.finish_sits)
        self.button = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x' : 0.5}, background_color='blueviolet')
        self.button.on_press = self.start_sits
        vl = BoxLayout(orientation='vertical')
        hl = BoxLayout(orientation='horizontal')
        hl.add_widget(self.sits)
        hl.add_widget(self.runner)
        vl.add_widget(Label(text=txt_test2))
        vl.add_widget(hl)
        vl.add_widget(self.button)
        self.add_widget(vl)
    def start_sits(self):
        self.runner.start()
        self.button.set_disabled(True)
    def finish_sits(self, *args):
        self.button.text = "Продолжить"
        self.button.on_press = self.next
        self.button.set_disabled(False)
    def next(self):
        self.manager.current = 'pulse2'


class PulseTwoScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stage = 0
        self.label = Label(text="Считайте пульс")
        self.timer = Seconds(15)
        self.timer.bind(done=self.timeout)
        self.in_p2 = TextInput(text='0', multiline=False)
        self.in_p2.set_disabled(True)
        self.in_p3 = TextInput(text='0', multiline=False)
        self.in_p3.set_disabled(True)
        self.button = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x' : 0.5}, background_color='blueviolet')
        self.button.on_press = self.start_timer
        vl = BoxLayout(orientation='vertical')
        hl1 = BoxLayout(orientation='horizontal', size_hint = (0.8, None), height = 30)
        hl2 = BoxLayout(orientation='horizontal', size_hint = (0.8, None), height = 30)
        hl1.add_widget(Label(text='Результат:'))
        hl1.add_widget(self.in_p2)
        hl2.add_widget(Label(text='Результат после отдыха:'))
        hl2.add_widget(self.in_p3)
        vl.add_widget(Label(text=txt_test3))
        vl.add_widget(self.label)
        vl.add_widget(self.timer)
        vl.add_widget(hl1)
        vl.add_widget(hl2)
        vl.add_widget(self.button)
        self.add_widget(vl)
    def start_timer(self):
        self.timer.start()
        self.button.set_disabled(True)
    def timeout(self, *args):
        if self.timer.done:
            if self.stage == 0:
                self.stage = 1
                self.label.text = "Отдыхайте"
                self.timer.restart(30)
                self.in_p2.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.label.text = "Считайте пульс"
                self.timer.restart(15)
            elif self.stage == 2:
                self.in_p3.set_disabled(False)
                self.button.set_disabled(False)
                self.button.text = "Завершить"
                self.button.on_press = self.next
    def next(self):
        global p2, p3
        p2 = check_int(self.in_p2, p2)
        p3 = check_int(self.in_p3, p3)
        if (p2 == False or p2 <= 0) or (p3 == False or p3 <= 0):
            print('p2 = False or p2 <= 0\nOR\np3 = False or p3 <= 0\n')
            p2 = 0
            p3 = 0
        else:
            self.manager.current = 'result'


class ResultScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.res = Label(text='')
        self.on_enter = self.before
        vl = BoxLayout(orientation='vertical')
        vl.add_widget(self.res)
        self.add_widget(vl)
    def before(self):
        global name, age, p1, p2, p3
        self.res.text = name + '\n' + test(p1, p2, p3, age)


class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstScr(name='insructions'))
        sm.add_widget(PulseOneScr(name='pulse1'))
        sm.add_widget(SquatsScr(name='squats'))
        sm.add_widget(PulseTwoScr(name='pulse2'))
        sm.add_widget(ResultScr(name='result'))
        return sm


app = HeartCheck()
app.run()