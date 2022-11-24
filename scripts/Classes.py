from sqlite3.dbapi2 import Date
import time
import logging
import sys
import os
import datetime
import re
import logging
import sqlite3
import wonderwords

if __name__ is "__main__":
    sys.exit('Classes.py should not be directly ran')
else:
    logging.getLogger('Classes')


class Box(object):
    def __init__(self, PhysicalLocation=None, ID=None, FriendlyName=None, DateCreated=None, DateClosed=None, IsOpen=None, QRCode=None) -> None:
        self.ID = ID
        self.FriendlyName = FriendlyName
        self.DateCreated = DateCreated
        self.DateClosed = DateClosed
        self.IsOpen = IsOpen
        self.QRCode = QRCode
        self.PhysicalLocation = PhysicalLocation

    

    def Create_Box(PhysicalLocation):
        FriendlyName = f'{wonderwords.RandomWord().word(include_parts_of_speech=["adjectives"])} {wonderwords.RandomWord().word(include_parts_of_speech=["nouns"])}'
        raise Exception('unfinished')
    @staticmethod
    def Test():
        return f'{wonderwords.RandomWord().word(include_parts_of_speech=["adjectives"])} {wonderwords.RandomWord().word(include_parts_of_speech=["nouns"])}'

class Document:
    def __init__(self, ID, DateUploaded, Image, BoxID, Sender, Category, Notes):
        self.ID = ID
        self.DateUploaded = DateUploaded
        self.Image = Image
        self.BoxID = BoxID
        self.Sender = Sender
        self.Category = Category