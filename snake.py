POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
       new_segment = Turtle("square")
       new_segment.color("white")
       new_segment.penup()
       new_segment.goto(position)
       self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[i - 1].xcor()
            new_ycor = self.segments[i - 1].ycor()
            self.segments[i].goto(new_xcor, new_ycor)

        self.segments[0].forward(20)

    def up(self):
        if(self.segments[0].heading() != DOWN):
          self.segments[0].setheading(UP)
    def down(self):
        if (self.segments[0].heading() != UP):
          self.segments[0].setheading(DOWN)
    def left(self):
        if (self.segments[0].heading() != RIGHT):
          self.segments[0].setheading(LEFT)

    def right(self):
        if (self.segments[0].heading() != LEFT):
          self.segments[0].setheading(RIGHT)
