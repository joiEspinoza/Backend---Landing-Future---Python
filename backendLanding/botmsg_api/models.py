from django.db import models


#--------------------------------------------------------------


class BotMsg ( models.Model ):


    msg = models.CharField( max_length = 255 )
    typeMsg = models.CharField( max_length = 255 )

    def __str__( self ):
        return '{} - {}'.format( self.msg, self.typeMsg )


