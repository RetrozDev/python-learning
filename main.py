from chapter1_variables import VariablesAndDataTypes
from chapter2_ifelse import IfElse
from chapter3_array import ArrayChapter
from chapter4_loops import LoopsChapter
from chapter5_functions import FunctionsChapter
from chapter6_class import Player
from chapter7_inheritance import Warrior

def main():
    # Chapter 0 : Introduction
    print("Hello, World!")

    # Chapter 1 : Variables and Data Types
    chapter1 = VariablesAndDataTypes()
    chapter1.show_user_info()

    # Chapter 2 : If Else
    chapter2 = IfElse(chapter1.wallet)
    wallet_after_purchase = chapter2.purchase()

    # Chapter 3 : Array
    chapter3 = ArrayChapter()
    chapter3.show_players()
    chapter3.update_players()

    # Chapter 4 : Loops
    chapter4 = LoopsChapter(chapter3.online_players)
    chapter4.for_loop()
    chapter4.while_loop()

    # Chapter 5: Functions
    result = FunctionsChapter.multiply(5, 10)
    print(f"Multiplication Result: {result}") # Expected 50
    max_result = FunctionsChapter.return_max(5, 10)
    print(f"Max Result: {max_result}") # Expected 10

    # Chapter 6 : Class
    player1 = Player("Player 1", 20.0, 5.0)
    player2 = Player("Player 2", 30.0, 10.0)
    player1.take_damage(5)
    player2.take_damage(30)

    # Chapter 7: Inheritance
    warrior1 = Warrior("Warrior 1", 100.0, 15.0)
    warrior1.take_damage(10)
    print(f"Warrior 1 - Health: {warrior1.health}, Armor: {warrior1.armor}")

if __name__ == "__main__":
    main()