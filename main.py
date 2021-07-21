from score_board import Score_Board
from food import Food
from turtle import Screen,Turtle
from snake import Snake_class


import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake_class()
food=Food()
score_board=Score_Board()

screen.listen() #to see if or any keys are pressed if 
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True
#game_loop beginning
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    #detect Collision with Food
    if snake.head.distance(food)< 15:
        food.re_position()
        score_board.score_update()
        snake.extend()
    #detect collision with Wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        score_board.game_over()
    #Detect Collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 18:
            game_is_on=False
            score_board.game_over()
screen.exitonclick()
    


        