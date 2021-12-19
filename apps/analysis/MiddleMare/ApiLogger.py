from django.urls import resolve
from django.utils.log import request_logger


class ApiLogger:
    def __init__(self, get_response):
        self.get_response = get_response
        self.SKIP_NAMESPACE = {"apis:analysis", "apis:device", "apis:micro", "apis:record", "apis:user"}
        self.SKIP_URL_NAME = {""}

    def __call__(self, request):
        response = self.get_response(request)
        namespace = resolve(request.path).namespace
        url_name = resolve(request.path).url_name
        method = request.method

        ip = request.META.get("REMOTE_ADDR")
        status_code = response.status_code
        api = request.get_full_path()
        record = f" {ip} {api} {namespace} {url_name} {status_code}"
        # print(method, ip)
        # print("namespace:{}   url_name:{}".format(namespace, url_name))
        # print(request.get_full_path())
        # print(response.content)
        request_logger.info(record)

        return response
