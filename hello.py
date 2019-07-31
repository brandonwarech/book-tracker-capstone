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
import os
from flask_cors import CORS

app = Flask(__name__, static_url_path='')
CORS(app)
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)
app.register_blueprint(blueprint)
app.config["DEBUG"] = True
app.config["SWAGGER_UI_JSONEDITOR"] = True
ns_search = api.namespace('search', description='Search operations')
ns_favorites = api.namespace('favorites', description='Favorites operations')
ns_reviews = api.namespace('reviews', description='Reviews operations')
ns_friends = api.namespace('friends', description='Friend operations')


book_fields = {
    "isbn": fields.String,
    "author":fields.String,
    "title":fields.String
}
isbn_model = api.model('books', {'isbn':fields.Integer('ISBN Number'),'author':fields.String('Author'), 'title':fields.String('Title')})
review_model = api.model('review', {'user_id':fields.Integer('User ID'), 'rating':fields.Integer('Rating 1-5'), 'comment':fields.String('Free form text comment')})

@app.route('/')
def root():
    return app.send_static_file('index.html')

@ns_search.route('/<string:query>')
class iBooks(Resource):
    def get(self, query):
        query = bs.Search({'query':query})
        results = bs.Search.searchByQuery(query)
        print(results)
        '''return jsonify({'books': results,
        'headers':{'Content-Type': 'application/json'},
        'statusCode':200
        })'''
        return jsonify(results)

@ns_favorites.route('/<string:user_id>')
class iFavorites(Resource):
    def get(self, user_id):
        #return_favorites = []
        iUser = u.User(user_id)
        results = bl.favorite.getFavorites(self, iUser)
        print(results)
        return jsonify({'favorites': results,
        'headers':{'Content-Type': 'application/json'},
        'statusCode':200
        })

    @api.expect(isbn_model, as_list=True)
    def post(self, user_id):
        json_data = request.json
        if 'isbn' in json_data and 'title' in json_data and 'author' in json_data:
            favorite = favorite()
            favorite.isbn = json_data['isbn']
            title = json_data['title']
            author = json_data['author']
            try:
                response = bl.addToFavorites({'isbn':isbn, 'user_id':user_id, 'title':title, 'author':author})
                return response
            except:
                return (response,400)
            else:
                return(response, 200)
        else:
            return('Error: Not all parameters supplied in POST Body json request payload (isbn, title, author)', 400)

    @staticmethod
    @api.param('isbn','Optional: Specific Book ISBN. Without this parameter, will delete all favorites for user')
    def delete(user_id):

        if flask.request.args.get("isbn") != None:
            isbn = flask.request.args.get("isbn")
            result = bl.favorite.removeBookFromFavorites(user_id,isbn)
            return result

        else:
            result = bl.favorite.removeAllFromFavorites(user_id)
            return result
                


@ns_reviews.route('/isbn/<string:isbn>')
class iReviews(Resource):
    @staticmethod
    def get(isbn):
        results = r.Review.getReviewsByISBN(isbn)
        print(results)
        return jsonify(results)

    @api.expect(review_model, as_list=True)
    def post(self,isbn):
        json_data = request.json
        if 'comment' in json_data and 'rating' in json_data and 'user_id' in json_data:
            comment = json_data['comment']
            rating = json_data['rating']
            user_id = json_data['user_id']
            review_obj = r.Review(user_id,isbn,rating,comment)

            try:
                #response = r.Review.addReview({'isbn':isbn, 'user_id':user_id, 'comment':comment, 'rating':rating})
                response = r.Review.addReview(review_obj)
                return response
            except:
                return (response,400)
            else:
                return(response, 200)
        else:
            return('Error: Not all parameters supplied in POST Body json request payload (isbn, title, author)', 400)

@ns_friends.route('/<string:user_id>')
class iFriends(Resource):
    @staticmethod
    def get(user_id):
        results = f.Friend.getFriends(user_id)
        print(results)
        return jsonify(results)
        
    def post(self):
        return True

port = int(os.getenv('PORT', 8000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

