from django.utils.deprecation import MiddlewareMixin


class LogMiddleware(MiddlewareMixin):



    def process_exception(self, request, exception):
        print(exception)
