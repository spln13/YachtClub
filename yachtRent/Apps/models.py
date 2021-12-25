import json
from django.http import JsonResponse


def response(to_return):
    to_return = json.dumps(to_return)
    json_response = JsonResponse(to_return, safe=False)
    return json_response
