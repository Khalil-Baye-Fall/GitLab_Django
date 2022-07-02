from django.urls import path
from api.views import *

urlpatterns = [
    
    path('home/', home_page, name='home'),
    path('topics/', get_topics, name='topics'),
    path('langs/', get_language, name='langue'),
    
]
