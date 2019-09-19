from django.http import HttpRequest, HttpResponse


def extract_http_information(request: HttpRequest, response: HttpResponse):
    """
    Extract http information from request and response
    :param request: Django Request instance
    :param response: Django Response instance
    :return:
    """
    http_info = {
        'request': {
            'method': request.method,
            'path': request.path,
            'qs': request.META['QUERY_STRING'],
            'full_path': request.get_full_path(),
            'is_secure': True if request.scheme == 'https' else False,
            'is_xhr': request.is_ajax(),
            'headers': {k: v for k, v in request.headers.items()},
        },
        'client': {
            'ip': get_requester_ip(request),
            'agent': request.META['HTTP_USER_AGENT'],
        },
        'status': {
            'code': response.status_code,
            'phrase': response.reason_phrase,
        },
        'server': {
            'name': request.META['SERVER_NAME'],
            'port': request.META['SERVER_PORT'],
        },
    }

    if 'HTTP_REFERER' in request.META:
        http_info['request'].update({'referrer': request.META['HTTP_REFERER']})

    if 'REMOTE_USER' in request.META:
        http_info['client'].update({'user': request.META['REMOTE_USER']})

    if 'REMOTE_HOST' in request.META:
        http_info['client'].update({'host': request.META['REMOTE_HOST']})

    return http_info


def extract_view_name(view):
    """
    Extract view name
    :param view:
    :return:
    """
    if hasattr(view, '__name__'):
        return view.__name__
    else:  # NOTE: case of class-based view
        return view.__class__.__name__


def is_asset_path(request):
    """
    Check the request path is asset path or not
    :param request: Django Request instance
    :return: boolean
    """
    is_asset = False
    black_list = [
        'media', 'static', 'favicon.ico',
        '/__debug_toolbar__/render_panel/',  # only debug mod and debug_toolbar extension active
    ]
    for p in black_list:
        if p in request.path:
            is_asset = True
            break

    return is_asset


def get_requester_ip(request):
    """
    Get Client IP Address
    :return:
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
