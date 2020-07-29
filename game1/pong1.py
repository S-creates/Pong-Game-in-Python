# Part 1 : getting started
import turtle


wn = turtle.Screen()
wn.title("Pong by @SALIOU")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
 
# Paddle A
    
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ring game
ring_game2 = turtle.Turtle()
ring_game2.speed(0)
ring_game2.shape("square")
ring_game2.color("white")
ring_game2.shapesize(stretch_wid=0.1, stretch_len=35)
ring_game2.penup()
ring_game2.goto(0, 306) 

# Ring game
ring_game4 = turtle.Turtle()
ring_game4.speed(0)
ring_game4.shape("square")
ring_game4.color("white")
ring_game4.shapesize(stretch_wid=0.1, stretch_len=35)
ring_game4.penup()
ring_game4.goto(0, -306)
# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
# Score
score_a = 0
score_b = 0





# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)    
def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)    


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop

while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
   
    # Border checking
    if ball.ycor() > 292:  
        ball.sety(292)
        ball.dy *= -1
    if ball.ycor() < -292:  
        ball.sety(-292)
        ball.dy *= -1       
    if ball.xcor() > 345:  
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
         

    if ball.xcor() < -345:  
        ball.goto(0, 0)
        ball.dx *= -1 
        score_b += 1  
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) 
        


    # Paddle and Ball Collision
    if ball.xcor() > 322 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 44 and ball.ycor() > paddle_b.ycor() - 44):
        ball.setx(322)
        ball.dx *= -1
    if ball.xcor() < -322 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 44 and ball.ycor() > paddle_a.ycor() - 44):
        ball.setx(-322)
        ball.dx *= -1        

