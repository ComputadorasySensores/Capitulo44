# Parte Inicial

import turtle

ventana = turtle.Screen()
ventana.title("Pong en Raspberry")
ventana.bgcolor("blue")
ventana.setup(width=800, height=600)
ventana.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.mx = 0.4
pelota.my = -0.4

# Puntaje
puntaje_a = 0
puntaje_b = 0


#  Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,265)
pen.write("Jugador A: 0  Jugador B: 0", align="center", font=("Verdana", 16, "italic"))

#  Funciones
def paddle_a_arriba():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_abajo():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_arriba():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_abajo():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#  Vinculando teclado
ventana.listen()
ventana.onkeypress(paddle_a_arriba, "w")
ventana.onkeypress(paddle_a_abajo, "s")
ventana.onkeypress(paddle_b_arriba, "Up")
ventana.onkeypress(paddle_b_abajo, "Down")
# Loop principal
while True:
    ventana.update()
    
# Movimiento de pelota
    pelota.setx(pelota.xcor() + pelota.mx)
    pelota.sety(pelota.ycor() + pelota.my)
    
#  Definiendo borde
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.my *= -1
        
    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.my *= -1
        
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.mx *= -1
        puntaje_a += 1
        pen.clear()
        pen.write("Jugador A: {}  Jugador B: {}".format(puntaje_a, puntaje_b), align="center", font=("Verdana", 16, "italic"))
        
    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.mx *= -1
        puntaje_b += 1
        pen.clear()
        pen.write("Jugador A: {}  Jugador B: {}".format(puntaje_a, puntaje_b), align="center", font=("Verdana", 16, "italic"))
        
# Choque de pelota y paddle

    if pelota.xcor() < -340 and pelota.ycor() < paddle_a.ycor() + 50 and pelota.ycor() > paddle_a.ycor() -50:
        pelota.mx *= -1
        
    elif pelota.xcor() > 340 and pelota.ycor() < paddle_b.ycor() +50 and pelota.ycor() > paddle_b.ycor() -50:
        pelota.mx *= -1
        

