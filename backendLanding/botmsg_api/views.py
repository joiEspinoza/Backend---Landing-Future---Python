from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from .serializers import botMsgSerializer


#--------------------------------------------------------------------------------



class BotMsgActions ( generics.GenericAPIView ):

    def get( self, request ):

        serializer_class = botMsgSerializer
        
        data = [ "botMsg" ]

        return Response( { "msg" : "botMsg", "data" : data } )
    

