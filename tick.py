class Tick:
    def __init__(self, open_p, high, low, close, rising_rate):
        self.open = open_p
        self.high = high
        self.low = low
        self.close = close
        self.rising_rate = str(round(rising_rate*100, 2))+"%"
        self.rising_rate_i = rising_rate

    def __str__(self):
        return self.rising_rate + "\t" + self.close + "\t" + self.high + "\t" + self.low + "\t" + self.open
