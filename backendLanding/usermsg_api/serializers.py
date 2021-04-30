from rest_framework import serializers
from .models import UserMsg


#-------------------------------------------------------------------------------


class UserMsgSerializer( serializers.ModelSerializer ):
    
    class Meta:
        model = UserMsg
        fields = '__all__'