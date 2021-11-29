# Import statements ---
from enum import Enum, auto
from dataclasses import dataclass
from abc import ABC, abstractmethod
import typing
from order import Order, BuySell
from trader import Trader
from portfolio import Portfolio
from market import Market


"""
AN IMPORTANT CONSIDERATION IS THAT IN THIS WORLD WE ARE HAPPY FOR PEOPLE TO HAVE A NEGATIVE
QUANTITY ON A MARKET. THINK OF THIS AS HOW SHORT YOU ARE ON THE MARKET
"""

if __name__ == "__main__":
    # I want to create two traders and a market, and have them add some orders and make a trade
    trader_one = Trader("Milan")
    trader_two = Trader("Louis")
    btc_market = Market("Bitcoin")
    trader_one_order = Order(trader_one, BuySell.buy, 100, 100, 0)
    trader_two_order = Order(trader_two, BuySell.sell, 100, 100, 0)

    trader_one.add_order(btc_market, trader_one_order)
    trader_two.add_order(btc_market, trader_two_order)
    trader_one.add_order(btc_market, trader_one_order)

    # I want to see if the traders have the correct portfolio

    assert trader_one.portfolio.portfolio == {"Bitcoin": 100}  # One takes on a position of +100
    assert trader_two.portfolio.portfolio == {"Bitcoin": -100}  # One takes on a position of -100
    assert btc_market.active_bids == {100: [trader_one_order]}  # The market has one bid order at 100
