import logging
import sys

import classes.iDb as db
# Set Logging Level
logging.basicConfig(level=logging.INFO)

class Friend:
    def __init__(self, User, Friend):
        self.user_id = User.user_id
        self.friend_id = Friend.user_id
        pass

    def addFriend(self):
        pass

    def removeFriend(self):
        pass


    @staticmethod
    def getFriends(user_id):
        print(user_id)
        try:
            
            sql = "SELECT * FROM FRIEND WHERE USER1 = \'" + str(user_id) +'\' OR USER2 = \'' + str(user_id) + "'"
            
            # Calls database with constructed SQL from imported db class
            #favs = db.db.callDbFetch(sql)
            friends_query_obj = db.dbQuery(sql)
            friends = db.dbQuery.callDbFetch(friends_query_obj)

            # Log Results of DB call and return results
            logging.debug("successful connect to db2")
            logging.info("favorites response: " + str(friends))

            if friends != [False]:
                return friends
            else:
                return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"error": str(sql) + str(sys.exc_info())}
            }

        except:
            logging.error("Oops!" + str(sys.exc_info()) + "occured. ")
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"error": str(sql) + str(sys.exc_info())}
            }
        