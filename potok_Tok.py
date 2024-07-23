INVADERS = 100
day = 0
skills = 20

while INVADERS > 0:
    day = day + 1
    INVADERS = INVADERS - skills
    print(f"сражается {day} дней, осталось {INVADERS} воинов")


