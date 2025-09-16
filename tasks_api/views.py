from rest_framework import generics
from .serializers import TaskSerializer
from tasks.models import Tasks


class TaskManager(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



