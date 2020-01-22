from app.util.App import App
from app.vo.GetMemberResponse import GetMemberResponse


class MemberConverter:

    @classmethod
    def get_member(cls):
        return App.request.query

    @classmethod
    def get_member_result(cls, input):
        get_member_response = GetMemberResponse()
        get_member_response.id = input['id']
        get_member_response.nickname = input['nama']
        return vars(get_member_response)

    @classmethod
    def get_members_result(cls, inputs):
        result = []
        for each_member in inputs:
            result.append(cls.get_member_result(each_member))
        return result