import ibm_db
import ibm_db_dbi
import sys
import configparser
import logging

# Set Logging Level
logging.basicConfig(level=logging.INFO)

# Load configuration File Elements Needed
try:
    config = configparser.ConfigParser()
    config.read("config.ini")
    db_creds = config["DATABASE"]["DB_CONN_STRING"]

except:
    print("Config.ini file not found or not accessible")

def main(params):

    if "user_id" in params:
        user_id = params["user_id"]
        logging.debug(user_id)

        if "booklist_id" in params:
            booklist_id = params["booklist_id"]
            sql = "SELECT BOOKLIST.BOOKLIST_ID,BOOK.ISBN,BOOK.TITLE,BOOK.AUTHOR FROM BOOKLIST,BOOKLIST_BOOK,BOOK WHERE BOOKLIST.BOOKLIST_ID=BOOKLIST_BOOK.BOOKLIST_ID AND BOOKLIST_BOOK.ISBN = BOOK.ISBN AND USER_ID = " + user_id + " AND BOOKLIST_ID = " + booklist_id + ";"
            results = callDb(sql)
            logging.info('booklist results: ' + str(results))
            return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": {"books": results}
        }

        else:
            logging.info("No booklist_id Parameter supplied, providing all booklists for user")
            sql = "SELECT BOOKLIST.BOOKLIST_ID,BOOK.ISBN,BOOK.TITLE,BOOK.AUTHOR FROM BOOKLIST,BOOKLIST_BOOK,BOOK WHERE BOOKLIST.BOOKLIST_ID=BOOKLIST_BOOK.BOOKLIST_ID AND BOOKLIST_BOOK.ISBN = BOOK.ISBN AND USER_ID = " + user_id + ";"
            results = callDb(sql)
            logging.info('user booklist results' + str(results))
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": {"books": results}
        }

    else:
        logging.error("No user_id parameter supplied")

def callDb(sql):
    conn_str = db_creds
    response =[]

    try:
        ibm_db_conn = ibm_db.connect(conn_str, "", "")
        stmt = ibm_db.exec_immediate(ibm_db_conn, sql)
        dictionary = ibm_db.fetch_assoc(stmt)

        while dictionary != False:
            #print("The ID is : ", dictionary["TITLE"])
            dictionary = ibm_db.fetch_assoc(stmt)
            if dictionary != False:
                response.append(dictionary)
                logging.info(dictionary)

        logging.info("successful connect to db2")
        logging.info('Response57: ' + str(response))
        return response

    except:
        logging.error("Oops!" + sys.exc_info() + "occured.")
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": {"error": sys.exc_info()}
        }

#main({'user_id':'12345'})