from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random
import string

class TokenGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super(TokenGenerator, self).__init__(**kwargs)
        
        self.orientation = 'vertical'
        
        self.input = TextInput(hint_text='Enter something')
        self.add_widget(self.input)
        
        self.token_label = Label(text='')
        self.add_widget(self.token_label)
        
        generate_btn = Button(text='Generate Token')
        generate_btn.bind(on_press=self.generate_token)
        self.add_widget(generate_btn)
    
    def generate_token(self, instance):
        input_text = self.input.text
        chars = string.ascii_letters + string.digits
        token = ''.join(random.choice(chars) for _ in range(32))
        self.token_label.text = token

class TokenApp(App):
    def build(self):
        return TokenGenerator()

if __name__ == '__main__':
    TokenApp().run()
