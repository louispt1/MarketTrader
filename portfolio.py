from collections import defaultdict
import typing

class Portfolio:
    def __init__(self):
        self.portfolio: typing.Dict[str:int] = defaultdict(
            int
        )  # When a trade executes, the traders will update their portfolios with the new quantity of the trade

    def add_trade(self, symbol: str, quantity: int, side: int):
        self.portfolio[symbol] += side * quantity
