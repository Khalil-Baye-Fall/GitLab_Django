from django.shortcuts import render
from api.models import *


# Create your views here.

def home_page(request):
    
    all_lang = Language.objects.all()
    all_topics = Topic.objects.all()
    
    context = {'all_lang': all_lang, 'all_topics': all_topics}
    print(all_topics)
    return render(request, 'api/main.html', context)

def get_topics(request):

    context = {}
    
    return render(request, 'api/topic.html', context)


def get_language(request):
    
    context = {}
    return render(request, 'api/language.html', context)