import json

from pyctx.context import RequestContext

from django_pyctx.helpers import extract_http_information, is_asset_path, extract_view_name

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
            request.ctx = RequestContext(request)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        if not self.is_asset_path:
            request.ctx.set_response(response)
            request.ctx.set_http_data(extract_http_information(request, response))
            dict_to_log = request.ctx.finalize()
            print(json.dumps(dict_to_log))

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not self.is_asset_path:
            fn_name = extract_view_name(view_func)
            request.ctx.set_view_name(fn_name)

        return None
