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

if __name__ == "__main__":
    main()