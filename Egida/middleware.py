from accounts import services


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        request.my_user = services.get_user_from_request(request)

        response = self._get_response(request)

        return response
