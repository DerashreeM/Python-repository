print("Hello Gamer!!!!")
print("Code: \n 1.square \n 2.Triangle \n 3.circle")
a=int(input("Enter your choice=>"))
match a:
   case 1:
     print("    SQUARE    ")
     w=int(input("enter your width=>"))
     h=int(input("enter your height=>"))
     import turtle
     turtle.title("Mehta Meet")
     turtle.bgcolor("orange")
     m=turtle.Turtle()
     for i in range(0,4):
      m.forward(w)
      m.right(90)
      m.forward(h)
     turtle.done()

   case 2:
     print("    TRIANGLE  ")
     w=int(input("enter your width=>"))
     #h=int(input("enter your height=>"))
     import turtle
     turtle.title("Mehta Meet")
     turtle.bgcolor("orange")
     m=turtle.Turtle()
     m.forward(w)
     m.left(125)
     m.forward(w)
     m.left(117)
     m.forward(w-7)
     turtle.done()

   case 3:
     print("    CIRCLE   ")
     c=int(input("Enter your radious of circle=>"))
     import turtle
     turtle.title("Mehta Meet")
     turtle.bgcolor("orange")
     m=turtle.Turtle()
     m.circle(c)
     turtle.done()
    
   case _:
      print("Invalid choice!!!!")