import copy
from typing import Any, Dict

from django.conf import settings
from pyctx import helpers


DEFAULT_SETTINGS: Dict[str, Any] = {
    'BLACK_LIST': [],
    'CONTEXT_ID_FACTORY': helpers.default_id_factory,
    'REQUEST_ID_FACTORY': helpers.default_id_factory,
    'EXTRAS_FACTORY': helpers.default_extras_factory,
    'ENABLE_SQL_TIMER': False,
}


def get_settings() -> Dict:
    django_pyctx_settings = copy.deepcopy(DEFAULT_SETTINGS)
    user_settings = {x: y for x, y in getattr(settings, "DJANGO_PYCTX", {}).items() if y is not None}
    django_pyctx_settings.update(user_settings)

    return django_pyctx_settings
