# Simple pong game
# Written by Kyle Nguyen

#Built with turtle; module that allows basic graphics
import turtle
import pygame
import random
import time

pygame.init()
pygame.mixer.init()
turtle.speed('fastest')
turtle.tracer(0)
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

bounceSound = pygame.mixer.Sound('pythonPong/bounce.wav')
scoreSound = pygame.mixer.Sound('pythonPong/score.wav')
startSound = pygame.mixer.Sound('pythonPong/start.wav')
paddleBounceSound = pygame.mixer.Sound('pythonPong/paddlebounce.wav')

startSound.play()

# score
scoreA = 0
scoreB = 0
# default shape size is 20px 20px
# objects to add
paddleSpeed = 0.4
# paddle a
    # module.Class
paddleA = turtle.Turtle()
#sets to the max speed
paddleA.speed(0)
paddleA.shape('square')
paddleA.color('white')
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# paddle b
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape('square')
paddleB.color('white')
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

#ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = -0.15

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup() 
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A: 0      Player B: 0', align='center', font=('Courier', 24, 'normal'))


#functions
def paddleAUp():
    # returns the y coordinate of the paddle
    y = paddleA.ycor()
    if y < 250:
        y += 20
    paddleA.sety(y)
def paddleADown():
    # returns the y coordinate of the paddle
    y = paddleA.ycor()
    if y > -240:
        y -= 20
    paddleA.sety(y)

def paddleBUp():
    # returns the y coordinate of the paddle
    y = paddleB.ycor()
    if y < 250:
        y += 20
    paddleB.sety(y)
def paddleBDown():
    # returns the y coordinate of the paddle
    y = paddleB.ycor()
    if y > -240:
        y -= 20
    paddleB.sety(y)


# AI movement function
def aiMovement():
    probability = random.uniform(0, 0.5)
    moveProbability = probability
    
    
    
    if random.random() < moveProbability:
        if ball.ycor() < paddleB.ycor():
            paddleB.sety(paddleB.ycor() - paddleSpeed)
        elif ball.ycor() > paddleB.ycor():
            paddleB.sety(paddleB.ycor() + paddleSpeed)
                        





# Keyboard binding
window.listen()
window.onkeypress(paddleAUp, "w")
window.onkeypress(paddleADown, "s")
window.onkeypress(paddleBUp, "Up")
window.onkeypress(paddleBDown, "Down") 
# Main loop
while True:
    #updates screen when loop repeats
    window.update()
    
    aiMovement()
    
    # move the ball
    # Ball starts at (0,0) then moves right 2 px(dx value)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        # sets the ball back to position 290 and reverses the ball
        ball.sety(290)
        ball.dy *= -1
        bounceSound.play()
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        bounceSound.play()
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write('Player A: {}      Player B: {}'.format(scoreA, scoreB), align='center', font=('Courier', 24, 'normal'))
        scoreSound.play()
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write('Player A: {}      Player B: {}'.format(scoreA, scoreB), align='center', font=('Courier', 24, 'normal'))
        scoreSound.play()



    # paddle and ball collision
    # if ball coordinate is between 340 and 350 AND if the ball is between the "Size" of the paddle (hence +- 50 corrdinate of paddle) then it will bounce back 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() -50) :
        ball.setx(340)
        ball.dx *= -1
        paddleBounceSound.play()
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() -50) :
        ball.setx(-340)
        ball.dx *= -1
        paddleBounceSound.play()
