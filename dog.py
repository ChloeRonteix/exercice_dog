import time
import random


class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.live = True
        self.weight = weight
        self.eat = 50
        self.drink = 50
        self.sleep = 50
    
    def life(self):
        while self.live == True:
            self.dead()
            self.dog_eat()
            print(f'{self.name} has {self.age} years and weigh {self.weight} grams.')
            self.one_year_pass()
            self.add_weigth()
            self.dog_weight()
            self.live_dog()
            time.sleep(1)

    def add_year(self):
        self.age += 1
        return self.age
        
    def one_year_pass(self):
        self.add_year()

    def dead(self):
        live = random.choice(range(1,10))
        if self.age >= 10:
            if live > 7:
                self.live = False
                          

    def live_dog(self):
        if self.live == False:
            print(f'{self.name} is dead :\'(')
            

    def add_weigth(self):
        if self.age <= 10:
            self.weight += 2
        else:
            self.weight += random.choice(range(1,4))
    
    def dog_weight(self):
        if self.weight <= 1:
            self.live = False
    
    def choice_eat(self):
        choice_meat = ['carrot','bacon','water','chocolate', 'nothing']
        print('Dog needs to eat. Choice between \n 1: carrot, 2: bacon, 3: chocolate, 4: nothing')
        eat = int(input('Choice the meat for the dog : '))
        if eat not in [1, 2, 3, 4]:
            print(f'Do not give shit to the dog please. Select in the list {choice_meat}')
            return
        return eat
    
    def dog_eat(self):
        eat = self.choice_eat()
        menu = []
        if eat == 1:
            self.eat += 5
            print(f'Croc croc the carrot.... But {self.name} is not a rabbit!')
        elif eat == 2:
            self.eat += 15
            self.weight += 1
            print(f'{self.name} had a good meat!')
        elif eat == 3:
            self.eat += random.choice([10, -10])
            self.weight += 2
        else:
            self.eat -= 20
            self.weight -= 5
        menu.append(eat)
        
        