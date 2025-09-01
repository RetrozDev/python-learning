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

if __name__ == "__main__":
    main()