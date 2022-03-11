import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race")
colors = ["red", "orange", "blue", "green", "yellow", "purple"]
y_postion = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for x in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[x])
    new_turtle.goto(x=-230, y=y_postion[x])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won")
            else:
                print("you lost")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()
