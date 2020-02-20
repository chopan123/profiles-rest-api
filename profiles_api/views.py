from rest_framework.views import APIView
from rest_framework.response import  Response


class HelloApiView(APIView):
    """TEst API View"""

    def get(self, request, format=None):
        """Lists api view features"""
        an_apiview = [
            'Uses HTTP Methods as function (get, post, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives  you the most control of the app logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello', 'an_apiview':an_apiview})
