import sys
import requests
import logging
import json

# Set Logging Level
logging.basicConfig(level=logging.INFO)

# Initialize Variables / Defaults
headers = {"accept": "application/json"}
isbn_array = []
final_books_array = []

class Search:
    search_url = "http://openlibrary.org/search.json?"
    books_url = "https://openlibrary.org/api/books?jscmd=data&format=JSON"
    headers = {"accept": "application/json"}

    def __init__(self, params):
        if 'query' in params:
            self.query = params['query']
            logging.debug('Created search instance')
        elif 'isbn' in params:
            self.query =  params['isbn']
            logging.debug('Created search instance')
        else:
            self.query = None
            pass

    def searchByQuery(self):
        
        if self.query != None:
            logging.info("Starting Search")
            # url = "https://openlibrary.org/api/books?jscmd=data&format=JSON&bibkeys=ISBN:9780980200447"
            books = self.open_query_to_summary(self.query)
            output = {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": {"books": books}
            }
            logging.debug("Data type is " + str(type(output)))
            print(type(output))
            logging.debug(output)
            return output
        else:
            
            output = { "body": { "error": "Please provide search parameter" }, "headers": { "Content-Type": "application/json" }, "statusCode": 404 }
            logging.error(output)
            return output

    '''
    else:
        logging.error("Required Parameters not supplied.")
        output = {
            "statusCode": 404,
            "headers": {"Content-Type": "application/json"},
            "body": {"error": "Please provide search parameter"},
        }
        logging.debug(output)
        return output
    '''

    def open_query_to_summary(self, query):
        summary = []
        search_url_final = self.search_url + "q=" + query
        try:
            r = requests.get(search_url_final, headers)
            data = r.json()
            logging.debug(str(type(data)))
            results = data["docs"]

        except requests.exceptions.HTTPError as errh:
            logging.error("Http Error:" + str(errh))
        except requests.exceptions.ConnectionError as errc:
            logging.error("Error Connecting:" + errc)
        except requests.exceptions.Timeout as errt:
            logging.error("Timeout Error:"+ errt)
        except requests.exceptions.RequestException as err:
            logging.error("OOps: Something Else" + err)
            
        for r in results:
            if 'title_suggest' in r and 'isbn' in r and 'author_name' in r and 'publish_year' in r and 'publisher' in r: 
                title = r['title_suggest']
                isbn = r['isbn'][0]
                author = r['author_name']
                publication_date = r['publish_year'][0]
                publisher = r['publisher'][0]

                book_object = {
                    "title": title,
                    "isbn": isbn,
                    "author": author,
                    "publisher": publisher,
                    "publication_date": publication_date
                }
                summary.append(book_object)
                logging.debug('Appending book object: ' + str(book_object))
            
            else:
                logging.debug("Skipping an entry as no ISBN present in object")
                pass
        
        logging.debug(summary)
        return summary

#main({'query':'a child called it'})

