from models.__init__ import CURSOR, CONN

class Recipient:

    all={}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

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

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Recipient instances """
        sql = """
            CREATE TABLE IF NOT EXISTS recipients (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Recipient in instances """
        sql = """
            DROP TABLE IF EXISTS recipients;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name value of the current Recipient instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key """
        sql = """
            INSERT INTO recipients (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """ Initialize a new Recipient instance and save the object to the database """
        recipient = cls(name,)
        recipient.save()
        return recipient

    def delete(self):
        """ Delete the table row corresponding to the current Recipient instance,
        delete the dictionary entry, and reassign id attribute """
        sql = """
            DELETE FROM recipients
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
        """ Return a Recipient object having the attribute values from the table row """

        # Check the dictionary for an existing instance using the row's primary key
        recipient = cls.all.get(row[0])
        if recipient:
            # ensure attributes match row values in case local instance was modified
            recipient.name = row[1]
        else:
            # not in dictionary, create new instance and add to dictionary
            recipient = cls(row[1],)
            recipient.id = row[0]
            cls.all[recipient.id] = recipient
        return recipient

    @classmethod
    def get_all(cls):
        """ Return a list containing a Recipient object per row in the table """
        sql = """
            SELECT *
            FROM recipients
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """ Return a Recipient object corresponding to the table row matching the specified primary key """
        sql = """
            SELECT *
            FROM recipients
            WHERE id = ?
        """
        
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None