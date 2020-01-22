from app.util.App import App


class MemberConverter:

    @classmethod
    def get_member(cls):
        return App.request.query