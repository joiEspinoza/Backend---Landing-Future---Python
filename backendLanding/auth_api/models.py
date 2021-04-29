from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


#----------------------------------------------------------------------



class UsuariosManager ( BaseUserManager ):
    """Manager para perfiles de ususario"""

    def create_user( self, email, name, password ):
        """Crear Nuevo Usuario"""

        if not email or not name or not password:
            raise ValueError( "Todos los campos son requerido" )

        email = self.normalize_email( email )
        usuario = self.model( email = email, name = name, password = password )

        usuario.set_password( password )
        usuario.save( using = self._db )

        return usuario



    def create_superuser( self, email, name, password ):
        """Crear Nuevo Usuario"""
        
        usuario = self.create_user( email, name, password )
        usuario.is_superuser = True

        usuario.save( using = self._db )

        return usuario


#----------------------------------------------------------
#----------------------------------------------------------


class Usuarios ( AbstractBaseUser, PermissionsMixin ): 
    """Model Base de datos para usuarios"""
    
    email = models.CharField( max_length = 255, unique = True )
    name = models.CharField( max_length = 255, unique = True )
    password = models.CharField( max_length = 255 )
    is_active = models.BooleanField( default = True )
    is_staff = models.BooleanField( default = True )


    objects = UsuariosManager()
    USERNAME_FIELD = "email" 
    
    #---> EMAIL no puede estar en requeridos | The field named as the 'USERNAME_FIELD' for a custom user model must not be included in 'REQUIRED_FIELDS'. HINT: The 'USERNAME_FIELD' is currently set to 'email', you should remove 'email' from the 'REQUIRED_FIELDS'
    REQUIRED_FIELDS = [ "name", "password" ]


    def __str__(self):
        return 'email : {} || name : {}'.format( self.email, self.name )




