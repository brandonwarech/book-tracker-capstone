import logging

# Set Logging Level
logging.basicConfig(level=logging.INFO)

class Book:
    def __init__(self,isbn,title,author,publisher,publication_date):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
        #self.genre = genre
        #self.thumbnail_url = thumbnail_url
        self.add_to_db()

    def add_to_db(self):
        logging.info('Mimick add to DB')

