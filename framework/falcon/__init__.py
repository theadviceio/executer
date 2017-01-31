import falcon
# import conf

# from api.notification import NOTICE_MNGR
# from api.settings.route import uri

# from api.framework.falcon.resources.status.logs import PrivateLogsClass
# from api.utils.fileloader import FileLoader
# from api.framework.falcon.middleware import headers, handle_404

__version__ = 0.2
__author__ = 'weldpua2008@gmail.com'

# pylint: disable=line-too-long


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
