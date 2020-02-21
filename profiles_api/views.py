from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions

class HelloApiView(APIView):
    """TEst API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Lists api view features"""
        an_apiview = [
            'Uses HTTP Methods as function (get, post, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives  you the most control of the app logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """ Create a hello with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello message"""
        a_viewset = [
            'Uses action (list, create, retrieve, update, partial_update)',
            'automatically maps to URLs',
            'Provides more functionality with less code',
        ]
        return Response({'message':'hello', 'a_viewset':a_viewset})

    def create(self, request):
        """Create a      new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle Getting an object by id"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle partial updating an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle destroying an object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating  and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)
