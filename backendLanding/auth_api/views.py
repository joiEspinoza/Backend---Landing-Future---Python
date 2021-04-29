
from rest_framework.response import Response
from rest_framework import generics, status, views, permissions

from .serializers import LoginSerializer


#---------------------------------------------------------------------------------


class AuthActionsAPIView ( generics.GenericAPIView  ):


    serializer_class = LoginSerializer


    def post( self, request ):

        serializer = self.serializer_class( data = request.data )

        if serializer.is_valid():
  
            return Response( { "ok" : True, "user" : serializer.validated_data }, status = status.HTTP_200_OK )

        else:
            return Response( { "ok" : False, "error" : serializer.errors }, status = status.HTTP_400_BAD_REQUEST )

