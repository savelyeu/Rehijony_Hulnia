import turtle
import pandas
from text import Text

FONT = ("Courier", 22, "bold")

screen = turtle.Screen()
screen.title("Rehijony")
screen.setup(700, 700)
image = "Zubr.gif"
turtle.addshape(image)
turtle.shape(image)
text = Text()

data = pandas.read_csv("list.csv")
rehijony = data.rehijon.to_list()
guessed = []

# def get_x(x, y):
#     print(x, y)
# turtle.onscreenclick(get_x)
# turtle.mainloop()

while len(guessed) < 6:
    answer = screen.textinput(title=f"{len(guessed)}/6 rehijonaŭ",
                              prompt="Jaki rehijon nastupny na mapie?").title()

    if answer == "Kaniec":
        text.kaniec()
        missing = []
        for rehijon in rehijony:
            if rehijon not in guessed:
                m = turtle.Turtle()
                m.hideturtle()
                m.penup()
                mis_data = data[data.rehijon == rehijon]
                m.goto(int(mis_data.x), int(mis_data.y))
                m.color("#FFA11E")
                m.write(rehijon, font=FONT)

    if answer in rehijony:
        guessed.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        reh_data = data[data.rehijon == answer]
        t.goto(int(reh_data.x), int(reh_data.y))
        t.color("#0c179d")
        t.write(answer, font=FONT)


screen.exitonclick()








