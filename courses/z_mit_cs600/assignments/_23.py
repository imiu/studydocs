from matplotlib import pyplot
import random

class Stock(object):
    """docstring for Stock"""
    def __init__(self, price, distribution):
        self.price = price
        self.history = [price]
        self.distribution = distribution
        self.last_change = 0
    
    def set_price(self, price):
        """docstring for set_price"""
        self.price = price
        self.history.append(price)
    
    def get_price(self):
        """docstring for get_price"""
        return self.price

    def make_move(self, mkt_bias, mo):
        """docstring for make_move"""
        if self.price == 0.0:
            return
        old_price = self.price
        base_move = self.distribution() + mkt_bias
        self.price = self.price * (1.0 + base_move)
        if mo:
            self.price = self.price + random.gauss(.5, .5) * self.last_change
        if self.price < 0.01:
            self.price = 0.0
        self.history.append(self.price)
        self.last_change = old_price - self.price
    
    def show_history(self, fig_num):
        """docstring for show_history"""
        pyplot.figure(fig_num)
        pyplot.plot(self.history)
        pyplot.title('History for ' + str(fig_num))
        pyplot.xlabel('Time')
        pyplot.ylabel('Price')


def test_stock():
    def run_sim(stks, fig, mo):
        """docstring for run_sim"""
        mean = 0.0
        for s in stks:
            for d in range(num_days):
                s.make_move(bias, mo)
            s.show_history(fig)
            mean += s.get_price()
        mean = mean / float(num_stocks)
        pyplot.axhline(mean)
    num_stocks = 20
    num_days = 100
    stks1 = []
    stks2 = []
    bias = 0.005
    mo = True
    for i in range(num_stocks):
        volatility = random.uniform(0, 0.2)
        d1 = lambda: random.uniform(-volatility, volatility)
        d2 = lambda: random.gauss(0.0, volatility / 2.0)
        stks1.append(Stock(100.0, d1))
        stks2.append(Stock(100.0, d2))
    run_sim(stks1, 1, mo)
    run_sim(stks2, 2, mo)

test_stock()
pyplot.show()
assert False