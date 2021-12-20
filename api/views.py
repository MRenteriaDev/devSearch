from django.contrib.auth import views
from django.http import JsonResponse
from proyects.models import Project, Review
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ProjectSerializer
from api import serializers

@api_view(["GET"])
def getRoutes(request):

    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]

    return JsonResponse(routes, safe=False)

@api_view(["GET"])
#@permission_classes([IsAuthenticated])
def getProjects(request):
    print("User: ", request.user)
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getProject(request, pk):
    projects = Project.objects.get(id=pk)
    serializer = ProjectSerializer(projects, many=False)
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def project_vote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    review, created = Review.objects.get_or_create(
        owner = user,
        project = project,
    )
    review.value = data["value"]
    review.save()
    project.getVoteCount
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)
