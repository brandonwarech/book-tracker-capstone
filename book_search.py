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

    elif "author" in params:
        author = params["author"]
        author_isbn = author_query_to_isbn_array(author)
        for i in author_isbn:
            data = search_by_isbn(i)
            logging.debug('Data37 Debug: ' + str(data))
            if transform_books_to_output_format(data) != None:
                logging.debug('Appending transform_books_to_output_format(data)' + str(transform_books_to_output_format(data)))
                final_books_array.append(transform_books_to_output_format(data))
            else:
                logging.warning('passing as no data was found') 
                pass
        logging.debug("Final Books Array 1 " + str(final_books_array))
        output= {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": {"books": final_books_array} }
        logging.debug('Returning')
        logging.debug(output)
        return output

    elif "title" in params:
        title = params["title"]
        title_isbn = title_query_to_isbn_array(title)
        for i in title_isbn:
            data = search_by_isbn(i)
            final_books_array.append(transform_books_to_output_format(data))
        logging.debug("Final Books Array 2 " + str(final_books_array))
        output = {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": {"books": final_books_array} }
        logging.debug("Returning")
        logging.debug(output)
        return output

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


def open_query_to_isbn_array(query):
    search_url_final = search_url + "q=" + query
    r = requests.get(search_url_final, headers)
    data = r.json()
    logging.debug(data)


def author_query_to_isbn_array(author):
    search_url_final = search_url + "author=" + author
    logging.info(search_url_final)
    r = requests.get(search_url_final, headers)
    data = r.json()
    for d in data["docs"]:
        try:
            isbn_array.append(d["isbn"][0])
        except KeyError:
            pass
    logging.debug(isbn_array)
    return isbn_array


def title_query_to_isbn_array(title):
    search_url_final = search_url + "title=" + title
    logging.debug(search_url_final)
    r = requests.get(search_url_final, headers)
    data = r.json()
    for d in data["docs"]:
        try:
            isbn_array.append(d["isbn"][0])
        except KeyError:
            pass
    logging.debug(isbn_array)
    return isbn_array


search({'author':'Rusty Williams'})
# search({"isbn": "9780980200447"})
# search({"title": "a child called it"})
# seax`rch({'test':'test'})

