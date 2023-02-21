import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Turtle Crossing')

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')
screen.onkey(player.down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        car_current_y = car.ycor()
        car_current_x = car.xcor()
        player_y = player.ycor()
        player_x = player.xcor()

        difference_y = abs(player_y - car_current_y)
        difference_x = abs(player_x - car_current_x)
        if difference_y < 15 and difference_x < 20:
            scoreboard.game_over()
            game_is_on = False

        #Increase the level when player reaches the end
        if player.finish_line():
            scoreboard.update_score()
            player.reset()
            car_manager.increase_level()

#prevents the screen from immediately closing when the game ended
screen.exitonclick()     