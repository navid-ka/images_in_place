import kivy
from kivy.core.text import LabelBase
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty


from simpleimage import SimpleImage



LabelBase.register(name='Nunito', fn_regular= 'assets/fonts/Nunito-Regular.ttf',
    fn_bold= 'assets/fonts/Nunito-Bold.ttf')


class VBoxWidget(BoxLayout):
    image = ObjectProperty(None)
    def filter_one(self, image):
        filename = App.get_running_app().filename
        image = SimpleImage(filename)
        for pixel in image:
            pixel.red = pixel.red * 1.5
            pixel.green = pixel.green * 0.7
            pixel.blue = pixel.blue * 1.5
        

    def filter_two(self, image):
        filename = App.get_running_app().filename
        App.get_running_app().filename
        image = SimpleImage(filename)
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