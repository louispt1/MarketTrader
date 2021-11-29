from portfolio import Portfolio
from market import Market
from order import Order, BuySell

class Trader:
    def __init__(self, name: str):
        self.name = name
        self.profit_loss = 0
        self.portfolio = Portfolio()

    def add_order(self, market: Market, order: Order):
        if order.side == BuySell.buy:
            market.add_bid(order)
        else:
            market.add_ask(order)

