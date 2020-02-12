import json
from bson.objectid import ObjectId
from sanic.log import logger
from sanic.exceptions import ServerError
from model.user import User


class UserService():

    async def register_user(self, user_param):
        try:
            logger.info(self.register_user.__name__+' Inserting a new user.')
            new_user = User(**json.loads(user_param.body))
            await new_user.commit()
            return new_user.dump()
        except Exception as e:
            logger.error(e)
            raise ServerError("Error inserting a new user.", status_code=500)

    async def get_user(self, id):
        try:
            result = await User.find_one({"_id": ObjectId(id)})
            return result.dump()
        except Exception as e:
            logger.error(e)
            raise ServerError("Error while finding user id: " +
                              str(id), status_code=500)

    async def search_user(self, email, page, page_size):
        try:
            if(email is not None):
                cursor = User.find({"email": email}).limit(
                    page_size).skip((page - 1) * page_size)
            else:
                cursor = User.find().limit(page_size).skip((page - 1) * page_size)
            return [u.dump() for u in (await cursor.to_list(page_size))]
        except Exception as e:
            logger.error(e)
            raise ServerError("Error while searching user.", status_code=500)
