from turtle import Turtle, Screen
from prettytable import PrettyTable
table = PrettyTable()
print(table)
tom = Turtle()
tom.color('green')
tom.shape('turtle')
tom.backward(160)


print(tom)
my_screen = Screen()
tom.color('red')
tom.fd(200)
my_screen.exitonclick()

