from app.decorator.Api import Api
from ..service.MemberService import MemberService


class MemberController:

    __service = MemberService()

    @classmethod
    @Api.route(path='/member', method='GET')
    def get_member(cls):
        return cls.__service.get_member()

    @classmethod
    @Api.route(path='/members', method='GET')
    def get_members(cls):
        return cls.__service.get_members()

    @classmethod
    @Api.route(path='/another-lambda', method='GET')
    def get_another_lambda(cls):
        return cls.__service.get_another_lambda()
