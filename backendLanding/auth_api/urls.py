from django.urls import path, include
from .views import AuthActionsAPIView


#--------------------------------------------------------------------------


urlpatterns = [
    
    path( 'login/', AuthActionsAPIView.as_view() ),

]
