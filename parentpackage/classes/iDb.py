import ibm_db
import ibm_db_dbi
import sys
import configparser
import logging
import jsonify
import traceback
import os.path

# Set Logging Level
logging.basicConfig(level=logging.DEBUG)

# Load configuration File Elements Needed
try:
    '''config = configparser.ConfigParser()
    config.read('./parentpackage/config.ini')
    db_creds = config["DATABASE"]["DB_CONN_STRING"]'''
    db_creds = 'DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net;PORT=50001;PROTOCOL=TCPIP;UID=kxj28592;PWD=7d^3h26x21fr717n;Security=SSL;'

except:
    print("Config.ini file not found or not accessible")


class dbQuery:

    def __init__(self, sql):
        self.sql = sql
        logging.debug('Created DB query object for ' + str(sql))
    
    def callDbFetch(self):
        conn_str = db_creds
        sql = self.sql
        response = []

        try:
            ibm_db_conn = ibm_db.connect(conn_str, "", "")
            stmt = ibm_db.exec_immediate(ibm_db_conn, sql)
            dictionary = ibm_db.fetch_assoc(stmt)
            response.append(dictionary)
            print(dictionary)

            while dictionary != False:
                dictionary = ibm_db.fetch_assoc(stmt)
                if dictionary != False:
                    response.append(dictionary)
                    logging.info(dictionary)

            logging.info("successful connect to db2")
            logging.info('Response57: ' + str(stmt))
            logging.info('Response58: ' + str(response))

            return response

        except:
            logging.error("Oops!" + str(sys.exc_info()) + "occured. ")
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"Error": sys.exc_info()}
            }

    #@staticmethod
    def callDbInsert(self,sql):
        conn_str = db_creds

        try:
            ibm_db_conn = ibm_db.connect(conn_str, "", "")
            stmt = ibm_db.exec_immediate(ibm_db_conn, str(sql))
            logging.debug("successful connect to db2")
            logging.info('Response57: ' + str(stmt))
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": 'Success'
            }

        except:
            logging.error("Oops!" + str(sys.exc_info()) + "occured. ")
            # traceback.print_exception()

            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"error": sys.exc_info()}
            }

