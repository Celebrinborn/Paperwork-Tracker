import time
import logging
import sys
import os
import datetime
import re
import logging
#from functions import Refresh
import sqlite3


logging.basicConfig(
    level=logging.INFO,
    #format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(os.path.join('logs', 'paperwork_tracker.log')), logging.StreamHandler()])
logging.info('configured logging')


#check if db already exists:
if os.path.exists(os.path.join('data','dataframe.sql')):
    pass
else:
    logging.error('no dataframe.sql file found')

#connect to sql database
logging.info('opening db connection')
try: 
    con = sqlite3.connect(os.path.join('data', 'database.db'))
    logging.info('creating boxes table')
    with open (os.path.abspath(os.path.join(os.path.abspath(''), '..', 'scripts', 'create_boxes.sql')), 'r') as sqlFile:
        data = sqlFile.readlines()
        logging.info((' '.join(data)))
        con.execute(' '.join(data))
    
    logging.info('creating documents table')
    with open (os.path.abspath(os.path.join(os.path.abspath(''), '..', 'scripts', 'create_documents.sql')), 'r') as sqlFile:
        data = sqlFile.readlines()
        logging.info((' '.join(data)))
        con.execute(' '.join(data))

except BaseException as e:
    logging.critical('error raised in sqllite3 connection catcher')
    raise e
finally:
    con.close()
    logging.info('closed db connection')