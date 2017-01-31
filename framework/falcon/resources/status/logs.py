import json
import falcon
# import api.status.log

__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'

class PrivateLogsClass(object):
    def on_get(self, req, resp, log_level=None):
        msg = {"error": False, "error_msg": ""}
        try:
            msg = api.status.log.get(level=log_level)
            resp.status = falcon.HTTP_200
        except Exception as error:
            msg["error"] = True
            msg["error_msg"] = "%s" % error
            resp.status = falcon.HTTP_400
        resp.body = json.dumps(msg, sort_keys=True, indent=4)