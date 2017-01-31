import json
# import falcon
import api.utils.errors


__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'


def get_body_json(body):
    data = None
    try:
        data = json.loads(body.decode('utf-8'))
    # pylint: disable=broad-except
    except Exception as error:
        api.utils.errors.get_syntax_error(error)
    return data