import turtle

wn = turtle.Screen()
wn.title("Pong by @KnowyGaming")
wn.bgcolor("black")
wn.setup(width=1000,height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-450, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(450, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("Green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("Red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b) , align="center",font=("courier",24 , "bold"))

# Functions

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)    

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")




# Main Game Loop

while True:
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1    

    if ball.xcor() > 490:
        ball.goto(0 ,0)
        ball.dx *= -1 
        score_a += 1  
        pen.clear()  
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b) , align="center",font=("courier",24 , "bold"))     

    if ball.xcor() < -490:
        ball.goto(0 ,0)
        ball.dx *= -1   
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b) , align="center",font=("courier",24 , "bold"))

    # Paddle and ball collision
    if ball.xcor() > 440 and ball.xcor() < 450 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(440)
        ball.dx *= -1        


    if ball.xcor() < -440 and ball.xcor() > -450 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-440)
        ball.dx *= -1  