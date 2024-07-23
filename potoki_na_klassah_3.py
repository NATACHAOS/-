from time import sleep
class Knight:
    INVADERS = 100
    day = 0
    skills = 20

    def run(self):
        while self.INVADERS > 0:
            self.day = self.day + 1
            self.INVADERS = self.INVADERS - self.skills
            print(f"сражается {self.day} дней, осталось {self.INVADERS} воинов")
            sleep(1)



my_obj = Knight()
my_obj.run()
print(f"Рыцарь одержал победу спустя {my_obj.day} дней")