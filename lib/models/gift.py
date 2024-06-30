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

    @property
    def recipient_id(self):
        return self._recipient_id
    
    @recipient_id.setter
    def recipient_id(self, recipient_id):
        if type(recipient_id) is int and Recipient.find_by_id(recipient_id):
            self._recipient_id = recipient_id
        else:
            raise ValueError(
                "recipient_id must reference a recipient in the database"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Gift instances """
        sql = """
            CREATE TABLE IF NOT EXISTS gifts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            recipient_id INTEGER,
            FOREIGN KEY (recipient_id) REFERENCES recipients(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Gift instances """
        sql = """
            DROP TABLE IF EXISTS gifts;
        """
        CURSOR.execute(sql)
        CONN.commit()