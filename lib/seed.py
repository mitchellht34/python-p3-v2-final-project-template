from models.__init__ import CONN, CURSOR
from models.recipient import Recipient
from models.gift import Gift
import ipdb

def seed_database():
    Recipient.drop_table()
    Gift.drop_table()
    Recipient.create_table()
    Gift.create_table()

    # Create seed data
    mom = Recipient.create("Mom")
    dad = Recipient.create("Dad")
    zach = Recipient.create("Zach")
    logan = Recipient.create("Logan")
    bottle = Gift.create("Water Bottle", 20, 1)
    tickets = Gift.create("Concert Tickets", 150, 2)
    shirt = Gift.create("T-shirt", 15, 4)
    weights = Gift.create("Dumbells", 45, 4)
    catan = Gift.create("Settlers of Catan", 30, 3)
    chess = Gift.create("Chess Board", 20, 3)


seed_database()
print("Seeded database")
