import traceback

from app.controller.MemberController import SampleController
from app.exception.BaseExceptionHandler import BaseExceptionHandler
from app.util.App import App
from app.util.Request import Request
from app.vo.BaseResultVO import BaseResultVO


class Main:
    @classmethod
    def run(cls, event, context):
        data = BaseResultVO(code=41, message='Not allowed')
        try:
            App.request = Request.load(event)
            if App.request.module and App.request.function:
                invoke = getattr(eval(App.request.module), App.request.function)
                data = invoke()
        except Exception as e:
            print(traceback.format_exc())
            data = BaseExceptionHandler(str(e)).message()
        finally:
            App.clean_up()
            return data.response()