from gettext import install
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    author = serializers.StringRelatedField()
    class Meta:
        model = Article
        fields = '__all__'

"""
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    slug = serializers.SlugField(max_length=200)
    published = serializers.DateTimeField(read_only=True)


    def create(self, validate_data):
        return Article.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.description = validate_data.get('description', instance.description)
        instance.slug = validate_data.get('slug', instance.slug)
        instance.published = validate_data.get('published', instance.published)
        instance.save()

        return instance

"""