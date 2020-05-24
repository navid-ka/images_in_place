import kivy
from kivy.core.text import LabelBase
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from PIL import Image, ImageEnhance
import sys



LabelBase.register(name='Nunito', fn_regular= 'assets/fonts/Nunito-Regular.ttf',
    fn_bold= 'assets/fonts/Nunito-Bold.ttf')




class VBoxWidget(BoxLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(VBoxWidget, self).__init__(**kwargs)

    def filter_one(self, source_image):
        
        source_image = App.get_running_app().source_image
        image = Image.open(source_image)
        enhance_value = 1.5
        image = ImageEnhance.Contrast(image).enhance(enhance_value)
        image.save("images/new_image.png")
        image = "images/new_image.png"
        self.source_image.source = "images/new_image.png"
        self.source_image.reload()

    def filter_two(self, source_image):
        source_image = App.get_running_app().source_image
        image = Image.open(source_image)
        image = ImageEnhance.Brightness(image).enhance(1.5)
        image.save("images/new_image.png")
        image = "images/new_image.png"
        self.source_image.source = "images/new_image.png"
        self.source_image.reload()

    def filter_three(self, source_image):
        source_image = App.get_running_app().source_image
        image = Image.open(source_image).convert('L')
        image.save("images/new_image.png")
        image = "images/new_image.png"
        self.source_image.source = "images/new_image.png"
        self.source_image.reload()

    def filter_four(self, source_image, *args):
        
        source_image = App.get_running_app().source_image
        image = Image.open(source_image)
        enhance_value = (args[1])
        image = ImageEnhance.Brightness(image).enhance(enhance_value)
        image.save("images/new_image.png")
        image = "images/new_image.png"
        self.source_image.source = "images/new_image.png"
        self.source_image.reload()

    def slider_one(self, source_image, *args):
        
        source_image = App.get_running_app().source_image
        image = Image.open(source_image)
        enhance_value = (args[1])
        image = ImageEnhance.Brightness(image).enhance(enhance_value)
        image.save("images/new_image.png")
        image = "images/new_image.png"
        self.source_image.source = "images/new_image.png"
        self.source_image.reload()

    def slider_two(self, source_image, *args):
        
        source_image = App.get_running_app().source_image
        image = Image.open(source_image)
        enhance_value = (args[1])
        image = ImageEnhance.Color(image).enhance(enhance_value)
        image.save("images/new_image.png")
        image = "images/new_image.png"
        self.source_image.source = "images/new_image.png"
        self.source_image.reload()
    def slider_three(self, source_image, *args):
        
        source_image = App.get_running_app().source_image
        image = Image.open(source_image)
        enhance_value = (args[1])
        image = ImageEnhance.Sharpness(image).enhance(enhance_value)
        image.save("images/new_image.png")
        image = "images/new_image.png"
        self.source_image.source = "images/new_image.png"
        self.source_image.reload()

class Main(App):
    source_image = StringProperty('images/logo.png')

    def build(self):
        Window.size = (1440 ,810)
        return VBoxWidget()

if __name__ == '__main__':
    Main().run()