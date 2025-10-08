from turtle import Turtle, Screen

test_turtle = Turtle()
print(test_turtle)
test_turtle.shape("turtle")
test_turtle.color("blue")
if test_turtle.onclick:
  test_turtle.forward(100)


test_screen = Screen()
my_screen = test_screen.canvheight
print(my_screen)
test_screen.exitonclick()


