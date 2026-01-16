import turtle
import time
import random

# Configuration
DELAY = 0.1

segments = []

# Configuring the window
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)


# Snake 
head = turtle.Turtle()
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("green")
food.penup()
food.goto(50, 60)


def go_up():
    head.direction = "Up"

def go_down():
    head.direction = "Down"

def go_left():
    head.direction = "Left"

def go_right():
    head.direction = "Right"
    

# Listen to the keyboard
window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")


def move():
    MOVE_BY = 10

    if head.direction == "Up":
        current_position_y = head.ycor()
        head.sety(current_position_y + MOVE_BY)

    if head.direction == "Down":
        current_position_y = head.ycor()
        head.sety(current_position_y - MOVE_BY) 

    if head.direction == "Left":
        current_position_x = head.xcor()
        head.setx(current_position_x - MOVE_BY) 

    if head.direction == "Right":
        current_position_x = head.xcor()
        head.setx(current_position_x + MOVE_BY)           
    

# Main game loop
while True:
    window.update()

    if head.distance(food) < 20:
        food.goto(
            random.randint(-290, 290),
            random.randint(-290, 290),
        )

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()

        segments.append(new_segment)

    for index in range(len(segments) -1, 0, -1):
        x_cor = segments[index -1].xcor()
        y_cor = segments[index -1].ycor()  

        segments[index].goto(x_cor, y_cor)

    if len(segments) > 0:
        x_cor = head.xcor()
        y_cor = head.ycor()

        segments[0].goto(x_cor, y_cor)       

    move()

    time.sleep(DELAY) 



window.mainloop()