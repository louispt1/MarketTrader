import typing
from collections import defaultdict

class Market:
    """Class that represents a `market`, where a market
    is an individual product that can be traded."""

    def __init__(self, marketName: str):
        self.marketName = marketName
        self.traders: typing.Set['Trader'] = set()  # We can use a set instead of a list for faster look-up
        self.active_bids: typing.Dict[
            int : typing.List['Order']
        ] = defaultdict(list)  # This maps a bid (request to buy) order's price (inxteger, in cents) to a list of orders at that price
        self.active_asks: typing.Dict[
            int : typing.List['Order']
        ] = defaultdict(list)  # This maps an ask (request to sell) order's price (integer, in cents) to a list of orders at that price
        self.best_bid_price: int = 0  # The best bid price is the price of the highest bid order
        self.best_ask_price: int = float(
            "inf"
        )  # The best ask price is the price of the lowest ask order, MYPY FLAG type: ignore

    def add_bid(self, order: 'Order'):
        """Add a new bid order to the market."""
        # 1. Check whether the bid price is greater than the best ask price, if so, execute a trade
        if order.price >= self.best_ask_price:
            # TODO MAKE A TRADE HERE
            pass
        else:  # Add the order to the active bids
            self.active_bids[order.price].append(order)

    def add_ask(self, order: 'Order'):
        """Add a new ask order to the market."""
        # 1. Check whether the ask price is less than the best bid price, if so, execute a trade
        if order.price <= self.best_bid_price:
            # TODO MAKE A TRADE HERE, this should execute the traders
            pass
        else:
            self.active_asks[order.price].append(order)
