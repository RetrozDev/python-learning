def main():
    # Chapter 0 : Introduction
    print("Hello, World!")


    # Chapter 1 : Variables and Data Types
    username = "Retroz" # String
    age = 25 # Integer
    age = age + 10 # Expected 35
    wallet = 100.50 # Float
    is_active = True # Boolean
    user_info = {
        "username": username,
        "age": age,
        "wallet": wallet,
        "is_active": is_active
    } # Object

    print(f"User Info: {user_info}")


    # Chapter 2 : If Else
    price = 80

    if wallet >= price:
        wallet -= price
        print(f"Purchase successful! Remaining wallet balance: {wallet}")

    elif wallet < 0:
        print("Wallet balance cannot be negative!")
        wallet = 0
    else:
        print("Insufficient funds!")


    # Chapter 3 : Array
    online_players = ["Player1", "Player2", "Player3"]
    print(f"Online Players: {online_players}")
    print(f"First Player: {online_players[0]}")
    print(f"Last Player: {online_players[len(online_players)-1]}")
    # Change first player username :
    online_players[0] = "NewPlayer1"
    print(f"Updated First Player: {online_players[0]}")
    online_players.insert(2, "InsertedPlayer")
    print(f"Updated Online Players: {online_players}")
    online_players[2:len(online_players) - 1] = ["NewPlayer2", "NewPlayer3"]
    print(f"Final Online Players: {online_players}")
    online_players.append("Player4")
    print(f"Final Online Players after append: {online_players}")


    # Chapter 4 : Loops
    # 1: for loop
    for player in online_players:
        print(f"Username: {player} n°: {online_players.index(player)+1}")
    # 2: while loop
    i = 1
    while i <= 10:
        print(f"i: {i}")
        i += 1


    # Chapter 5: functions
    def multiply(a, b):
        return a * b

    result = multiply(5, 10)
    print(f"Multiplication Result: {result}") # Expected 50

    def return_max(a, b):
        return a if a > b else b

    max_result = return_max(5, 10)
    print(f"Max Result: {max_result}") # Expected 10


    # chapter 6 : Class
    class Player :
        def __init__(self, username, health, attack):
            self.username = username
            self.health = health
            self.attack = attack
            print(f"{self.username} created with {self.health} health and {self.attack} attack.")

        def take_damage(self, damage):
            if self.health - damage <= 0:
                self.health = 0
                print(f"{self.username} has been defeated!")
            else: self.health -= damage
            print(f"{self.username} took {damage} damage. Remaining health: {self.health}")

    player1 = Player("Player 1", 20.0, 5.0)

    player2 = Player("Player 2", 30.0, 10.0)

    player1.take_damage(5)
    player2.take_damage(30)

if __name__ == "__main__":
    main()