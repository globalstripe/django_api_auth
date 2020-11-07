from rest_framework import serializers

from .models import Hero
from .models import News

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('created_on','hero_id','firstname', 'lastname', 'postcode', 'profile_url')

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('created_on','news_id','slug', 'story', 'pic_url')
