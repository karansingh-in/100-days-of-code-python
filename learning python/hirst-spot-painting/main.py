# import colorgram

# colors = colorgram.extract('image.jpg', 6) # image name, no. of colors to extract
# # print(colors)

# list_of_rgb = []
# for col in range(len(colors)):
#     color = colors[col].rgb
#     r_value = color.r
#     g_value = color.g
#     b_value = color.b
#     rgb_tuple = (r_value,g_value,b_value)
#     list_of_rgb.append(rgb_tuple)
# print(list_of_rgb)

import random
import turtle as t
color_list = [(252, 251, 248), (219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153), (245, 232, 236)]
screen = t.Screen()
screen.bgcolor('black')
t.colormode(255)
tom = t.Turtle()
tom.speed('fastest')


for i in range(1, 11):
    tom.home()
    tom.setheading(225)
    tom.penup()
    tom.fd(550)
    tom.right(135)
    tom.fd(50*i)
    tom.right(90)
    tom.pendown()
    for j in range(10):
        tom.penup()
        # r_color_for_dot = random.choice(color_list)[0]
        # g_color_for_dot = random.choice(color_list)[1]
        # b_color_for_dot = random.choice(color_list)[2]
        
        print(f'{random.choice(color_list)}')
        tom.fd(50); tom.pendown(); tom.dot(20, random.choice(color_list)); tom.penup(); tom.fd(50)

    
screen.exitonclick()


