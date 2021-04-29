from django.urls import path, include
from botmsg_api import views


#--------------------------------------------------------------------------


urlpatterns = [
    
    path( 'botmsg/', views.BotMsgActions.as_view() ),

]
