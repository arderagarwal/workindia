from rest_framework import serializers
from app.models import  Snippet

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'due_date', 'title', 'description', 'category']
        
