from dice import *

class Caracter:
    _type = "Caracter"
    
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
    
    def getType(self):
        return self._type
    
    # def setType(self, new_type):
    #     self._type = new_type

    def get_name(self):
        return self._name

    def wound(self, damages):
        self._hp = self._hp - damages

    def isAlive(self):
        if (self._hp > 0):
            # print("Alive !")
            return True
        else:
            # print(f"Dead noob {self._name}")
            return False
        
    def showHealthBar(self):
        if (self._hp < 0):
            self._hp = 0
        missing_hp = self._max_hp - self._hp
        # print(f"hp: {self._hp}")
        # print(f"missing hp: {missing_hp}")
        health_bar = f"{'●'*self._hp}{'○'*missing_hp} {self._hp}/{self._max_hp}hp"
        print(health_bar)

    def compute_damages(self, result):
        damages = 0
        damages = damages + self._attack
        damages = damages + result
        return damages

    def attack(self, target):
        if (self.isAlive()):
            result = self._dice.roll()
            damages = self.compute_damages(result)
            print(f"► {self._type} {self._name} attack {target.get_name()} with {damages} damages : {self._attack} (attack) + {result} (roll)")
            target.defense(damages, self)

    def defense(self, damages, attacker):
        wounds = damages - self._defense
        result = self._dice.roll()
        wounds = wounds - result
        if (wounds < 0):
            wounds = 0
        print(f"◄ {self._type} {self._name} take {wounds} wounds from {attacker.get_name()} : {damages} (damages) - {self._defense} (defense) - {result} (roll)")
        self.wound(wounds)
        self.showHealthBar()

    # def last_breath(self):
    #     pass

class Warrior(Caracter):
    _type = "Warrior"

    def compute_damages(self, result):
        damages = super().compute_damages(result)
        damages = damages + 3
        print("► Coup de hache ! (3)")
        return damages

class Mage(Caracter):
    _type = "Mage"
    
    # Bonus de défense de 3
    
class Thief(Caracter):
    _type = "Thief"
    
class Necromancer(Caracter):
    _type = "Necromancer"
    
class Princess(Caracter):
    _type = "Princess"

if __name__ == "__main__":
    a_dice = Dice(20)
    
    car1 = Mage("Oliver", 20, 8, 3, a_dice)
    car2 = Warrior("Elsa", 20, 8, 3, a_dice)
    
    while(car1.isAlive() and car2.isAlive()):
        car1.attack(car2)
        car2.attack(car1)