# The famous and classic pong!
# Made by viegasdev

# Import modules
import turtle
import os

# Inserting player names
player_a = str(input("Insert player A name: "))
player_b = str(input("Insert player B name: "))

# Game window configuration
window = turtle.Screen()
window.title('Pong Game by viegasdev')
window.bgcolor('#264653')
window.setup(width=800, height=600)
window.tracer(0) # Stops window from always updating, increases the perfomance

# Score
score_a = 0
score_b = 0

# Paddle A -> Left
paddle_a = turtle.Turtle() # Creates a object
paddle_a.speed(0) # Animation speed (the fastest possible)
paddle_a.shape('square')
paddle_a.color('#e76f51')
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Stretches the 20px width five times
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B -> Right
paddle_b = turtle.Turtle() # Creates a object
paddle_b.speed(0) # Animation speed (the fastest possible)
paddle_b.shape('square')
paddle_b.color('#e76f51')
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # Stretches the 20px width five times
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle() # Creates a object
ball.speed(1) # Animation speed (the fastest possible)
ball.shape('square')
ball.color('#e9c46a')
ball.penup()
ball.goto(0,0)
window.delay(30)

# Score board
pen = turtle.Turtle()
pen.speed(0)
pen.color('#ffb997')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("{}: 0    {}: 0".format(player_a, player_b), align = 'center', font=('Courier', 24, 'normal'))

# Ball x axis movement
ball.dx = 0.35 # Everytime ball moves, it moves 2px in x axis

# Ball y axis movement 
ball.dy = 0.35 # Everytime ball moves, it moves 2px in y axis

# Functions to move the paddles
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
window.listen()
window.onkeypress(paddle_a_up, 'w') # Calls the function when user press the key
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True:
    window.update() # Every time the loop runs, it updates the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy)

    # Border hitting
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1 # When the ball touches the right border, 1 point is added to A's score
        pen.clear() # Clears the pen value before displaying the new value
        pen.write("{}: {}    {}: {}".format(player_a, score_a, player_b, score_b), align = 'center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1 # When the ball touches the left border, 1 point is added to B's score
        pen.clear()
        pen.write("{}: {}    {}: {}".format(player_a, score_a, player_b, score_b), align = 'center', font=('Courier', 24, 'normal'))

    # Paddle and ball colisions

    # Paddle B -> Right
    if (ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50)):
        ball.setx(340)
        ball.dx *= -1

    # Paddle A -> Left
    if (ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50)):
        ball.setx(-340)
        ball.dx *= -1