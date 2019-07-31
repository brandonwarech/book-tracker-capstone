import ibm_db
import ibm_db_dbi
import sys
import configparser
import logging
import jsonify
import traceback
import classes.iDb as db
import classes.user as u
import classes.Book as b
#from abc import ABC, abstractclassmethod, abstractmethod
import traceback

# Set Logging Level
logging.basicConfig(level=logging.INFO)

# Abstract? class of a saved book (favorite)


class Review:

    def __init__(self, user_id, isbn, rating, comment):

        # Log the creation of the instance
        logging.debug('Created Favorites Class Instance')

        # Keep list of instances created
        instances = []
        instances.append(self)

        self.rating = rating
        self.comment = comment
        self.user_id = user_id
        self.isbn = isbn

    # Class method to retrieve favorites based on user_id
    @staticmethod
    def getReviewsByUser(user_id):
        try:
            sql = "SELECT * FROM REVIEWS WHERE USER_ID = " + str(user_id)

            # Calls database with constructed SQL from imported db class
            reviews = db.dbQuery.callDbFetch(sql)

            # Log Results of DB call and return results
            logging.debug("successful connect to db2")
            logging.info("Reviews response: " + str(reviews))
            return favs

        except:
            logging.error("Oops!" + str(sys.exc_info()) + "occured. ")
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"error": str(sql) + str(sys.exc_info())}
            }

    @staticmethod
    def getReviewsByISBN(isbn):
        try:
            sql = "SELECT * FROM KXJ28592.REVIEWS WHERE ISBN = " + str(isbn)
            db_obj = db.dbQuery(sql)
            reviews = db.dbQuery.callDbFetch(db_obj)

            # Log Results of DB call and return results
            logging.debug("successful connect to db2")
            logging.info("SQL: " + str(sql))
            logging.info("Reviews response: " + str(reviews))
            return reviews

        except:
            logging.error("Oops!" + str(sys.exc_info()) + "occured. ")
            logging.error(traceback.print_exc())
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"error": str(sql) + str(sys.exc_info()) + str(traceback.print_exc()
)}
            }

        else:
            return reviews


    # Class method which adds book to a user's favorites (also to database)
    def addReview(self):

        sql = "INSERT INTO KXJ28592.REVIEWS (USER_ID,RATING,COMMENT,ISBN) VALUES (" + str(
            self.user_id) + ',' + str(self.rating) + ',\'' + str(self.comment) + '\',\'' + str(self.isbn) + '\');'

        # The only line of code that really does things (calls out to add favorite to Database)
        query_object = db.dbQuery(sql)
        results = db.dbQuery.callDbInsert(self,query_object)

        # Log things about
        logging.debug(sql)
        logging.debug('Result 113: ' + str(results))

        # Error handling based on response from db.callDbInsert function
        # Follows schema
        # {
        #    "statusCode": 400,
        #    "headers": {"Content-Type": "application/json"},
        #    "body": ''
        # }

        # Handle successful response
        if results['statusCode'] == 200:
            logging.debug(results)
            logging.info('Successfully added to Favorites' + str(results))
            return results, 200

        # Handle unsuccessful resposes
        elif results['statusCode'] == 400:
            return results, 400

        else:
            logging.warning('Unexpected Response recieved from DB callout')
            logging.error(results)
            return results, 500


    @staticmethod
    def deleteReview(user_id,isbn):
        try:
            sql = "DELETE FROM REVIEWS WHERE USER_ID = " + str(user_id) + " AND ISBN = " + str(isbn)

            # Calls database with constructed SQL from imported db class
            result = db.dbQuery.callDbFetch(sql)

            # Log Results of DB call and return results
            logging.debug("successful connect to db2")
            logging.info("response: " + str(result))
            return {"Success"}

        except:
            logging.error("Oops!" + str(sys.exc_info()) + "occured. ")
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"error": str(sql) + str(sys.exc_info())}
            }