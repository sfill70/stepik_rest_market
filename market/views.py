from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
import requests
from requests.exceptions import Timeout
from .util_market import beauty_url, food_url, presents_url, list_market_json, list_market_json_2


@api_view(http_method_names=['GET'])
def market(request: Request) -> Response:
    try:
        market_list = requests.get(presents_url, timeout=10).json()
        market_list = list_market_json_2(market_list)
    except Timeout:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
    if request.query_params:
        min_price = request.query_params.get('min_price')
        min_weight = request.query_params.get('min_weight')
        if min_price and not min_weight:
            result = [goods for goods in market_list if goods["price"] >= int(min_price)]
            return Response(result)
        if min_weight and not min_price:
            result = [goods for goods in market_list if goods["weight"] >= int(min_weight)]
            return Response(result)
        if min_weight and min_price:
            result = [goods for goods in market_list if
                      goods["price"] >= int(min_price) and goods["weight"] >= int(min_weight)]
            return Response(result)
    if market_list:
        return Response(market_list)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=['GET'])
def product(request: Request, pk: int) -> Response:
    try:
        market_list = requests.get(presents_url, timeout=10).json()
        market_list = list_market_json(market_list)
    except Timeout:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
    response = None
    for box in market_list:
        if box["inner_id"] == pk:
            response = box
    if response:
        response.pop('inner_id', None)
        return Response(response)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
