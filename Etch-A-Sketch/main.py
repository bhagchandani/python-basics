from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
	timmy.forward(10)

def move_backward():
	timmy.backward(10)

def move_counter_clock():
	newheading = timmy.heading() + 10
	timmy.setheading(newheading)

def move_clock():
	newheading = timmy.heading() - 10
	timmy.setheading(newheading)

def clear_screen():
	timmy.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)

screen.onkey(key="s", fun=move_backward)

screen.onkey(key="a", fun=move_counter_clock)

screen.onkey(key="d", fun=move_clock)

screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()