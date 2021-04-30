from django.db import models


#-----------------------------------------------------------------------


class UserMsg ( models.Model ):


    nombre = models.CharField( max_length = 255 )
    email = models.CharField( max_length = 255 )
    telefono = models.CharField( max_length = 255 )
    empresa = models.CharField( max_length = 255 )
    mensaje = models.CharField( max_length = 15000 )
    date = models.CharField( max_length = 255 )

    def __str__(self):
        return 'nombre : {} || empresa : {} || email : {} || date : {} '.format( self.nombre, self.empresa, self.email, self.date )

