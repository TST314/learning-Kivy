#source from Kivy's docs. 

#IMPORTS (common)
import os
import collections, fileinput, shutil
from sys import stdout


#Kivy imports
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.frames = {} #if this works here then it may be possible to have many frames!


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()

'''
INITIAL NOTES
______________

- Uses more imports than tkinter
- Only has 2 parts in the __init__ special method instead of the 3 in tkinter
- Looks nicer than ttk or tkinter
- Seems to use a similar syntax to tkinter
	- instead of doing tk.Frame.__init__(self,parent) we do super
- Will probably be a similar size to tkinter files for larger projects. 
- If I take out the common imports then it may run faster if it is ever converted into an exe. 
'''
