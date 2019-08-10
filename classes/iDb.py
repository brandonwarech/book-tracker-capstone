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

# Set DB Credentials -- FUTURE: Move to configuration file
db_creds = 'DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net;PORT=50001;PROTOCOL=TCPIP;UID=kxj28592;PWD=7d^3h26x21fr717n;Security=SSL;'

class dbQuery:

    def __init__(self,sql):
        self.sql = sql
        logging.debug('Created DB query object for ' + str(sql))
    
    @staticmethod
    def callDbFetch(sql):
        conn_str = db_creds
        response = []

        try:
            # Call DB2
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

    @staticmethod
    def callDbInsert(sql):
        conn_str = db_creds
        try:
            ibm_db_conn = ibm_db.connect(conn_str, "", "")
            stmt = ibm_db.exec_immediate(ibm_db_conn, str(sql))
            logging.debug("successful connect to db2")
            logging.info('Response57: ' + str(stmt))
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": 'Success! ' + str(ibm_db.num_rows(stmt)) + ' rows affected'
            }

        except:
            logging.error("Oops!" + str(sys.exc_info()) + "occured. ")
            # traceback.print_exception()

            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"error": str(sys.exc_info())}
            }

    @staticmethod
    def callDbDelete(sql):
        conn_str = db_creds
        try:
            ibm_db_conn = ibm_db.connect(conn_str, "","")
            stmt = ibm_db.exec_immediate(ibm_db_conn,str(sql))
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": "Success! " + str(ibm_db.num_rows(stmt)) + ' rows affected'
            }
            
        except:
            logging.error("Oops!" + str(sys.exc_info()) + "occured. ")
            # traceback.print_exception()

            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"error": str(sys.exc_info())}
            }