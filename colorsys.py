     import turtle
     import colorsys
     turtle.title("Mehta Meet")
     m=turtle.Turtle()
     m.speed(0)
     m.pensize(1)
     h=0.0
     for i in range(30):
       color=colorsys.hsv_to_rgb(h,1,1)
       #turtle.bgcolor(color)
       m.pencolor(color)
       h+=0.08
       m.rt(i)
       m.circle(200,i)
       m.fd(i)
       m.rt(90)
     turtle.done()
