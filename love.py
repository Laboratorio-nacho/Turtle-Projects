import turtle
from turtle import*

s = Screen()
s.bgcolor("black")

t = turtle.Turtle()
t.pencolor("white")



def curve():
    speed(0.1)
    for i in range(200):
        speed(0.1)
        t.rt(1)
        t.fd(1)


def heart():
    t.fillcolor("red")
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    speed(0.1)
    curve()
    speed(0.1)
    t.lt(120)
    speed(0.1)
    curve()
    speed(0.1)
    t.fd(112)
    t.end_fill()

heart()
t.ht()

def write(msj,pos):
    x,y = pos  
    t.penup()
    t.goto(x,y)
    t.color("white")
    style = ("stencil STD", 18 , "italic")
    t.write(msj, font=style)

# Nuevo: escribir 'daniela' estilizado
def write_stylish(text, pos, base_size=36):
    x, y = pos
    t.penup()
    t.goto(x, y)
    t.hideturtle()
    # dibujar contorno con varios colores para efecto "cool"
    colors = ["#FF6B6B", "#FFD93D", "#6BCB77", "#4D96FF", "#9D4EDD"]
    # escribir sombra/contorno desplazada varias veces
    for i, c in enumerate(colors):
        t.goto(x + i*2 - 4, y - i*2 + 4)
        t.color(c)
        style = ("Arial", base_size - i*4, "bold")
        t.write(text, font=style, align="center")

    # texto principal blanco en el centro
    t.goto(x, y)
    t.color("white")
    style = ("Arial", base_size, "bold")
    t.write(text, font=style, align="center")


# Animación simple: escala creciente
def animate_text(text, pos):
    for size in range(12, 46, 4):
        t.clear()
        # redibujar el corazón debajo (simplemente llamar a heart()),
        # pero para evitar duplicados, volvemos a dibujar fondo negro y corazón
        s.bgcolor("black")
        # re-dibujar el corazón estático
        t.reset()
        t.pencolor("white")
        t.speed(0)
        t.penup()
        t.hideturtle()
        # mantener el corazón dibujado como antes
        heart()
        t.penup()
        write_stylish(text, pos, base_size=size)
        turtle.update()


# Llamada final para mostrar 'daniela' centrado encima del corazón
write_stylish("daniela", (0, 20), base_size=48)






turtle.exitonclick()

