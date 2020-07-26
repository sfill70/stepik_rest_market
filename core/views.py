"""Декораторы для вьюшек (фукциий и клаасов, ва разных)
   обработчик не отловленных исключений, сведения выводятся в браузер
   если в сетиднге дебаг=фальш вывода не будет, но не факт"""
import datetime
import functools
import inspect
import json
import traceback

from stepik_rest_market.settings import DEBUG
from django.db import transaction
from django.http import JsonResponse
from django.views import View

JSON_DUMPS_PARAMS = {
    'ensure_ascii': False
}


def ret(json_object, status=200):
    """Отдает JSON с правильным НТТР заголовком и в
    читаемом виде в случае с кирилицей."""
    return JsonResponse(
        json_object,
        status=status,
        safe=not isinstance(json_object, list),
        json_dumps_params=JSON_DUMPS_PARAMS
    )


def error_response(exception):
    """Форматирует НТТР ответ с описанием ошибки и Трасебеком"""
    res = {}
    if DEBUG:
        res = {"errorMessage": str(exception),
               "traceback": traceback.format_exc()}
    return ret(res, status=400)


def base_view(fn):
    """Декоратор для вьюшк (функций), обрабатывает исключения"""

    @functools.wraps(fn)
    def inner(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return fn(request, *args, **kwargs)
        except Exception as e:
            return error_response(e)

    return inner


class BaseView(View):

    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(request, *args, *kwargs)
        except Exception as e:
            return self._response(response)
        else:
            return response

    @staticmethod
    def _response(data, *, status=200):
        return JsonResponse(
            data,
            status=status,
            safe=not isinstance(data, list),
            json_dumps_params=JSON_DUMPS_PARAMS
        )
