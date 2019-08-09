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
            sql = "SELECT DISTINCT * FROM FAVORITES,BOOK WHERE FAVORITES.ISBN = BOOK.ISBN AND USER_ID = \'" + str(user_id) + "\'"

            # Calls database with constructed SQL from imported db class
            favs_query_obj = db.dbQuery(sql)
            favs = db.dbQuery.callDbFetch(favs_query_obj)

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
                "body": {"error": "\'" + str(sql) + "\'"}
            }

    # Class method which adds book to a user's favorites (also to database)
    @staticmethod
    def addToFavorites(self, user_id, Book):

        self.isbn = Book.isbn
        self.title = Book.title
        self.author = Book.author
        self.publisher = Book.publisher
        self.publication_date = Book.publication_date
        
        # Add to Database        
        sql = "INSERT INTO FAVORITES (USER_ID,ISBN) VALUES (\'" + str(user_id) + '\',\'' + str(self.isbn) + '\');'
        sql_db_object = db.dbQuery(sql)
        results =  db.dbQuery.callDbDelete(sql_db_object)

        # Log things about
        logging.debug(sql)
        logging.debug('Result 113: ' + str(results))

        # Return
        return results

    '''
        try:

            # Handle successful response
            if results['statusCode'] == 200:
                logging.debug(results)
                logging.info('Successfully added to Favorites' + str(results))
                return results
                
            # Handle unsuccessful resposes
            elif results['statusCode'] != 200:
                return results

            else:
                logging.warning('Unexpected Response recieved from DB callout')
                logging.error(results)
                return results


    '''

    @staticmethod
    def removeAllFromFavorites(user_id):
        #user_id = User.user_id

        try:
            sql = "DELETE FROM FAVORITES WHERE USER_ID = \'" + str(user_id) + "\'"
            
            # Calls database with constructed SQL from imported db class
            query_obj = db.dbQuery(sql)
            result = db.dbQuery.callDbDelete(query_obj)

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

    @staticmethod
    def removeBookFromFavorites(user_id,ISBN):
        try:
            sql = "DELETE FROM FAVORITES WHERE USER_ID = \'" + str(user_id) + "\' AND ISBN = \'" + str(ISBN) + "\'"
            
            # Calls database with constructed SQL from imported db class
            query_obj = db.dbQuery(sql)
            result = db.dbQuery.callDbDelete(query_obj)

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



