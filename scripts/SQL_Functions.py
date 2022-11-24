import time
import logging
import sys
import os
import datetime
import re
import logging
import sqlite3
from .Functions import *

def Query(query, params=[], returnID = False):
    try:
        logging.info('connecting to db')
        con = sqlite3.connect(os.path.join('data', 'database.db'))
        curser = con.cursor()
        rows = curser.execute(query, params).fetchall()
        if returnID == True:
            id = curser.lastrowid
        results = ','.join(rows)
        con.commit()
    except BaseException as e:
        logging.error('an error occured while running query')
        logging.error(f'query is {query}. params are: {", ".join(params)}')
        logging.error(str(e))
    finally:
        con.close()
        if returnID == True:
            return results, id
        else:
            return results, None

def Initilize_Database():
    #check if db already exists:
    if os.path.exists(os.path.join('data','database.db')):
        pass
    else:
        logging.error('no database.db file found')

    #connect to sql database
    logging.info('opening db connection')
    try: 
        con = sqlite3.connect(os.path.join('data', 'database.db'))
        logging.info('creating boxes table')
        with open (os.path.abspath(os.path.join(os.path.abspath(''), 'scripts', 'create_boxes.sql')), 'r') as sqlFile:
            data = sqlFile.readlines()
            logging.info((' '.join(data)))
            con.execute(' '.join(data))
        
        logging.info('creating documents table')
        with open (os.path.abspath(os.path.join(os.path.abspath(''), 'scripts', 'create_documents.sql')), 'r') as sqlFile:
            data = sqlFile.readlines()
            logging.info((' '.join(data)))
            con.execute(' '.join(data))

    except BaseException as e:
        logging.critical('error raised in sqllite3 connection catcher')
        raise e
    finally:
        con.close()
        logging.info('closed db connection')

def IsTableExists(table):
    #check if db already exists:
    if os.path.exists(os.path.join('data','database.db')):
        pass
    else:
        logging.error('no database.db file found')

    # get connection
    try: 
        con = sqlite3.connect(os.path.join('data', 'database.db'))
        
        #check if table exists
        if len(con.cursor().execute(f"select sql from sqlite_master where type = 'table' and name = '{table}';").fetchall()) == 1:
            results = True
        else:
            results = False
        
    except BaseException as e:
        logging.critical('error while checking for tables')
        logging.critical(str(e))
        raise e
    finally:
        con.close()
        logging.info('closed db connection')
        return results

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        #format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.FileHandler(os.path.join('logs', 'paperwork_tracker.log')), logging.StreamHandler()])
    logging.info('configured logging')
    Initilize_Database(logging)
else:
    logging.getLogger('SQL_Functions')