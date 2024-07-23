from time import sleep
from threading import Thread


class Knight(Thread):
    INVADERS = 100
    day = 0

    def __init__(self, name, skills, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skills = skills

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.INVADERS > 0:
            self.day = self.day + 1
            self.INVADERS = self.INVADERS - self.skills
            print(f"{self.name} сражается {self.day} дней, осталось {self.INVADERS} воинов", flush=True)
            sleep(1)
        print(f"{self.name} одержал победу спустя {self.day} дней", flush=True)


t1 = Knight(name='Sir Lanselot', skills=20)
t2 = Knight(name='Sir Galahad', skills=10)

t1.start()
t2.start()

t1.join()
t2.join()

print("Все битвы закончились!")