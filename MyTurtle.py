'''
  Vinicius R. Miguel
  github.com/vrmiguel/MyTurtle
  Messing around with Turtle trying to learn some of it.
'''

import turtle

class MyTurtle:
  t = None #Placeholder for a Turtle
  def __init__(self, x = 0, y = 0, speed = 1):
    self.t = turtle.Turtle()
    self.t.speed = speed
    if(x != 0 or y != 0):
      self.t.penup()
      self.t.goto(x, y)
      self.t.pendown()
  
  def disable_pen(self):
    self.t.penup()
  
  def enable_pen(self):
    self.t.pendown()

  def forward(self, x = 20):
    self.t.forward(x)

  def goto(self, x = 0, y = 0):
    self.t.penup()
    self.t.goto(x, y)
    self.t.pendown()
  
  def set_speed(self, speed=2):
    self.t.speed = speed

  def make_triangle(self, siz = 50, direction = 'down'):
    if(direction not in ['up', 'down']):
      raise Exception('Incorrect input on make_triangle()')
    self.make_regular_polygon(3, siz, direction)

  # Makes the turtle draw a square. Copied straight from repl.it's example on Turtle. :P
  def make_square(self, moveDistance=75):
    for c in ['red', 'green', 'yellow', 'blue']:
      self.t.color(c)
      self.t.forward(moveDistance)
      self.t.left(90)

  def make_circle(self, siz = 50):
    self.t.circle(siz)

  def set_color(self, color = 'blue'):
    self.t.color(color)

    # Makes a spiral from making several little squares.
    # Warning: This'll take a while to finish.
  def make_spiral(self): 
    size = 1
    while(size is not 500):
      self.t.forward(size)
      self.t.right(91)
      size += 1

  def make_nautilus(self):
    size = 1
    while(size is not 500):
      for _ in [2, 3, 4, 5]:
        self.t.forward(size)
        self.t.right(90)
        size += 1
      self.t.right(10)

  def make_star(self, siz = 50):
    for i in range(5):
      self.t.forward(siz)
      self.t.right(144)

  def make_regular_polygon(self, num_sides = 5, siz = 50, direction = 'down'):
    if (num_sides < 3 or direction not in ['up', 'down']):
      raise Exception("Incorrect input on make_regular_polygon()")

    angle = 360.0 / num_sides
    if (direction == 'down'):
      for i in range(num_sides):
        self.t.forward(siz)
        self.t.right(angle)
    elif (direction == 'up'):
      for i in range(num_sides):
        self.t.forward(siz)
        self.t.left(angle)

if __name__ == '__main__':
  t = MyTurtle(0, 0)
  t.set_speed("fastest")
  t.make_square()
  t.set_color()  
  t.goto(100,0)
  t.make_triangle()
  t.make_triangle(50, 'up')
  t.make_regular_polygon()
  t.make_regular_polygon(5, 50, 'up')
  t.goto(250, 65) 
  t.make_regular_polygon(8)
  t.goto(400, 65)
  t.make_star()
  #t.make_regular_polygon(300, 0.5)
  t.make_nautilus()
