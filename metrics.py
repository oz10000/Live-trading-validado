class Metrics:

    def __init__(self):

        self.trades = 0
        self.wins = 0
        self.pnl = 0

    def update(self, result):

        self.trades += 1
        self.pnl += result

        if result > 0:
            self.wins += 1

    def winrate(self):

        if self.trades == 0:
            return 0

        return self.wins / self.trades
