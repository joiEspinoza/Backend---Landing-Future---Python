from rest_framework import serializers
from .models import BotMsg


#-------------------------------------------------------------------------------


class botMsgSerializer( serializers.ModelSerializer ):
    
    class Meta:
        model = BotMsg
        fields = '__all__'