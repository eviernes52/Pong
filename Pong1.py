# Pong Game in Python 3 with turtle module 
# By: Emiliano Viernes
import turtle
import os

wn = turtle.Screen()
wn.title("Pong by Emiliano Viernes")
wn.bgcolor("purple")
wn.setup(width=800, height=600)
wn.tracer(0)


#scoring
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("hot pink")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("hot pink")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.18
ball.dy = -0.18



#pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("navy")
pen.penup()
pen.hideturtle()
pen.goto(0 , 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Movement Function a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Movement Function b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard Binding 
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")


# MG Loop
while True:
    wn.update()
    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Ball Border Top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    #Ball Border Bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    #Ball Border Right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))


    # Paddle + Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1