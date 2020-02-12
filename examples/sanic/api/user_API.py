import json
from service.user_service import UserService
from sanic.response import text
from sanic_openapi import doc
from util.generic_except import get_response_error
from sanic.exceptions import ServerError
from marshmallow.exceptions import ValidationError
from sanic import response


@doc.summary("Post new User.")
@doc.consumes(doc.String(name="body"), location="body")
async def post_user(req):
    try:
        return response.json(await UserService().register_user(req))
    except ServerError as se:
        return get_response_error("user.post.generic.error", se)
    except ValidationError as ve:
        return get_response_error("user.post.validation.error", ve)


@doc.summary("Fetch user by ID.")
async def get_user(req, user_id):
    try:
        user = await UserService().get_user(user_id)
        return response.json(text(user))
    except ServerError as se:
        return get_response_error("user.get.generic.error", se)


@doc.summary("Search users.")
@doc.consumes(doc.String(name="body"), location="body")
async def search_user(req):
    try:
        term = json.loads(req.body)
        email = None
        if "email" in term:
            email = term['email']
        users = await UserService().search_user(email, term['page'], term['page_size'])
        return response.json(text(users))
    except ServerError as se:
        return get_response_error("user.get.generic.error", se)
