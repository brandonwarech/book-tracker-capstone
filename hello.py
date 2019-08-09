from flask import Flask, jsonify, request, Blueprint
import classes.favorites as bl
import classes.search as bs
import classes.review as r
import classes
from flask_restplus import Api, Resource, Model, fields, marshal_with
import flask_restplus
import flask
import json
import classes.user as u
import classes.Friend as f
import classes.Book as bk
import os
from flask_cors import CORS
from functools import wraps
import sys

# Setup API Key Authentication for Flask RestPlus
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

# Define Flask App including Blueprint
app = Flask(__name__, static_url_path='')
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, authorizations=authorizations)
app.register_blueprint(blueprint)
app.config["DEBUG"] = True
app.config["SWAGGER_UI_JSONEDITOR"] = True

# Temporarily set token to authenticate against- Future - remove from code and add to config.ini
myToken = 'test_token'

# Enable Cors
CORS(app)

# Define Namespaces for API Families
ns_search = api.namespace('search', description='Search operations')
ns_favorites = api.namespace('favorites', description='Favorites operations')
ns_reviews = api.namespace('reviews', description='Reviews operations')
ns_friends = api.namespace('friends', description='Friend operations')

# Define Object Models for use by API's
book_fields = {
    "isbn": fields.String,
    "author": fields.String,
    "title": fields.String
}
isbn_model = api.model('books', {'isbn': fields.String('ISBN Number'), 'author': fields.String('Author'), 'title': fields.String(
    'Title'), 'publisher': fields.String('Publisher'), 'publication_date': fields.String('Publication Date'), })
review_model = api.model('review', {'user_id': fields.Integer('User ID'), 'rating': fields.Integer(
    'Rating 1-5'), 'comment': fields.String('Free form text comment')})


# Define public endpoints with behaviors
@app.route('/')
def root():
    return app.send_static_file('index.html')


# Implement Authentication
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']
        if not token:
            return {'message': 'Token is missing'}, 401
        if token != myToken:
            return {'message': 'Incorrect token'}, 401
        print('TOKEN: {}'.format(token))
        return f(*args, **kwargs)
    return decorated


@ns_search.route('/<string:query>')
class iBooks(Resource):
    def get(self, query):
        query = bs.Search({'query': query})
        results = bs.Search.searchByQuery(query)
        print(results)

        return jsonify(results)


@ns_favorites.route('/<string:user_id>')
class iFavorites(Resource):

    @api.doc(security='apikey')
    @token_required
    def get(self, user_id):
        try:
            results = bl.favorite.getFavorites(user_id)
            print(results)
            return jsonify(results)

        except:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": {"error": 'Unable to delete Favorites ' + str(sys.exc_info())},
                'details': results
            }


    @api.doc(security='apikey')
    @token_required
    @api.expect(isbn_model)
    def post(self, user_id):

        # Set incoming POST Request Payload Body JSON
        json_data = request.json

        # Validate and parse request body for book values
        if 'isbn' in json_data and 'title' in json_data and 'author' in json_data and 'publisher' in json_data and 'publication_date' in json_data:
            favorite = bl.favorite()
            isbn = json_data['isbn']
            title = json_data['title']
            author = json_data['author']
            publisher = json_data['publisher']
            publication_date = json_data['publication_date']

            # Create book object
            book = bk.Book(isbn, title, author, publisher, publication_date)

            # Add to Favorites DB table
            response = bl.favorite.addToFavorites(favorite, user_id, book)
            return response

        else:
            return('Error: Not all parameters supplied in POST Body json request payload (isbn, title, author)', 400)

    @staticmethod
    @api.param('isbn', 'Optional: Specific Book ISBN. Without this parameter, will delete all favorites for user')
    @api.doc(security='apikey')
    @token_required
    def delete(user_id):

        # Checks if ISBN in URL Path query parameters, if so - removes only that ISBN
        if flask.request.args.get("isbn") != None:
            isbn = flask.request.args.get("isbn")
            result = bl.favorite.removeBookFromFavorites(user_id, isbn)

            if result['statusCode'] == 200:
                return result

            else:
                return {
                    "statusCode": 400,
                    "headers": {"Content-Type": "application/json"},
                    "body": {"error": 'Unable to delete Favorites ' + str(sys.exc_info())},
                    'details': result
                }

        # If No ISBN specified, removes all favorites for the user ID
        else:
            result = bl.favorite.removeAllFromFavorites(user_id)
            if result['statusCode'] == 200:
                return result

            else:
                return {
                    "statusCode": 400,
                    "headers": {"Content-Type": "application/json"},
                    "body": {"error": 'Unable to delete Favorites ' + str(sys.exc_info())},
                    'details': result
                }


@ns_reviews.route('/<string:isbn>')
class iReviews(Resource):
    @staticmethod
    @api.doc(security='apikey')
    @token_required
    def get(isbn):
        results = r.Review.getReviewsByISBN(isbn)
        print(results)
        return jsonify(results)

    @staticmethod
    @api.doc(security='apikey')
    @token_required
    @api.expect(review_model, as_list=True)
    def post(self, isbn):
        json_data = request.json
        if 'comment' in json_data and 'rating' in json_data and 'user_id' in json_data:
            comment = json_data['comment']
            rating = json_data['rating']
            user_id = json_data['user_id']
            review_obj = r.Review(user_id, isbn, rating, comment)

            try:
                response = r.Review.addReview(review_obj)
                return response
            except:
                return (response, 400)
            else:
                return(response, 200)
        else:
            return('Error: Not all parameters supplied in POST Body json request payload (isbn, title, author)', 400)

    @staticmethod
    @api.param('isbn', 'Optional: Specific Book ISBN. Without this parameter, will delete all favorites for user')
    @api.doc(security='apikey')
    @token_required
    def delete(user_id):
        if flask.request.args.get("isbn") != None:
            isbn = flask.request.args.get("isbn")
            result = r.Review.deleteReview(user_id, isbn)
            return result

        else:
            return {"Error: ISBN not provided"}


@ns_friends.route('/<string:user_id>')
class iFriends(Resource):
    @staticmethod
    @api.doc(security='apikey')
    @token_required
    def get(user_id):
        results = f.Friend.getFriends(user_id)
        print(results)
        return jsonify(results)

    @staticmethod
    @api.doc(security='apikey')
    @token_required
    def post(self):
        return True


port = int(os.getenv('PORT', 8000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
