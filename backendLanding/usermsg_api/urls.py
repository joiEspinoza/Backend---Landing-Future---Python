from django.urls import path, include
from usermsg_api import views


#--------------------------------------------------------------------------


urlpatterns = [
    
    path( 'usermsgactions/', views.UserMsgActions.as_view() ),

]
