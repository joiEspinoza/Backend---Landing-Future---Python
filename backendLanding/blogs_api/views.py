from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from .serializers import blogSerializer
from .models import Blog


#--------------------------------------------------------------------------------


class BlogActions ( generics.GenericAPIView ):
  
   
    serializer_class = blogSerializer
    
    def get( self, request ):
        
        try:

            blogs = Blog.objects.all()
            
            serializer = self.serializer_class( blogs, many = True )

            return Response( { "ok" : True, "blogs" : serializer.data }, status = status.HTTP_200_OK )


        except:

            return Response( { "ok" : False, "msg" : "GET - something went wrong" } )


    def post( self, request ):


        #try:
            print( request.data )
            serializer = self.serializer_class( data = request.data )

            serializer.is_valid( raise_exception = True )
            serializer.save()

            return Response( { "ok" : True, "msg" : 'blog added successfully' }, status = status.HTTP_201_CREATED )

        
        #except:
          
            #return Response( { "ok" : False, "msg" : "POST - something went wrong" }, status = status.HTTP_400_BAD_REQUEST )


    def patch( self, request ):
        
        blog = Blog.objects.get( id = request.data["id"] )
        serializer = self.serializer_class( blog, data = request.data, partial = True )
        
        serializer.is_valid()
        serializer.save()
        
        return Response( { "ok" : True, "blogUpdated" : serializer.data }, status = status.HTTP_200_OK )


    def delete( self, request ):


        try:
          
            serializer = self.serializer_class( data = request.data, partial = True )
            blog = Blog.objects.get( id = serializer.initial_data[ "id" ] ).delete()
            
            return Response( { "ok" : True, "msg" : 'blog deleted successfully' }, status = status.HTTP_204_NO_CONTENT )
        
        except:
          
          return Response( { "ok" : False, "msg" : "DELETE - something went wrong" } )