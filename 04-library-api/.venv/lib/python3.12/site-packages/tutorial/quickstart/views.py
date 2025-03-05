from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, views, response

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class Index(views.APIView):
    def get(self, request):
        bar = request.GET.get('bar', '')
        r = response.Response(data={'message': 'Hello, world!'})
        #r.headers['Location'] = '\n\n'
        r.headers['Location'] = f'http://localhost:8000/api/?bar={bar}'
        return r