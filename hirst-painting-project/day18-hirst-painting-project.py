import colorgram
import turtle
import random
turtle.colormode(255)


hirst = turtle.Turtle()
hirst.speed("fastest")
hirst.penup()

# The Hirst Painting Project
# Extract 6 colors from an image.
colors = colorgram.extract('hirst_spot_painting.jpg', 30)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
list_of_colors = []
for color in colors:
    rgb = color.rgb # e.g. (255, 151, 210)
    list_of_colors.append((rgb[0], rgb[1], rgb[2]))

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
#red = rgb[0]
#red = rgb.r

#print(list_of_colors)
# canvas size 10x10

# spacing between circles 50

colors = ["blue", "red", "gold", "green", "black", "gray"]

DOT_SIZE = 20
NUMBER_OF_DOTS = 101


hirst.setheading(225)
hirst.forward(300)
hirst.setheading(0)
hirst.hideturtle()
    
for dot_count in range(1, NUMBER_OF_DOTS):
    hirst.dot(DOT_SIZE, random.choice(list_of_colors))
    hirst.forward(50)
    if dot_count % 10 == 0:
        hirst.setheading(90) 
        hirst.forward(50) 
        hirst.setheading(180) 
        hirst.forward(500)  
        hirst.setheading(0)  


screen = turtle.Screen()
screen.exitonclick()
