#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.recipient import Recipient
from models.gift import Gift
import ipdb

def reset_database():
    Recipient.drop_table()
    # Gift.drop_table()
    Recipient.create_table()
    # Gift.create_table()

    # Create seed data
    mom = Recipient.create("Mom")
    dad = Recipient.create("Dad")
    zach = Recipient.create("Zach")
    logan = Recipient.create("Logan")

reset_database()
ipdb.set_trace()
