from rest_framework.serializers import ModelSerializer
from .models import TodoTask

class TaskSerializer(ModelSerializer):
    class Meta:
        model=TodoTask
        fields='__all__'