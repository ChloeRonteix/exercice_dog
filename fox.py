from dog import Dog
import random
from animals import Animals

class Fox(Animals):

    def __init__(self, name, age):
        Animals.__init__(self, name, age)
        self.race = 'Fox'
        self.rabbit = 0
        

    def rabbit_kill(self):
        if self.age <= 5:
            rabbit = random.choice(range(5,11))
        elif self.age >= 15:
            rabbit = random.choice(range(16,30))
        else:
            rabbit = random.choice(range(11,16))
        self.rabbit += rabbit
        print(f'{self.name} killed {self.rabbit} rabbits.')

    def life(self):
        self.rabbit_kill()


    
