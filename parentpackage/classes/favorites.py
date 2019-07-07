import ibm_db
import ibm_db_dbi
import sys
import configparser
import logging
import jsonify
import traceback
import parentpackage.classes.iDb as db
import parentpackage.classes.user as u
from abc import ABC,abstractclassmethod,abstractmethod

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

        '''
        # Create favorite object based on the arguments isbn and user_id supplied
        self.isbn = Book.isbn
        self.user_id = User.user_id
        '''
        #self.User = u.User()
        #self.Book = {}

    # Class method to retrieve favorites based on user_id
    def getFavorites(self, User):
        print(User.user_id)
        user_id = User.user_id
        try:
            
            sql = "SELECT * FROM FAVORITES WHERE USER_ID = " + str(user_id)
            
            # Calls database with constructed SQL from imported db class
            favs = db.db.callDbFetch(self,sql)

            # Log Results of DB call and return results
            logging.debug("successful connect to db2")
            logging.info("favorites response: " + str(favs))
            return favs

        except:
            logging.error("Oops!" + str(sys.exc_info()) + "occured. ")
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"error": str(sql) + str(sys.exc_info())}
            }

    # Class method which adds book to a user's favorites (also to database)
    def addToFavorites(self, User, Book):

        self.isbn = Book.isbn
        self.user_id = User.user_id
        
        sql = "INSERT INTO KXJ28592.FAVORITES (USER_ID,ISBN) VALUES (" + str(
            self.user_id) + ',' + str(self.isbn) + ');'

        # The only line of code that really does things (calls out to add favorite to Database) 
        results =  db.db.callDbInsert(self, sql)

        # Log things about
        logging.debug(sql)
        logging.debug('Result 113: ' + str(results))

        # Error handling based on response from db.callDbInsert function
        # Follows schema
        # {
        #    "statusCode": 400,
        #    "headers": {"Content-Type": "application/json"},
        #    "body": ''
        #}
        
        # Handle successful response
        if results['statusCode'] == 200:
            logging.debug(results)
            logging.info('Successfully added to Favorites' + str(results))
            return results, 200
            
        # Handle unsuccessful resposes
        elif results['statusCode'] == 400:
            return results,400

        else:
            logging.warning('Unexpected Response recieved from DB callout')
            logging.error(results)
            return results,500


    def removeFromFavorites(self,params):
        return params




'''    def __str__:
        return '{} {}'.format(self.user_id, self.isbn)'''



