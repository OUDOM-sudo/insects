import turtle
import random 

randomColor = ["red", "blue", "green", "yellow", "pink", "brown", "black", "purple"]
radiusSize = [10, 70, 80, 10, 20, 30, 50]
numbers = [-100, -50, 188, 177, 199, -99, -30, 0, 10, 20, 30, 40, 50, 100, 200, -200, -188]

t = turtle.Turtle()
t.speed(10) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest


for i in range(100):
  t.color(random.choice(randomColor))
  t.begin_fill()
  t.circle(random.choice(radiusSize))
  t.color(random.choice(randomColor))
  t.goto(-random.choice(numbers), random.choice(numbers))
  t.end_fill()
  for x in range(3):
   t.color(random.choice(randomColor))
   t.begin_fill()
   t.forward(random.choice(radiusSize))
   t.left(120)
   t.end_fill()



