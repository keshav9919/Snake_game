import turtle
import time
import random
delay=0.1
wn=turtle.Screen()
wn.title("snake game by keshav")
wn.setup(width=600,height=600)
wn.bgcolor("green")
wn.tracer(0)
head=turtle.Turtle()
head.shape("square")
head.penup()
head.speed(0)
head.goto(0,0)
head.color("black")
head.penup()
head.direction="stop"
food=turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
segments=[]
score=0
highscore=0
pen=turtle.Turtle()
pen.penup()
pen.shape("square")
pen.goto(0,260)
pen.hideturtle()
pen.write("Score :0 High Score:0 ",align="center",font=("Arial",24,"normal"))


def moveup():
    if(head.direction!="down"):
        head.direction="up"
def movedown():
    if(head.direction!="up"):
        head.direction="down"
def moveleft():
    if(head.direction!="right"):
        head.direction="left"
def moveright():
    if(head.direction!="left"):
        head.direction="right"
    
def move():
    if(head.direction=="up"):
        y=head.ycor()
        head.sety(y+20)
    if(head.direction=="down"):
        y=head.ycor()
        head.sety(y-20)
    if(head.direction=="left"):
        x=head.xcor()
        head.setx(x-20)
    if(head.direction=="right"):
        x=head.xcor()
        head.setx(x+20)
wn.listen()
wn.onkeypress(moveup,"w")
wn.onkeypress(movedown,"s")
wn.onkeypress(moveright,"d")
wn.onkeypress(moveleft,"a")
while True:
    wn.update()
    if(head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290):
        time.sleep(1)
        score=0
        head.goto(0,0)
        head.direction="stop"
        for i in segments:
            i.goto(1000,100)
        segments=[]
        pen.clear()
        pen.write("Score:{} High Score:{}".format(score,highscore),align="center",font=("Arial",24,"normal"))
        
    if(head.distance(food)<20):
        food.goto(random.randint(-290,290),random.randint(-290,290))
        new=turtle.Turtle()
        new.speed(0)
        new.shape("square")
        new.color("grey")
        new.penup()
    
    
        segments.append(new)
        score+=10
        if(score>highscore):
            highscore=score
        pen.clear()
        pen.write("Score:{} High Score:{}".format(score,highscore),align="center",font=("Arial",24,"normal"))
    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)
    if(len(segments)>0):
        segments[0].goto(head.xcor(),head.ycor())
        
        
    move()
    for i in segments:
        if i.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for i in segments:
                i.goto(1000,1000)
            segments=[]
            score=0
            pen.clear()
            pen.write("Score:{} High Score:{}".format(score,highscore),align="center",font=("Arial",24,"normal"))
    time.sleep(delay)
#keyboard


    


wn.mainloop()
