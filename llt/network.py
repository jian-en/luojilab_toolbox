# -*- coding: utf-8 -*-


def get_client_ip(request):
    """
    从request对象中获取客户端ip地址
    :param request: request对象
    :return: 客户端ip地址
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    else:
        return request.META.get('REMOTE_ADDR')
