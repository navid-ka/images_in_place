import kivy
from kivy.core.text import LabelBase
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.core.image import Image as CoreImage
import PIL

from simpleimage import SimpleImage



LabelBase.register(name='Nunito', fn_regular= 'assets/fonts/Nunito-Regular.ttf',
    fn_bold= 'assets/fonts/Nunito-Bold.ttf')


class VBoxWidget(BoxLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(VBoxWidget, self).__init__(**kwargs)


    def filter_one(self, source_image):
        
        source_image = App.get_running_app().source_image
        image = SimpleImage(source_image)
        
        for pixel in image:
            pixel.red = pixel.red * 1.5
            pixel.green = pixel.green * 0.7
            pixel.blue = pixel.blue * 1.5
        image.pil_image.save("images/new_image.png")
        image = "images/new_image.png"
        self.source_image.source = "images/new_image.png"
        self.source_image.reload()

    def filter_two(self, source_image):
        source_image = App.get_running_app().source_image
        image = SimpleImage(source_image)
        for pixel in image:
            pixel.red = pixel.red  // 2
            pixel.green = pixel.green // 2
            pixel.blue = pixel.blue * 2
        image.pil_image.save("images/new_image.png")
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