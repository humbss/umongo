from umongo import Document, fields
from util.mongo_connection import get_connection

instance = get_connection()


@instance.register
class User(Document):
    name = fields.StringField(required=True, unique=False)
    email = fields.EmailField(required=True, unique=False)
