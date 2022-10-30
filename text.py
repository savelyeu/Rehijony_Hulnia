from turtle import Turtle
FONT = ("Courier", 14, "normal")

class Text(Turtle):

    def __init__(self):
        super().__init__()
        self.color("#E3DEDA")
        self.hideturtle()
        self.penup()
        self.goto(-165, -320)
        self.write("'Kaniec', kab pahliadzieć usie rehijony" , align="left", font=FONT)

    def kaniec(self):
        self.goto(-120, 320)
        self.write("Kali laska, usie šesć rehijonaŭ", align="left", font=FONT)