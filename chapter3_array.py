# Chapter 3: Array
class ArrayChapter:
    def __init__(self):
        self.online_players = ["Player1", "Player2", "Player3"]

    def show_players(self):
        print(f"Online Players: {self.online_players}")
        print(f"First Player: {self.online_players[0]}")
        print(f"Last Player: {self.online_players[len(self.online_players)-1]}")

    def update_players(self):
        self.online_players[0] = "NewPlayer1"
        print(f"Updated First Player: {self.online_players[0]}")
        self.online_players.insert(2, "InsertedPlayer")
        print(f"Updated Online Players: {self.online_players}")
        self.online_players[2:len(self.online_players) - 1] = ["NewPlayer2", "NewPlayer3"]
        print(f"Final Online Players: {self.online_players}")
        self.online_players.append("Player4")
        print(f"Final Online Players after append: {self.online_players}")
