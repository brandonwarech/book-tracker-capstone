import sys
import requests
import logging
import json

# Set Logging Level
logging.basicConfig(level=logging.INFO)

# Initialize Variables / Defaults
headers = {"accept": "application/json"}
search_url = "http://openlibrary.org/search.json?"
books_url = "https://openlibrary.org/api/books?jscmd=data&format=JSON"
isbn_array = []
final_books_array = []

def main(params):
    
    logging.info("Starting Search for " + str(params))
    # url = "https://openlibrary.org/api/books?jscmd=data&format=JSON&bibkeys=ISBN:9780980200447"

    if "isbn" in params:
        isbn = params["isbn"]
        data = search_by_isbn(isbn)
        book_object = transform_books_to_output_format(data)
        logging.debug("Returning")
        output = {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": {"books": [book_object]}
        }
        logging.debug(output)
        return output

    elif "query" in params:
        query = params["query"]
        books = open_query_to_summary(query)
        #logging.info(books)
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
        logging.error("Required Parameters not supplied.")
        output = {
            "statusCode": 404,
            "headers": {"Content-Type": "application/json"},
            "body": {"error": "Please provide search parameter"},
        }
        logging.debug(output)
        return output

def open_query_to_summary(query):
    summary = []
    search_url_final = search_url + "q=" + query
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

