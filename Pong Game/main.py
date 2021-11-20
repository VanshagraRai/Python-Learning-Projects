import turtle
import winsound

win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("red")
win.setup(width=800, height=600)
win.tracer(0)


# Scores
score_1 = 0
score_2 = 0

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.color("white")
paddle_1.penup()
paddle_1.goto(-350, 0)

# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.color("white")
paddle_2.penup()
paddle_2.goto(350, 0)


# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.3
Ball.dy = -0.3


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "bold"))

# Functions
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


# Keyboard bindings
win.listen()
win.onkeypress(paddle_1_up, "w")
win.onkeypress(paddle_1_down, "s")
win.onkeypress(paddle_2_up, "Up")
win.onkeypress(paddle_2_down, "Down")


# Main loop
while True:
    win.update()

    # Move the ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Border Setting
    if Ball.ycor() >= 290:
        Ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if Ball.ycor() <= -290:
        Ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write(
            "Player 1: {}  Player 2: {}".format(score_1, score_2),
            align="center",
            font=("Courier", 24, "bold"),
        )

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write(
            "Player 1: {}  Player 2: {}".format(score_1, score_2),
            align="center",
            font=("Courier", 24, "bold"),
        )

    # Paddle colliding
    if (
        Ball.xcor() > 340
        and Ball.xcor() < 350
        and (Ball.ycor() < paddle_2.ycor() + 50)
        and (Ball.ycor() > paddle_2.ycor() - 50)
    ):
        Ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (
        Ball.xcor() < -340
        and Ball.xcor() > -350
        and (Ball.ycor() < paddle_1.ycor() + 50)
        and (Ball.ycor() > paddle_1.ycor() - 50)
    ):
        Ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
