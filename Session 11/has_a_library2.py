class Library:
    def __init__(self, games=[]):
        self.games = games
        self.number_of_games = len(games)

    def show(self):
        print("-------------Library-------------")
        for name in self.games:
            name.show()
        print("number_of_games:",self.number_of_games)
        print("--------------------------")
