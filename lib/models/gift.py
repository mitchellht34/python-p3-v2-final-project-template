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
    
    def save(self):
        """ Insert a new row with the name, price, and recipient id values of the current Gift object.
        Update object id attribute using the primary key values of new row.
        Save the object in local dictionary using table row's PK as dictionary key """
        sql = """
            INSERT INTO gifts (name, price, recipient_id)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.price, self.recipient_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, price, recipient_id):
        """ Initialize a new Gift instance and save the object to the database """
        gift = cls(name, price, recipient_id)
        gift.save()
        return gift

    def delete(self):
        """ Delete the table corresponding to the current Gift instance,
        delete the dictionary entry, and reassign id attribute """
        sql = """
            DELETE FROM gifts
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """ Return a Gift object having the attribute values from the table row """

        # Check the dictionary for existing instance using the row's primary key
        gift = cls.all.get(row[0])
        if gift:
            # ensure attributes match row values in case local instance was modified
            gift.name = row[1]
            gift.price = row[2]
            gift.recipient_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            gift = cls(row[1], row[2], row[3])
            gift.id = row[0]
            cls.all[gift.id] = gift
        return gift

    @classmethod
    def get_all(cls):
        """ Return a list containing one Gift object per table row """
        sql = """
            SELECT *
            FROM gifts
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """ Return Gift object corresponding to the table row matching the specified primary key """
        sql = """
            SELECT *
            FROM gifts
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None