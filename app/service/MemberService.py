from app.repository.UserRepository import UserRepository
from app.util.App import App
from ..vo.BaseResultVO import BaseResultVO


class MemberService:

    @classmethod
    def get_member(cls):
        query_param = App.request.query
        user_repository = UserRepository()
        result = user_repository.get_user(query_param['id'])
        return BaseResultVO(result=result)