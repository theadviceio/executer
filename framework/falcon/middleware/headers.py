# pylint: disable=logging-not-lazy, unused-import, no-self-use, unused-argument
# import re
# import falcon
# from conf.framework import CORS_ACTIVE, SERVER_NAME
__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'

class BaseHeaders(object):
    #expression = re.compile("^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$")

    # def process_request(self, req, res):
    # #
    # #     """Process the request before entering in the API
    # #     Before we process anything in the API, we reset the Origin header to
    # #     match the address from the request.
    # #     Args:
    # #         Access-Control-Allow-Origin: Change the origin to the URL that made
    # #             the request.
    # #     Raises:
    # #         HTTP Error: An HTTP error in case the Origin header doesn't match
    # #                     the predefined regular expression.
    # #     Return:
    # #         HTTP headers: A modified set of headers.
    # #     """
    # #
    #     origin_domain = req.get_header("Origin", required=True)
    #     #     # if self.expression.match(origin_domain):
    #     res.set_headers({
    #         'Cache-Control': 'no-store, must-revalidate, no-cache, max-age=0',
    #         'Content-Type': 'application/json; charset=utf-8',
    #         'Access-Control-Allow-Credentials': 'true',
    #         'Access-Control-Allow-Origin': origin_domain,
    #         'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, x-auth-user, x-auth-password, Authorization',
    #         'Access-Control-Allow-Methods': 'GET, PUT, POST, OPTIONS, DELETE'
    #     })
    #     # else:
    #     #     raise falcon.HTTPError(falcon.HTTP_400, "Bad request",
    #     #                            "The Origin header is invalid.")

    def process_response(self, req, res, resource):
        """Process the response before returning it to the client.
        In the reutrning reponse we change some values to be able to overcome
        the CORS protection and mask the origin server. The CORS interaction
        is protected by a check agains a regular expression to make sure the
        origin is a website-like URL.
        Warning:
            If you are really concerned about security, you can deactivate
            the CORS allowance by turning CORS_ACTIVE to `False` in your settings
            file. That will force the application to answer to the SITE_DOMAIN
            domain.
        Args:
            Server (string): Changes the server name sent to the browser in the
                response to avoid exposure of name and version of the same.
            Access-Control-Allow-Origin (string): Change the origin name to
                match the one that made the request. That way we can allow CORS
                anywhere.
        Raises:
            HTTP Error: An HTTP error in case the Origin header doesn't match
            the predefined regular expression.
        Returns:
            HTTP headers: A modified set of headers
        """
        #origin_domain = req.get_header("Origin", required=True)
        # if self.expression.match(origin_domain):
        res.set_headers({
            'Cache-Control': 'no-store, must-revalidate, no-cache, max-age=0',
            'Content-Type': 'application/json; charset=utf-8',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, x-auth-user, x-auth-password, Authorization',
            'Access-Control-Allow-Methods': 'GET, PUT, POST, OPTIONS, DELETE'
        })
        # else:
        #     raise falcon.HTTPError(falcon.HTTP_400, "Bad request",
        #                            "The Origin header is invalid.")
