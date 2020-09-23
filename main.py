import turtle
t = turtle.Turtle()
t.speed(50)
canvas = t.getscreen()
canvas.bgcolor('gray')
def move(x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()  #end of move function
mycolors = ['red','orange','green','peachpuff','violet','white','blue','yellow']
move(0,0)
length = 20
def flower():
  for c in mycolors:
    t.pencolor(c)
    for i in range(4):
      t.rt(90)
      t.forward(length) #end of square loop
    t.penup()
    t.rt(45)
    t.pendown()  #color loop ends
move(0,-100)
for i in range(4):
    t.rt(90)
    t.forward(20)
t.hideturtle()
flower()