import sys
import requests


def search(params):
    print('Starting')
    url = "https://openlibrary.org/api/books?jscmd=data&format=JSON&bibkeys=ISBN:9780980200447"
    #url = "https://openlibrary.org/api/books?jscmd=data&bibkeys=ISBN:"

    if 'isbn' in params:
        isbn = params['isbn']
        url = url + isbn
        print(url)

    # Make callout to Books API 
    headers = {'accept': 'application/json'}
    r = requests.get(url,headers)

    data = r.json()

    print(data)
    print(str(type(data)))
    for d in data:
        print(d)
    
    if r.status_code != 200:
        print("Failed call Books API")
        return {
            'statusCode': r.status_code,
            'headers': { 'Content-Type': 'application/json'},
            'body': {'message': 'Error procesisng your request'}
        }
    else:
        print("Successfully called Books API")
        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json'},
            'body': {'location': data}
        }

