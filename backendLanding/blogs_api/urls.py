from django.urls import path, include
from blogs_api import views


#--------------------------------------------------------------------------


urlpatterns = [
    
    path( 'blogactions/', views.BlogActions.as_view() ),

]
