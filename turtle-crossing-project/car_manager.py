from turtle import Turtle 
import random 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SHAPE_SIZE = (2, 4, 5)


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        

    def car_position_y(self):
        return random.randint(-250,250)
        pass


    def create_car(self):
        number_of_cars = random.randint(1, 6)
        if number_of_cars == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, self.car_position_y())
            self.all_cars.append(new_car)
        pass

    def drive(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        pass

    def drive_fast(self):
        self.car_speed += MOVE_INCREMENT
        pass
    pass
