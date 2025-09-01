from chapter6_class import Player

class Warrior(Player):
    def __init__(self, username, health, attack):
        super().__init__(username, health, attack)
        self.attack = attack
        self.armor = 3

    def take_damage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0
        else:
            self.health -= damage

    def blade(self):
        self.armor = 3