from rest_framework import serializers
from tasks.models import Tasks  # Note: The relative import `..` is correct if `api` and `tasks` are at the same level.

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'duedate', 'priority', 'status', 'Task_status','user']

        