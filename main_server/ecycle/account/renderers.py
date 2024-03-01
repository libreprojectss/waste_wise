from rest_framework import renderers
import json

class UserRenderer(renderers.JSONRenderer):
    charset='utf-8'
    def render(self,data):
        if 'error' in str(data):
            response=json.dumps({"errors":data})
        else:
            response=json.dumps(data)
        return response