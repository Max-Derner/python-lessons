import random


dots_dropped = 0
dots_hitting_quarter_circle = 0

while True:
    resolution = 1_000_000
    rand_x = random.randint(1, resolution)
    rand_y = random.randint(1, resolution)

    dots_dropped += 1
    if rand_x**2 + rand_y**2 <= resolution**2:
        dots_hitting_quarter_circle += 1

    pistemation = 4 * dots_hitting_quarter_circle / dots_dropped
    print(pistemation)
