from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
current_position = [(-40, 0), (-20, 0), (0, 0)]
segments = []

for position in current_position:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    for seg_number in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_number - 1].xcor()
        new_y = segments[seg_number - 1].ycor()
        segments[seg_number].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)

screen.exitonclick()
