from flask import Flask, jsonify, request, Blueprint
import parentpackage.classes.favorites as bl
import parentpackage.classes.search as bs
from flask_restplus import Api, Resource, Model, fields, marshal_with
import flask_restplus
import flask
import json
import parentpackage.classes.user as u

app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)
app.register_blueprint(blueprint)
app.config["DEBUG"] = True
app.config["SWAGGER_UI_JSONEDITOR"] = True
ns_search = api.namespace('search', description='Search operations')
ns_favorites = api.namespace('favorites', description='Favorites operations')

book_fields = {
    "isbn": fields.String,
    "author":fields.String,
    "title":fields.String
}
isbn_model = api.model('books', {'isbn':fields.Integer('ISBN Number'),'author':fields.String('Author'), 'title':fields.String('Title')})

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

@ns_favorites.route('/<int:user_id>')
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




if __name__ == '__main__':
    app.run(debug=True)
