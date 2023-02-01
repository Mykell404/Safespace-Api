from apiflask.schemas import Schema
from apiflask import fields

"""
    class Post:
    id int
    post str
    date_added datetime
"""


class PostOutputSchema(Schema):
    id = fields.Integer()
    post = fields.String()
    date_added = fields.DateTime()
