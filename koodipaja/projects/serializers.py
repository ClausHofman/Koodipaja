from rest_framework import serializers
from .models import Project, ProjectPageTitle, ProjectArticle

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectPageTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPageTitle
        fields = '__all__'

class ProjectArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectArticle
        fields = '__all__'
