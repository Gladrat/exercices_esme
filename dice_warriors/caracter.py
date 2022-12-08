from dice import *

class Caracter:
    def __init__(self, car_name, car_max_hp, car_attack, car_defense, car_dice):
        self._name = car_name
        self._max_hp = car_max_hp
        self._hp = self._max_hp
        self._attack = car_attack
        self._defense = car_defense
        self._dice = car_dice
    
    def __str__(self):
        return f"I'm a caracter ! My name is {self._name}"
    
    def getDice(self):
        return self._dice

    def wound(self, damages):
        self._hp = self._hp - damages

    def isAlive(self):
        if (self._hp > 0):
            print("Alive !")
            return True
        else:
            print(f"Dead noob {self._name}")
            return False
        
    def showHealthBar(self):
        missing_hp = self._max_hp - self._hp
        print(f"hp: {self._hp}")
        print(f"missing hp: {missing_hp}")
        health_bar = f"{'●'*self._hp}{'○'*missing_hp} {self._hp}/{self._max_hp}hp"
        print(health_bar)

    def attack(self):
        damages = 0
        damages = damages + self._attack
        damages = damages + self._dice.roll()
        print(f"BOUM ! {damages}")

    def defense(self, damages):
        damages = damages - self._defense
        damages = damages - self._dice.roll()
        self.wound(damages)

    # def last_breath(self):
    #     pass

if __name__ == "__main__":
    a_dice = Dice(10)
    cheater_dice = RiggedDice(10)
    car1 = Caracter("Julie", 20, 8, 3, a_dice)
    car2 = Caracter("Constance", 10, 12, 3, a_dice)
    print(car1)
    print(car2)  