import turtle
     import colorsys
     turtle.title("Mehta Meet")
     #mturtle.bgcolor("")
     m=turtle.Turtle()
     m.pensize(1)
     h=0.0
     i=1
     j=100
     while i<30:
       color=colorsys.hsv_to_rgb(h,1,1)
       m.pencolor(color)
       h+=0.08
       m.circle(j)
       j+=10
       i+=1
     turtle.done()
