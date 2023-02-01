from apiflask import APIFlask, abort
from db import Post, session
from flask import jsonify
from schemas import PostOutputSchema, PostCreateSchema, PostUpdateSchema

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


# Getting all post
@app.get('/post')
def get_all_post():
    post = session.query(Post).all()
    schema = PostOutputSchema()
    result = schema.dump(post, many=True)

    return jsonify(result)


# Creating all post
@app.post('/post')
@app.input(PostCreateSchema)
@app.output(PostOutputSchema)
def create_post(data):
    post = data.get('post')

    new_post = Post(post=post)

    session.add(new_post)
    session.commit()
    return new_post, 201


# Getting post by id
@app.get('/post/<int:post_id>')
@app.output(PostOutputSchema)
def get_post_by_id(post_id):
    post = session.query(Post).filter_by(id=post_id).first()

    if post is not None:
        return post, 201

    abort(404)


# Update Post
@app.put('/post/<int:post_id>')
@app.input(PostUpdateSchema)
@app.output(PostOutputSchema)
def update_post(post_id, data):  # Make sure the post_id comes before the data else it would throw an error
    post = data.get('post')
    post_to_update = session.query(Post).filter_by(id=post_id).first()
    post_to_update.post = post

    session.commit()
    return post_to_update


@app.delete('/post/<int:post_id>')
def delete_post(post_id):
    post_to_delete = session.query(Post).filter_by(id=post_id).first()

    session.delete(post_to_delete)
    session.commit()
    return {"message":"Deleted"},204
