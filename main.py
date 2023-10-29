from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from instructions import *
from ruffier import test

p1, p2, p3 = 0, 0, 0
age = 7
name = ""


class InstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.in_name = TextInput(multiline=False)
        self.in_age = TextInput(text='7', multiline=False) 
        self.button = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x' : 0.5}, color='purple')
        self.button.on_press = self.next
        vl = BoxLayout(orientation='vertical')
        hl1 = BoxLayout(orientation='horizontal')
        hl2 = BoxLayout(orientation='horizontal')
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
        age = int(self.in_age.text)
        self.manager.current = 'pulse1'


class PulseOneScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x' : 0.5})
        self.in_p1 = TextInput(text='0', multiline=False)
        self.button.on_press = self.next
        vl = BoxLayout(orientation='vertical')
        vl.add_widget(Label(text=txt_test1))
        vl.add_widget(self.in_p1)
        vl.add_widget(self.button)
        self.add_widget(vl)
    def next(self):
        global p1
        p1 = int(self.in_p1.text)
        self.manager.current = 'squats'


class SquatsScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x' : 0.5})
        self.button.on_press = self.next
        vl = BoxLayout(orientation='vertical')
        vl.add_widget(Label(text=txt_test2))
        vl.add_widget(self.button)
        self.add_widget(vl)
    def next(self):
        self.manager.current = 'pulse2'


class PulseTwoScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.in_p2 = TextInput(text='0', multiline=False, halign='right') #<--
        self.in_p3 = TextInput(text='0', multiline=False, halign='right')
        self.button = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x' : 0.5})
        self.button.on_press = self.next
        vl = BoxLayout(orientation='vertical')
        hl1 = BoxLayout(orientation='horizontal', padding=10)
        hl2 = BoxLayout(orientation='horizontal')
        hl1.add_widget(Label(text='Результат:'))
        hl1.add_widget(self.in_p2)
        hl2.add_widget(Label(text='Результат после отдыха:'))
        hl2.add_widget(self.in_p3)
        vl.add_widget(Label(text=txt_test3))
        vl.add_widget(hl1)
        vl.add_widget(hl2)
        vl.add_widget(self.button)
        self.add_widget(vl)
    def next(self):
        global p2, p3
        p2 = int(self.in_p2.text)
        p3 = int(self.in_p3.text)
        self.manager.current = 'result'


class ResultScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical')
        vl.add_widget(Label(text=name))
        vl.add_widget(Label(text=test(p1, p2, p3, age)))
        #vl.add_widget(Label(text=txt_index + str(test(p1, p2, p3, age))))
        #vl.add_widget(Label(text=txt_workheart + ruffier_result()))
        self.add_widget(vl)


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
