import time
import logging
import sys
import os
import datetime
import re
import logging
import sqlite3
import wonderwords
from .SQL_Functions import Query
from .SQL_Functions import *

if __name__ == "__main__":
    sys.exit('Functions should not be directly ran')
else:
    logging.getLogger('Functions')

def GenerateFriendlyName():
    return f'{wonderwords.RandomWord().word(include_parts_of_speech=["adjectives"])} {wonderwords.RandomWord().word(include_parts_of_speech=["nouns"])}'

def Create_Box(PhysicalLocation):
    assert PhysicalLocation is not None, 'Location cannot be None'
    assert len(str(PhysicalLocation).strip()) > 0, 'Physical Location cannot be blank'
    name = GenerateFriendlyName()
    qrcode = None
    query = f"insert into Boxes (FriendlyName, DateCreated, DateClosed, IsOpen, QRCode, PhysicalLocation) values (?, ?, ?, ?, ?, ?);"
    params = (name, datetime.datetime.now(), datetime.datetime.max, True, qrcode, PhysicalLocation)
    logging.info(f"sending query {query} with params {params}")
    _, id = Query(query, params, True)
    logging.info(f'created box with name {name} and id {id}')
    
    return name, id, qrcode


def Create_Documents():
    pass

def Get_Boxes():
    pass

def Get_Documents(Box):
    pass

def Get_Locations():
    return Query('select distinct PhysicalLocation from Boxes')
