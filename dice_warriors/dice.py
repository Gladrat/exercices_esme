import random

class Dice:
    def __init__(self, nb_faces):
        self._faces = nb_faces
        self._color = "red"
        self._material = "wood"
        self._type = "normal dice"
        
    def __str__(self):
        return f"I'm a {self._type} with {self._faces} faces"
    
    def roll(self):
        return random.randint(1, self._faces)

class RiggedDice(Dice):
    def __init__(self, nb_faces):
        super().__init__(nb_faces)
        self._type = "rigged dice"
    
    def roll(self, rigged=False):
        if rigged == True:
            return self._faces
        else:
            return super().roll()
        

if __name__ == "__main__":
    my_dice = Dice(20)
    print(my_dice)
    print(my_dice.roll())

    my_rigged_dice = RiggedDice(12)
    print(my_rigged_dice)
    print(my_rigged_dice.roll())
    print(my_rigged_dice.roll(True))