import turtle

t = turtle.Pen() #boligrafo               (arrow)
turtle.bgcolor("black")
colores =  [ "red", "yellow", "blue", "green"]
t.speed(11)

for i in range(250):
    t.pencolor(colores [i%4])
    t.forward(i)
    t.left(95) 


turtle.exitonclick()
