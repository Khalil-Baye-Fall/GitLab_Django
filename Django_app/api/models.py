from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)
    comments = models.TextField(max_length=500)
    date_add = models.DateTimeField(auto_now=True)
    # recent_changed = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return "{}: {}".format(self.name, self.comments)
    

class Language(models.Model):
    name_lang = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name_lang