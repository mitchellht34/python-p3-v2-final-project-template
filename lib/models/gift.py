from models.__init__ import CURSOR, CONN
from models.recipient import Recipient

class Gift:

    all = {}

    def __init__(self, name, price, recipient_id, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.recipient_id = recipient_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
        
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price:
            self._price = price
        else:
            raise ValueError(
                "price should be a price"
            )

    