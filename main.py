import kivy
from kivy.core.text import LabelBase
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

from tkinter.filedialog import askopenfilename
from tkinter import Tk
from simpleimage import SimpleImage



LabelBase.register(name='Nunito', fn_regular= 'assets/fonts/Nunito-Regular.ttf',
    fn_bold= 'assets/fonts/Nunito-Bold.ttf')


class HBoxWidget(BoxLayout):
    pass

class VBoxWidget1(BoxLayout):

    def get_image_one(self):
        
        '''This method is called by button FileChooser, it opens a FileChooser selects the desired image'''
        Tk().withdraw()
        img1 = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("image files","*.jpg"),("all files","*.*")))
        app = App.get_running_app()
        app.first_image = img1
        

    def right_half_darker(self, first_image):

        app = App.get_running_app()
        image = SimpleImage(app.first_image)
        for pixel in image:
            pixel.red = pixel.red * 1.5
            pixel.green = pixel.green * 0.7
            pixel.blue = pixel.blue * 1.5
        app.first_image = image


class VBoxWidget2(BoxLayout):
    pass

class ContainerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)

class Main(App):
    first_image = StringProperty('images/logo.png')
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (1440 ,810)
        return ContainerBox()

if __name__ == '__main__':
    Main().run()