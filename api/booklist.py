import ibm_db
import ibm_db_dbi
import sys
import configparser

# Load configuration File Elements Needed
try:
    config = configparser.ConfigParser()
    config.read('config.ini')
    db_creds = config['DATABASE']['DB_CONN_STRING']
except:
    print('Config.ini file not found or not accessible')

def getBookList(params):
    
    if "user_id" in params:
        user_id = params["user_id"]
        print(user_id)
        if "booklist_id" in params:
            booklist_id = params["booklist_id"]
        conn_str = db_creds
        sql = "SELECT BOOKLIST.BOOKLIST_ID,BOOK.ISBN,BOOK.TITLE,BOOK.AUTHOR FROM BOOKLIST,BOOKLIST_BOOK,BOOK WHERE BOOKLIST.BOOKLIST_ID=BOOKLIST_BOOK.BOOKLIST_ID AND BOOKLIST_BOOK.ISBN = BOOK.ISBN AND USER_ID = " + user_id + ";"

        try:
            ibm_db_conn = ibm_db.connect(conn_str,'','')
            stmt = ibm_db.exec_immediate(ibm_db_conn, sql)
            dictionary = ibm_db.fetch_assoc(stmt)

            while dictionary != False:
                print("The ID is : ", dictionary["TITLE"])
                print(str(dictionary))
                dictionary = ibm_db.fetch_assoc(stmt)
                print(str(dictionary))



            print('successful connect')
            print(str(dictionary))
            return dictionary
        except:
            print("Oops!",sys.exc_info(),"occured.")
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"error":sys.exc_info()}
            }
    else:
        print("No parameters supplied")

getBookList({'user_id':'12345'})

'''
import ibm_db
conn = ibm_db.connect("database","username","password")
sql = "SELECT EMPNO, LASTNAME FROM EMPLOYEE WHERE EMPNO > ? AND EMPNO < ?"
stmt = ibm_db.prepare(conn, sql)
max = 50
min = 0
# Explicitly bind parameters
ibm_db.bind_param(stmt, 1, min)
ibm_db.bind_param(stmt, 2, max)
ibm_db.execute(stmt)
# Process results

# Invoke prepared statement again using dynamically bound parameters
param = max, min, 
ibm_db.execute(stmt, param)
'''
