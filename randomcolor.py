     import turtle
     from random import randint
     turtle.title("Mehta Meet")
     #turtle.bgcolor("orange")
     m=turtle.Turtle()
     m.speed(0)
     m.pensize(1)
     x=1
     while x<500:
       r=randint(0,255)
       g=randint(0,255)
       b=randint(0,255)
       turtle.colormode(255)
       m.pencolor(r,g,b)
       m.fd(60+x)
       m.rt(90.25)
       x+=1
     turtle.done()
