from django.urls import resolve


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
        remote_host = request.META.get("REMOTE_HOST")
        remote_addr = request.META.get("REMOTE_ADDR")
        status_code = response.status_code
        print(method, remote_addr, remote_host)
        print("namespace:{}   url_name:{}".format(namespace, url_name))
        print(request.get_full_path())
        print(response.content)
        return response
