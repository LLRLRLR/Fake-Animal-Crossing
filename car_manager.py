from turtle import Turtle
import random 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 2


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.increase = MOVE_INCREMENT
        self.STARTING_MOVE_DISTANCE = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle('square')
            #set dimensions to 40 by 20
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto((300,random_y))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.STARTING_MOVE_DISTANCE)

    def increase_level(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT
