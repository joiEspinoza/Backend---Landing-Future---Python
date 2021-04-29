from rest_framework import serializers
from django.contrib import auth
from .models import Usuarios
from rest_framework.exceptions import AuthenticationFailed


#----------------------------------------------------------------------------------------


class LoginSerializer( serializers.ModelSerializer ):
    
    
    email = serializers.EmailField( max_length = 255, min_length = 3 )
    
    password = serializers.CharField( max_length = 68, min_length = 6, write_only = True )
    
    name = serializers.CharField( max_length = 255, min_length = 3, read_only = True )
    


    class Meta:
       
        model = Usuarios
        fields = [ 'email', 'password', 'name' ]
    


    def validate( self, attrs ):
        
        
        email = attrs.get( 'email' )
        password = attrs.get( 'password' )
        

        user = auth.authenticate( email = email, password = password )
        if not user:
           
            raise AuthenticationFailed( 'Invalid credentials, try again' )
        
        else:
            
            data = { "uid" : user.id, 'email' : user.email, 'name' : user.name }


        return data
