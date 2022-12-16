from turtle import *
bgcolor("Green")
#turtle.circle(100)
#turtle.getscreen()._root.mainloop()
color("Pink", "Yellow")
begin_fill()
#for t in range(4):
#    turtle.forward(90)
#    turtle.left(90)
while True:
    forward(128)
    left(88)
    if abs(pos()) < 1:
        break
end_fill()
done()
#turtle.getscreen()._root.mainloop()
