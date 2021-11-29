from dataclasses import dataclass
from enum import Enum, auto


class BuySell(Enum):
    buy = 1  # We choose 1 and -1 to make the maths easier later
    sell = -1


@dataclass  # Use a dataclass to define the trade class, this automatically adds things like ability to print so we can see if its working
class Order:
    trader: 'Trader'
    side: BuySell
    quantity: float
    price: float
    identity: int
