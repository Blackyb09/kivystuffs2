from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
#from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label

Window.size = (300, 400)
#origin = Builder.load_file("calculator.kv")

class Calculator(BoxLayout):
    def changecolor(self): 
        self.ids.clear.add_widget(Label(text="press"))
    #clear screen button
    def clearscreen(self):
        self.ids.disp.text = '0'
    
    #numbers button methods to get the numbers on the buttons
    def button_press(self, button):
        existing_text = self.ids.disp.text
        if existing_text == "0":
            self.ids.disp.text = f"{button}"
        elif existing_text != "0":
            self.ids.disp.text = f"{existing_text}{button}"
    
    def deleteback(self):
        existing_text = self.ids.disp.text
        if existing_text != "0":
            self.ids.disp.text = existing_text[0:-1]
    
    def signs(self, sign):
        existing_text = self.ids.disp.text
        operators = ['+', '-', '*', '/']
        if existing_text[-1] not in operators:
            self.ids.disp.text = f"{existing_text}{sign}"
    def dot(self):
        existing_text = self.ids.disp.text
        operators = ['+', '-', '*', '/']
        # for i in existing_text:
        #     if i in '-+/*':
        #         newlist = existing_text.split(i)
        #         self.ids.disp.text = f"{newlist[0:]}{newlist[-1]}."

        # if '.' in (existing_text):
        #     pass
        # else:
        #     existing_text = f"{existing_text}."
        #     self.ids.disp.text
        if existing_text[-1] != '.' and existing_text[-1] not in operators:
            newlist = existing_text.split('.')
            nw = str(newlist[-1])
            print(newlist)
            if nw not in "1234567890":
                self.ids.disp.text = f"{existing_text}."
            # if existing_text[0] in "+-/*1234567890":
            #     self.ids.disp.text = existing_text + '.'
            # if existing_text[-1] == ".":
            #     self.ids.disp.text = existing_text[0:] 
    def equalto(self):
        existing_text = self.ids.disp.text
        operators = ['+', '-', '*', '/']
        if existing_text[-1] not in operators:
            self.ids.disp.text = str(eval(existing_text))
    def plusminus(self):
        existing_text = self.ids.disp.text
        if existing_text != '':
            if existing_text[0] in "+1234567890":
                self.ids.disp.text = "-" + existing_text
            if existing_text[0] == "-":
                self.ids.disp.text = existing_text[1:]  

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalculatorApp().run()