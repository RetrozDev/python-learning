# Chapter 4: Loops
class LoopsChapter:
    def __init__(self, online_players):
        self.online_players = online_players

    def for_loop(self):
        for player in self.online_players:
            print(f"Username: {player} n°: {self.online_players.index(player)+1}")

    def while_loop(self):
        i = 1
        while i <= 10:
            print(f"i: {i}")
            i += 1
