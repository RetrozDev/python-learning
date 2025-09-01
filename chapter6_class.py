# Chapter 6: Class
class Player:
    def __init__(self, username, health, attack):
        self.username = username
        self.health = health
        self.attack = attack
        print(f"{self.username} created with {self.health} health and {self.attack} attack.")

    def take_damage(self, damage):
        if self.health - damage <= 0:
            self.health = 0
            print(f"{self.username} has been defeated!")
        else:
            self.health -= damage
        print(f"{self.username} took {damage} damage. Remaining health: {self.health}")
