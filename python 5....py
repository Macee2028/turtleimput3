import turtle
import random

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('black')


t=turtle.Turtle()
#menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('white')
t.write("Background Color",font=("arial",30,"normal"),align = "center")

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor('tan')
t.write("1. Tan",font=("arial",20,"normal"),align = "left")

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor('azure')
t.write("2. Azure",font=("arial",20,"normal"),align = "left")

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor('aquamarine')
t.write("3. Aquamarine",font=("arial",20,"normal"),align = "left")

t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor('darkkhaki')
t.write("4. DarkKhaki",font=("arial",20,"normal"),align = "left")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor('white')
t.write("Choose One",font=("arial",30,"normal"),align = "center")

choose = int(input("Choose One: "))
if choose == 1:
    screen.bgcolor('tan')
elif choose == 2:
    screen.bgcolor('azure')
elif choose == 3:
    screen.bgcolor('aquamarine')
else:
    screen.bgcolor('darkkhaki')
t.clear()
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('black')
t.write("Enter Your Name",font=("arial",30,"normal"),align = "center")
name = input("Enter your name: ")
t.clear()
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
num1 = random.randint(-100,100)
num2 = random.randint(-100,100)

solution = num1 - num2

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor('red')
t.write(name,font=("arial",30,"normal"),align = "center")


t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor('blue')
t.write(num1,font=("arial",30,"normal"),align = "center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor('purple')
t.write("+",font=("arial",30,"normal"),align = "center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('green')
t.write(num2,font=("arial",30,"normal"),align = "center")

t.penup()
t.goto(100,0)
t.pendown()
t.pencolor('purple')
t.write("=",font=("arial",30,"normal"),align = "center")

answer = float(input("What is the answer: "))

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor('black')
t.write(sum,font=("arial",30,"normal"),align = "center")



t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('black')
t.write(solution,font=("arial",30,"normal"),align = "center")

if answer == sum:
    screen.bgcolor("dodgerblue")
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.pencolor('black')
    t.write("Correct", font=("arial", 30, "normal"), align="center")
else:
    screen.bgcolor("darkorange")
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.pencolor('black')
    t.write("Incorrect", font=("arial", 30, "normal"), align="center")

turtle.done()
