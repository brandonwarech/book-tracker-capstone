import sys
import requests

headers = {"accept": "application/json"}
search_url = "http://openlibrary.org/search.json?"
books_url = "https://openlibrary.org/api/books?jscmd=data&format=JSON"
isbn_array = []
final_books_array = []


def search(params):
    print("Starting")
    # url = "https://openlibrary.org/api/books?jscmd=data&format=JSON&bibkeys=ISBN:9780980200447"

    if "isbn" in params:
        isbn = params["isbn"]
        data = search_by_isbn(isbn)
        book_object = transform_books_to_output_format(data)
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": {"books": [book_object]},
        }

    elif "author" in params:
        author = params["author"]
        author_isbn = author_query_to_isbn_array(author)
        for i in author_isbn:
            data = search_by_isbn(i)
            final_books_array.append(transform_books_to_output_format(data))
        print(final_books_array)
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": {"books": [final_books_array]},
        }

    elif "title" in params:
        title = params["title"]
        title_isbn = title_query_to_isbn_array(title)
        for i in title_isbn:
            data = search_by_isbn(i)
            final_books_array.append(transform_books_to_output_format(data))
        print(final_books_array)
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": {"books": [final_books_array]},
        }

    else:
        print("error: No parameters supplied")
        return {
            "statusCode": 404,
            "headers": {"Content-Type": "application/json"},
            "body": {"error": "Please provide search parameter"},
        }


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
            publication_date = data[d]["publish_date"]
            book_object = {
                "title": title,
                "isbn": isbn,
                "author": author_array,
                "publisher": publisher,
                "publication_date": publication_date,
                "url": url,
            }
            print(book_object)
            return book_object
        except KeyError:
            pass


def search_by_isbn(isbn):
    books_url_final = books_url + "&bibkeys=ISBN:" + isbn
    try:
        r = requests.get(books_url_final, headers)
        r.raise_for_status()
        data = r.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)


def open_query_to_isbn_array(query):
    search_url_final = search_url + "q=" + query
    r = requests.get(search_url_final, headers)
    data = r.json()
    print(data)


def author_query_to_isbn_array(author):
    search_url_final = search_url + "author=" + author
    print(search_url_final)
    r = requests.get(search_url_final, headers)
    data = r.json()
    for d in data["docs"]:
        try:
            isbn_array.append(d["isbn"][0])
        except KeyError:
            pass
    print(isbn_array)
    return isbn_array


def title_query_to_isbn_array(title):
    search_url_final = search_url + "title=" + title
    print(search_url_final)
    r = requests.get(search_url_final, headers)
    data = r.json()
    for d in data["docs"]:
        try:
            isbn_array.append(d["isbn"][0])
        except KeyError:
            pass
    print(isbn_array)
    return isbn_array


# search({'author':'Rowling'})
search({"isbn": "9780980200447"})
# search({"title": "a child called it"})
# search({'test':'test'})

