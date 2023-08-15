from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Task, Project
from .serializers import TaskSerializer, ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    @action(detail=True, methods=['GET'])
    def tasks(self, request, pk=None):
        project = self.get_object()
        tasks = Task.objects.filter(project_id=project)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)