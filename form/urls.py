from django.urls import path 

# importing views from views..py 
from . import views
from .views import Display
urlpatterns = [ 
    #path('', CreateEntryView.as_view() ), 
    
    path('', views.contact),
    path('snippet', views.snippet_detail),
    path('disp', Display ),
] 