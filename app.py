from apiflask import APIFlask
from db import Post, session
from flask import jsonify
from schemas import PostOutputSchema

app = APIFlask(__name__)


@app.get('/')
def index():
    return {"Message": "Working"}


"""
get /post get_all_post
post /post create_post
get /post/<int:post_id> get_post_by_id
put /post/<int:post_id> update_post
delete /post/<int:post_id> delete_post

------------------------
post /signup create_user
post /login login_user
get /post/<user>/<int:post_id> get_post_by_user

"""


@app.get('/post')
def get_all_post():
    post = session.query(Post).all()
    schema = PostOutputSchema()
    result = schema.dump(post, many=True)

    return jsonify(result)


