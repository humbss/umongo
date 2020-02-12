from api.user_API import post_user
from api.user_API import get_user
from api.user_API import search_user


def add_routes(app):
    app.add_route(search_user, '/user/search', methods=['POST'])
    app.add_route(post_user, '/user', methods=['POST'])
    app.add_route(get_user, '/user/<user_id>', methods=['GET'])

