import sys
import requests
import logging

# Set Logging Level
logging.basicConfig(level=logging.INFO)

# Initialize Variables / Defaults
headers = {"accept": "application/json"}
search_url = "http://openlibrary.org/search.json?"
books_url = "https://openlibrary.org/api/books?jscmd=data&format=JSON"
isbn_array = []
final_books_array = []

def search(params):
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
        open_query_to_summary(query)

    else:
        logging.error("Required Parameters not supplied.")
        output = {
            "statusCode": 404,
            "headers": {"Content-Type": "application/json"},
            "body": {"error": "Please provide search parameter"},
        }
        return output


def transform_books_to_output_format(data):
    for d in data:
        try:
            title = data[d]["title"]
            publisher = data[d]["publishers"][0]["name"]
            isbn = data[d]["identifiers"]["isbn_10"][0]
            url = data[d]["url"]
            author_array = []
            authors = data[d]["authors"]
            for a in authors:
                author_array.append(a["name"])
                logging.debug('Appending ' + a["name"] )
            publication_date = data[d]["publish_date"]
            book_object = {
                "title": title,
                "isbn": isbn,
                "author": author_array,
                "publisher": publisher,
                "publication_date": publication_date,
                "url": url
            }
            logging.debug('Book Object: ' + str(book_object))
            return book_object
        except KeyError:
            logging.warning(KeyError(message))
            pass


def search_by_isbn(isbn):
    books_url_final = books_url + "&bibkeys=ISBN:" + isbn
    try:
        r = requests.get(books_url_final, headers)
        r.raise_for_status()
        data = r.json()
        return data
    except requests.exceptions.HTTPError as errh:
        logging.error("Http Error:" + str(errh))
    except requests.exceptions.ConnectionError as errc:
        logging.error("Error Connecting:" + errc)
    except requests.exceptions.Timeout as errt:
        logging.error("Timeout Error:"+ errt)
    except requests.exceptions.RequestException as err:
        logging.error("OOps: Something Else" + err)


def open_query_to_summary(query):
    summary = []
    search_url_final = search_url + "q=" + query
    try:
        r = requests.get(search_url_final, headers)
        data = r.json()
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
            isbn = r['isbn']
            author = r['author_name']
            publication_date = r['publish_year']
            publisher = r['publisher']

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
            logging.warning("Skipping an entry as no ISBN present in object")
            pass
    
    logging.debug(summary)
    return summary

search({'query':'a child called it'})
# search({"isbn": "9780980200447"})
# search({"title": "a child called it"})
# seax`rch({'test':'test'})

