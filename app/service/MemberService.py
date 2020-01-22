from app.converter.MemberConverter import MemberConverter
from app.repository.UserRepository import UserRepository
from app.util.App import App
from ..vo.BaseResultVO import BaseResultVO


class MemberService:

    @classmethod
    def get_member(cls):
        request_data = MemberConverter.get_member()
        user_repository = UserRepository()
        result = user_repository.get_user(request_data['id'])
        result = MemberConverter.get_member_result(result)
        return BaseResultVO(result=result)

    @classmethod
    def get_members(cls):
        user_repository = UserRepository()
        results = user_repository.get_users()
        results = MemberConverter.get_members_result(results)
        return BaseResultVO(result=results)