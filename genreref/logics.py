from rest_framework import serializers
from .models import Genre
from rest_framework.viewsets import ModelViewSet


class GenreSerializer(serializers.ModelSerializer):

    parent_str = serializers.CharField(source='parent.name', read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'


class GenreAPI(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
