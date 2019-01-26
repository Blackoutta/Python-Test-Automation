lottery_player_dict = {
    "name": "Rolf",
    "numbers": {5, 9, 12, 3, 1, 21}
}

class LotteryPlayer(object):
    """This is a lottery player class"""
    def __init__(self, name):
        self.name = name
        self.number = {5, 9, 12, 3, 1, 21}

    def total(self):
        return sum(self.number)

    @staticmethod
    def say_win():
        print("I win!")

player1 = LotteryPlayer("Yang")
player2 = LotteryPlayer("John")
