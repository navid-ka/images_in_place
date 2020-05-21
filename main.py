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

    image = ObjectProperty(None)

    def filter_one(self, image_widget):
        filename = App.get_running_app().filename
        image = SimpleImage(filename)
        for pixel in image:
            pixel.red = pixel.red * 1.5
            pixel.green = pixel.green * 0.7
            pixel.blue = pixel.blue * 1.5

        new_image = image.pil_image.save("images/new_image.png")
        filename = new_image


    def filter_two(self, image_widget):
        filename = App.get_running_app().filename
        image = SimpleImage(filename)
        for pixel in image:
            pixel.red = pixel.red  // 2
            pixel.green = pixel.green // 2
            pixel.blue = pixel.blue * 2

        new_image = image.pil_image.save("images/new_image.png")
        filename = new_image



class Main(App):
    filename = StringProperty('images/logo.png')
    filter_one = BooleanProperty(False)
    filter_two = BooleanProperty(False)
    def build(self):
        Window.size = (1440 ,810)
        return VBoxWidget()

if __name__ == '__main__':
    Main().run()