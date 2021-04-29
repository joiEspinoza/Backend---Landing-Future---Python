from django.db import models


#-----------------------------------------------------------------------


class Blog ( models.Model ):


    title = models.CharField( max_length = 255, unique = True )
    autor = models.CharField( max_length = 255 )
    url = models.CharField( max_length = 255 )
    textBody = models.CharField( max_length = 15000 )
    date = models.CharField( max_length = 255 )

    def __str__(self):
        return 'title : {} || autor : {} || url : {} || textBody : {} || date : {}'.format( self.title, self.autor, self.url, self.textBody, self.date )

