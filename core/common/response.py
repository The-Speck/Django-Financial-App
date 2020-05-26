from enum import Enum
from http import HTTPStatus

from django.http.response import JsonResponse


class Response(Enum):
    success = 1
    warning = 2
    error = 3

    @staticmethod
    def respond(message, status, body={}, http_status=HTTPStatus.OK):
        return JsonResponse({
            'message': message,
            'status': status,
            'body': body
        }, http_status)
