import json

from django.db import connection

from .helpers import extract_http_information, is_asset_path, extract_view_name, get_request_context, sql_timer_enabled
from .query_timer import QueryTimer

__all__ = [
    'RequestCTXMiddleware'
]


class RequestCTXMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        self.is_asset_path = is_asset_path(request)

        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not self.is_asset_path:
            request.ctx = get_request_context(request)

        if sql_timer_enabled():
            request._sql_timer = QueryTimer()
            with connection.execute_wrapper(request._sql_timer):
                response = self.get_response(request)
        else:
            response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        if not self.is_asset_path and hasattr(request, 'ctx'):
            request.ctx.set_response(response)
            request.ctx.set_http_data(extract_http_information(request, response))

            if sql_timer_enabled() and hasattr(request, '_sql_timer'):
                request.ctx.log.set_data('sqlTimers', request._sql_timer.to_log_list())

            dict_to_log = request.ctx.finalize()
            print(json.dumps(dict_to_log))

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not self.is_asset_path:
            fn_name = extract_view_name(view_func)
            request.ctx.view_name = fn_name

        return None
