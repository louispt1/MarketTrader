import typing
from portfolio import Portfolio
from order import Order

class Trader:
    def __init__(self, name: str):
        self.name = name
        self.profit_loss = 0
        self.portfolio = Portfolio()

