# bounce.py
#
# Exercise 1.5
ball_height = 100  #Initial height in meters
num_bounces = 1

while num_bounces <= 10:
    ball_height = round(ball_height *(3/5), 4)
    print(num_bounces, ball_height)
    num_bounces = num_bounces + 1
    
