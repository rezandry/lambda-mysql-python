from app.decorator.Api import Api
from ..service.MemberService import MemberService


class MemberController:

    __service = MemberService()

    @classmethod
    @Api.route(path='/member', method='GET')
    def get_member(cls):
        return cls.__service.get_member()