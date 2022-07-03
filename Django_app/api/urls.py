from django.urls import path
from api.views import *

urlpatterns = [
    
    path('home/', home_page, name='home'),
    path('topic/<str:pk>/', get_topic, name='topic'),
    path('lang/<str:pk>/', get_language, name='langue'),
    path('topics/', Topics, name='topics'),
    path('langues/', langues, name='langues'),
    
    # CRUD
    # POST
    path('topic_view/', topic_view, name='topic_view'),
    path('lang_view/', lang_view, name='lang_view'),
    
    # PUT
    path('update_topic/<str:id>', update_view, name='update_topic'),
    
]
