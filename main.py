import kivy
from kivy.core.text import LabelBase
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty

from tkinter.filedialog import askopenfilename
from tkinter import Tk
from simpleimage import SimpleImage



LabelBase.register(name='Nunito', fn_regular= 'assets/fonts/Nunito-Regular.ttf',
    fn_bold= 'assets/fonts/Nunito-Bold.ttf')


class VBoxWidget(BoxLayout):


    def get_image_one(self):
        
        '''This method is called by button FileChooser, it opens a FileChooser selects the desired image'''
        Tk().withdraw()
        image = askopenfilename(initialdir = "\src\images",title = "Select file",filetypes = (("image files","*.jpg"),("all files","*.*")))  
        self.filename.source = image
    
    def filter_one(self, filename):
        image = SimpleImage(self.filename.source)
        for pixel in image:
            pixel.red = pixel.red * 1.5
            pixel.green = pixel.green * 0.7
            pixel.blue = pixel.blue * 1.5

        image.show()
        
    def filter_two(self, filename):
        image = SimpleImage(self.filename.source)
        for pixel in image:
            pixel.red = pixel.red  // 2
            pixel.green = pixel.green // 2
            pixel.blue = pixel.blue * 2

        image.show()



class Main(App):
    filename = StringProperty('images/logo.png')
    def build(self):
        Window.size = (1440 ,810)
        return VBoxWidget()

if __name__ == '__main__':
    Main().run()