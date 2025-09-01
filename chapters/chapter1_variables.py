# Chapter 1: Variables and Data Types
class VariablesAndDataTypes:
    def __init__(self):
        self.username = "Retroz"  # String
        self.age = 25  # Integer
        self.age = self.age + 10  # Expected 35
        self.wallet = 100.50  # Float
        self.is_active = True  # Boolean
        self.user_info = {
            "username": self.username,
            "age": self.age,
            "wallet": self.wallet,
            "is_active": self.is_active
        }  # Object

    def show_user_info(self):
        print(f"User Info: {self.user_info}")
