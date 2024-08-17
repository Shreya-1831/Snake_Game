from turtle import Turtle
pos = [(0, 0), (-20, 0), (-40, 0)]
moved = 20


class Snake:
    def __init__(self):
        self.seg = []
        self.create_snake()
        self.head = self.seg[0]

    def create_snake(self):
        for p in pos:
            self.add_seg(p)

    def add_seg(self, p):
        nw = Turtle(shape="square")
        nw.color("white")
        nw.penup()
        nw.goto(p)
        self.seg.append(nw)

    def reset(self):
        for se in self.seg:
            se.goto(1000,1000)
        self.seg.clear()
        self.create_snake()
        self.head = self.seg[0]

    def extend(self):
        self.add_seg(self.seg[-1].position())

    def move(self):
        for seq in range(len(self.seg)-1, 0, -1):
            new_x = self.seg[seq - 1].xcor()
            new_y = self.seg[seq - 1].ycor()
            self.seg[seq].goto(new_x, new_y)
        self.head.forward(moved)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
