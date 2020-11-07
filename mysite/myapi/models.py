import uuid
#import django.utils
from django.db import models


class Hero(models.Model): 
    hero_id = models.UUIDField(
      default=uuid.uuid4,
      editable=False)  
 #     using the function uuid4 on the module  
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    postcode = models.CharField(default='NE658UQ', max_length=60)
    created_on = models.DateTimeField(auto_now_add=True)
    profile_url = models.URLField(default='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png', max_length=250)

    def __str__(self):
        return self.firstname

class News(models.Model): 
    news_id = models.UUIDField(
      default=uuid.uuid4,
      editable=False)  
 #     using the function uuid4 on the module  
    slug = models.CharField(max_length=60)
    story = models.CharField(max_length=600)
    created_on = models.DateTimeField(auto_now_add=True)
    pic_url = models.URLField(default='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png', max_length=250)

    def __str__(self):
        return self.slug
