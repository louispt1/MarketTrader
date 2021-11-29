# Import statements ---
from enum import Enum


class Trader:
    UserID: str
    # current trades --> list of current Trades TODO
   
#    Constructor
    def ___init___(self):
     self.UserID = ""

# Setter methods
    def setUser(self, id: str):
     self.UserID = id

#  Getter methods
    def getUser(self):
       return self.UserID

class buySell(Enum):
    buy = 0
    sell =1

class Trade:
    buy: bool
    quantity: float
    price: float
    identity: str

# Constructor
    def ___init___(self):
     self.buy = True
     self.quantity = 0
     self.price = 0
     self.identity = ""

# Setter methods
    def setQuant(self, quant: float):
        self.quantity = quant
        return self.quantity

    def setPrice(self, price: float):
        self.price = price
        return self.price

    def setBuy(self, buy: bool):
        self.buy = buy
        return self.buy

# Getter methods
    def getQuant(self):
        return self.quantity

    def getPrice(self):
        return self.price
        
    def getBuy(self):
        return self.buy
