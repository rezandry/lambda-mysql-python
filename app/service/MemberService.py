from ..vo.BaseResultVO import BaseResultVO


class MemberService:

    @classmethod
    def get_member(cls):
        result = {'data': ['Reza']}
        return BaseResultVO(result=result)