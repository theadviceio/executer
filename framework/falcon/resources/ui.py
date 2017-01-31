import falcon
import json


__version__ = '1.0.0'
__author__ = 'weldpua2008@gmail.com'



# pylint: disable=no-self-use,logging-not-lazy
class UIAPP(object):

    def on_get(self, req, resp, role_group_id=None, role_id=None):
        """Handles GET requests"""
        msg = {"error": False, "error_msg": ""}
        resp.status = falcon.HTTP_200
        
        
        resp.body = json.dumps(msg, sort_keys=True, indent=4)
    
    def on_post(self, req, resp, service_name=None):
        #,state=None,enabled=None):
        """Handles POST requests"""
        body = req.stream.read()
        notification_key = None
        execution_status = {"error": False, "error_msg": ""}
        data, execution_status, resp = self.get_body_json(
            body=body,
            resp=resp,
            execution_status=execution_status)       
        resp.status = falcon.HTTP_200    
        resp.body = json.dumps(execution_status, sort_keys=True, indent=4)