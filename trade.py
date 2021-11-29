from dataclasses import dataclass
from trader import Trader


@dataclass
class Trade:
    buyer: Trader
    seller: Trader
    quantity: float
    market: str

    def __post_init__(self):
        self.buyer.profit_loss += self.quantity * self.seller.portfolio.portfolio[self.market]
        self.seller.profit_loss -= self.quantity * self.buyer.portfolio.portfolio[self.market]

        self.seller.portfolio.portfolio[self.market] -= self.quantity
        self.buyer.portfolio.portfolio[self.market] += self.quantity
