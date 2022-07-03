from django.shortcuts import get_object_or_404, render, redirect
from api.models import *
from .forms import *


# Create your views here.

def home_page(request):
    
    all_lang = Language.objects.all()
    all_topics = Topic.objects.all()
    
    context = {'all_lang': all_lang, 'all_topics': all_topics}
    print(all_topics)
    return render(request, 'api/main.html', context)

def get_topic(request, pk=None):
    topic = Topic.objects.get(pk=pk)
    context = {'topic': topic}
    return render(request, 'api/topic.html', context)


def get_language(request, pk=None):
    lang = Language.objects.get(pk=pk)
    context = {'lang': lang}
    return render(request, 'api/language.html', context)

def Topics(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'api/topic.html', context)

def langues(request):
    langues = Language.objects.all()
    context = {'langues': langues}
    return render(request, 'api/language.html', context)


# --------------------------------------------------------
# create CRUD in django 
# POST method
def topic_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = Topic_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
         
    context['form']= form
    return render(request, "common_temp/top_lang.html", context)

def lang_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = Lang_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
         
    context['form']= form
    return render(request, "common_temp/top_lang.html", context)


# Update method
def update_view(request, id):
 
    context ={}

    obj = get_object_or_404(Topic, id = id)
 
    form = Topic_form(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("home")
 
    context["form"] = form
 
    return render(request, "common_temp/top_lang.html", context)