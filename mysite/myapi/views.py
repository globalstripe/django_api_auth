from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import HeroSerializer, NewsSerializer
from .models import Hero, News


class HeroViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)

    queryset = Hero.objects.all().order_by('firstname')
    serializer_class = HeroSerializer

class NewsViewSet(viewsets.ModelViewSet):
     
    #permission_classes = (IsAuthenticated,)

    queryset = News.objects.all().order_by('slug')
    serializer_class = NewsSerializer