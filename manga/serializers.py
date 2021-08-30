from rest_framework import serializers

from .models import *


class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = '__all__'





class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageFile
        fields = ('Which_Chapter', 'file')

