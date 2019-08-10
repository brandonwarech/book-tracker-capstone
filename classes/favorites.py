import ibm_db
import ibm_db_dbi
import sys
import configparser
import logging
import jsonify
import traceback
import classes.iDb as db
import classes.user as u
import json

# Set Logging Level
logging.basicConfig(level=logging.INFO)

# Abstract? class of a saved book (favorite)
class favorite:
    
    def __init__(self):

        # Log the creation of the instance
        logging.debug('Created Favorites Class Instance')

        # Keep list of instances created
        instances = []
        instances.append(self)

    #def to_json(self):
    #    return {'user_id': self.user_id, 'isbn': self.isbn}

    # Class method to retrieve favorites
    @staticmethod
    def getFavorites(user_id):
        try:
            # Calls database 
            favs = db.dbQuery.callDbFetch("SELECT DISTINCT * FROM FAVORITES,BOOK WHERE FAVORITES.ISBN = BOOK.ISBN AND USER_ID = \'" + str(user_id) + "\'")

            # Log Results of DB call and return results
            logging.debug("successful connect to db")
            logging.info("Favorites response: " + str(favs))

            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": favs}

        except:
            logging.error("Oops!" + str(sys.exc_info()) + "occured. ")
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"error": "\'" + str(sys.exc_info()) + "\'"}
            }

    # Class method which adds book to a user's favorites (also to database)
    #@staticmethod
    def addToFavorites(self, user_id, Book):

        self.isbn = Book.isbn
        self.title = Book.title
        self.author = Book.author
        self.publisher = Book.publisher
        self.publication_date = Book.publication_date
        
        # Add to Database        
        results =  db.dbQuery.callDbDelete("INSERT INTO FAVORITES (USER_ID,ISBN) VALUES (\'" + str(user_id) + '\',\'' + str(self.isbn) + '\');')

        # Log things about
        logging.debug(sys.exc_info())
        logging.debug('Result 113: ' + str(results))

        # Return
        return results

    @staticmethod
    def removeAllFromFavorites(user_id):
        #user_id = User.user_id

        try:            
            # Calls database 
            result = db.dbQuery.callDbDelete("DELETE FROM FAVORITES WHERE USER_ID = \'" + str(user_id) + "\'")

            # Log Results of DB call and return results
            logging.debug("successful connect to db2")
            logging.info("response: " + str(result))
            return result

        except:
            logging.error("Oops!" + str(sys.exc_info()) + "occured. ")
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"error": str(sys.exc_info())}
            }

    @staticmethod
    def removeBookFromFavorites(user_id,ISBN):
        try:
            sql = "DELETE FROM FAVORITES WHERE USER_ID = \'" + str(user_id) + "\' AND ISBN = \'" + str(ISBN) + "\'"
            
            # Calls database with constructed SQL from imported db class)
            result = db.dbQuery.callDbDelete(sql)

            # Log Results of DB call and return results
            logging.debug("successful connect to db2")
            logging.info("response: " + str(result))
            return result

        except:
            logging.error("Oops!" + str(sys.exc_info()) + "occured. ")
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"error": str(sql) + str(sys.exc_info())}
            }



