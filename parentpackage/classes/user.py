import logging

# Set Logging Level
logging.basicConfig(level=logging.INFO)

class User:
    def __init__(self,user_id):
        self.user_id = user_id
        self.add_to_db()

    def add_to_db(self):
        logging.info('Mimick add to DB')

