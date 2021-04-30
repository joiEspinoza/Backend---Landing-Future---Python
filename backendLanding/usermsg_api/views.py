from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from .serializers import UserMsgSerializer
from .models import UserMsg


#--------------------------------------------------------------------------------


class UserMsgActions ( generics.GenericAPIView ):
  
   
    serializer_class = UserMsgSerializer
    
    def get( self, request ):
        
        try:

            msgs = UserMsg.objects.all()
            
            serializer = self.serializer_class( msgs, many = True )

            return Response( { "ok" : True, "msgs" : serializer.data }, status = status.HTTP_200_OK )


        except:

            return Response( { "ok" : False, "msg" : "GET - something went wrong" } )



    def post( self, request ):


        try:
            print( request.data )
            serializer = self.serializer_class( data = request.data )

            serializer.is_valid( raise_exception = True )
            serializer.save()

            return Response( { "ok" : True, "msg" : 'msg added successfully' }, status = status.HTTP_201_CREATED )

        
        except:
          
            return Response( { "ok" : False, "msg" : "POST - something went wrong" }, status = status.HTTP_400_BAD_REQUEST )
