from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
import requests
from requests.exceptions import Timeout
from .util_recipient import recipients_url, list_recipient_json
from core.views import base_view


@base_view
@api_view(http_method_names=['GET'])
def recipients(request: Request) -> Response:
    try:
        recipients_req = requests.get(recipients_url, timeout=10)
        if recipients_req.status_code == 404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        recipients_list = recipients_req.json()
        recipients_list = list_recipient_json(recipients_list)
    except Timeout:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
    if recipients_list:
        return Response(recipients_list)


@base_view
@api_view(http_method_names=['GET'])
def recipient_detail(request: Request, pk: int) -> Response:
    try:
        recipients_req = requests.get(recipients_url, timeout=10)
        if recipients_req.status_code == 404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        recipients_list = recipients_req.json()
        recipients_list = list_recipient_json(recipients_list)
    except Timeout:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
    response = None
    for index, recipient in enumerate(recipients_list):
        if index == pk:
            response = recipient
    if response:
        return Response(response)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
