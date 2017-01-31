import falcon
import re
# import utils.typeutils


# import conf

# from notification import NOTICE_MNGR

# from framework.falcon.resources.status.logs import PrivateLogsClass
# from utils.fileloader import FileLoader
# from framework.falcon.middleware import headers, handle_404

__version__ = 0.2
__author__ = 'weldpua2008@gmail.com'


class UriFormatter(object):

    """formatting url and prevent ValueError: uri_template may not contain '//'"""

    def __init__(self, prefix, suffix):
        self._prefix = ""
        self._suffix = ""

        # if isinstance(prefix, basestring):
        if utils.typeutils.is_string(prefix):
            self._prefix = prefix
        # if isinstance(suffix, basestring):
        if utils.typeutils.is_string(suffix):
            self._suffix = suffix

    def format(self, uri_local, prefix=None, suffix=None):
        """add prefix to all uri"""
        # if not isinstance(prefix, basestring):
        if not utils.typeutils.is_string(prefix):
            prefix = self._prefix
        # if not isinstance(suffix, basestring):
        if not utils.typeutils.is_string(suffix):
            suffix = self._suffix
        uri_full = prefix + "/" + str(uri_local) + suffix
        uri_full = re.sub("//", "/", uri_full)
        uri_full = re.sub("//", "/", uri_full)
        # print uri_full
        return uri_full


# pylint: disable=line-too-long
# pylint: disable=invalid-name
_uri_formatter = UriFormatter(
    conf.framework.ROUTE_PREFIX,
    conf.framework.ROUTE_SUFFIX)

# pylint: disable=invalid-name
uri = _uri_formatter.format


# pylint: disable=invalid-name
# app = falcon.API(
#     media_type='application/json')

app = falcon.API(
    media_type='application/json',
    middleware=[
        headers.BaseHeaders(),
        handle_404.WrongURL()

    ])

# kwargs_config = {
#     "config_path": conf.CONFIG_PATH}


# app.add_route(uri('components'), ComponentsApp())
# app.add_route(uri('components/{component_name}'), ComponentsApp())


# app.add_route(uri('/private/status/log'), PrivateLogsClass())
# app.add_route(uri('/private/status/log/{log_level}'), PrivateLogsClass())

# app.add_route('/index.html', FileLoader())
# app.add_route('/html/{dir_path}/{file_path}', FileLoader())
