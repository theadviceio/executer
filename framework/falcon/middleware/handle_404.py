import json
import falcon

__author__ = 'weldpua2008@gmail.com'

# pylint: disable=unused-argument
class WrongURL(object):

    def process_response(self, req, resp, resource=''):
        """Intercept main 404 response by Falcon
        If the API hits a non existing endpoint, it will trigger a customized
        404 response that will redirect people to the documentation.
        Raises:
            HTTP 404: A falcon.HTTP_404 error
        Returns:
            JSON: A customized JSON response
        """
        if resp.status == falcon.HTTP_404:
            content = resp.body
            if content is None:
                resp.body = json.dumps({
                    "error": True,
                    "error_msg": "Page not found"})
