     import turtle
     import colorsys
     turtle.title("Mehta Meet")
     #turtle.bgcolor("")
     m=turtle.Turtle()
     h=0.0
     m.speed(0)
     m.pensize(1)
     for i in range(50):
       color = colorsys.hsv_to_rgb(h,1,1)
       turtle.bgcolor(color)
       m.pencolor(color)
       h+=0.08
       m.circle(5*i)
       m.circle(-5*i)
     turtle.done()
