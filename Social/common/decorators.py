from django.http.response import HttpResponseBadRequest
from django.http.response import Http404


def ajax_required(func):
    def warp(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest
        return func(request, *args, **kwargs)
    warp.__doc__ = func.__doc__
    warp.__name__ = func.__name__
    return warp