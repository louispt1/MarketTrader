# Import statements ---
from enum import Enum, auto
from dataclasses import dataclass
from abc import ABC, abstractmethod
import typing
from order import Order, BuySell
from trader import Trader
from portfolio import Portfolio


"""
AN IMPORTANT CONSIDERATION IS THAT IN THIS WORLD WE ARE HAPPY FOR PEOPLE TO HAVE A NEGATIVE
QUANTITY ON A MARKET. THINK OF THIS AS HOW SHORT YOU ARE ON THE MARKET
"""


class Market:
    """Class that represents a `market`, where a market
    is an individual product that can be traded."""

    def __init__(self, marketName: str):
        self.marketName = marketName
        self.traders: typing.Set[Trader] = set()  # We can use a set instead of a list for faster look-up
        self.active_bids: typing.Dict[
            int : typing.List[Order]
        ] = dict()  # This maps a bid (request to buy) order's price (integer, in cents) to a list of orders at that price
        self.active_asks: typing.Dict[
            int : typing.List[Order]
        ] = dict()  # This maps an ask (request to sell) order's price (integer, in cents) to a list of orders at that price
        self.best_bid_price: int = 0  # The best bid price is the price of the highest bid order
        self.best_ask_price: int = float(
            "inf"
        )  # The best ask price is the price of the lowest ask order, MYPY FLAG type: ignore

    def add_bid(self, order: Order):
        """Add a new bid order to the market."""
        # 1. Check whether the bid price is greater than the best ask price, if so, execute a trade
        if order.price >= self.best_ask_price:
            # TODO MAKE A TRADE HERE
            pass
        else:  # Add the order to the active bids
            self.active_bids[order.price].append(order)

    def add_ask(self, order: Order):
        """Add a new ask order to the market."""
        # 1. Check whether the ask price is less than the best bid price, if so, execute a trade
        if order.price <= self.best_bid_price:
            # TODO MAKE A TRADE HERE, this should execute the traders
            pass
        else:
            self.active_asks[order.price].append(order)


class TraderOnMarket:
    """Class that represents a trader on a market, this gives the trader the ability to actually make trades."""

    def __init__(self, trader: Trader, market: Market):
        self.trader = trader
        self.market = market

    def add_order(self, order: Order):
        """Add a new order to the market."""
        # TODO add the order to the market using the market functions
        pass


if __name__ == "__main__":
    # I want to create two traders and a market, and have them add some orders and make a trade
    trader_one = Trader("Milan")
    trader_two = Trader("Louis")
    btc_market = Market("Bitcoin")
    trader_one_order = Order(BuySell.buy, 100, 100, 0)
    trader_two_order = Order(BuySell.sell, 100, 100, 0)

    trader_one.add_order(btc_market, trader_one_order)
    trader_two.add_order(btc_market, trader_two_order)
    trader_one.add_order(btc_market, trader_one_order)

    # I want to see if the traders have the correct portfolio

    assert trader_one.portfolio.portfolio == {"Bitcoin": 100}  # One takes on a position of +100
    assert trader_two.portfolio.portfolio == {"Bitcoin": -100}  # One takes on a position of -100
    assert btc_market.active_bids == {100: [trader_one_order]}  # The market has one bid order at 100
