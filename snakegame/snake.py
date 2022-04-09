from turtle import Turtle

INITIAL_POS = [(0, 0), (-20, 0), (-40, 0)]
TRAVEL_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for positions in INITIAL_POS:
            seg_1 = Turtle(shape="square")
            seg_1.color("white")
            seg_1.penup()
            seg_1.goto(positions)
            self.segment.append(seg_1)

    def move(self):
        for seg_no in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_no - 1].xcor()
            new_y = self.segment[seg_no - 1].ycor()
            self.segment[seg_no].goto(new_x, new_y)
        self.head.forward(TRAVEL_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

