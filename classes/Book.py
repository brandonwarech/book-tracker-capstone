import logging
import classes.iDb as db

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
        #logging.info('Mimick add to DB')
        sql = "INSERT INTO BOOK (ISBN,TITLE,AUTHOR,PUBLISHER,PUBLICATION_DATE) VALUES (\'" + str(self.isbn) + "\',\'" + str(self.title) + "\',\'" + str(self.author) + "\',\'" + str(self.publisher) + "\',\'" + str(self.publication_date) + "\')"
        print('creating book object in db: SQL : ' + sql)
        logging.info(sql)
        query_object = db.dbQuery(sql)
        results = db.dbQuery.callDbInsert(query_object)
        logging.info(results)
