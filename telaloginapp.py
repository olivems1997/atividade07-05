from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

class TelaLogin(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 15
        self.padding = [20, 20, 20, 20]  # Padding ajustado para mover a caixa para cima
        
        # Cor de background
        with self.canvas.before:
            Color(0.21, 0.20, 0.80, 1) 
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._atualizar_retangulo, pos=self._atualizar_retangulo)
            
        # Imagem do logo
        self.add_widget(Image(source='image.png', size_hint_y=None, height=160))
        
        # Espaçador para empurrar os próximos widgets para cima
        self.add_widget(Widget(size_hint_y=None, height=120))

        # Entrada de email
        self.email = TextInput(hint_text='Email', multiline=False, size_hint_y=None, height=50, size_hint_x=None, width=200, pos_hint={'center_x': 0.5})
        self.add_widget(self.email)
        
        # Entrada de senha
        self.senha = TextInput(hint_text='Senha', multiline=False, password=True,  size_hint_y=None, height=50, size_hint_x=None, width=200, pos_hint={'center_x': 0.5})
        self.add_widget(self.senha)
        
        # Botão de login
        self.add_widget(Button(text='Login', size_hint_y=None, height=40, size_hint_x=None, width=200, pos_hint={'center_x': 0.5}))
        
        self.add_widget(Widget(size_hint_y=None, height=100))

        
    def _atualizar_retangulo(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

class MeuApp(App):
    def build(self):
        Window.size = (360, 640)  # Define o tamanho da janela
        return TelaLogin()

if __name__ == '__main__':
    MeuApp().run()