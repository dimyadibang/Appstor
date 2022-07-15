

from Setoran.models import Mahasantri, Ustadz, Kitab, Setoran
from Setoran.serializers import UstadzSerializer, MahasantriSerializer, KitabSerializer, SetoranSerializer, UserSerializer, GroupSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User, Group

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class UstadzViewSet(viewsets.ModelViewSet):
    queryset = Ustadz.objects.all()
    serializer_class = UstadzSerializer
    
class MahasantriViewSet(viewsets.ModelViewSet):
    queryset = Mahasantri.objects.all()
    serializer_class = MahasantriSerializer
    

class KitabViewSet(viewsets.ModelViewSet):
    queryset = Kitab.objects.all()
    serializer_class = KitabSerializer
    

class SetoranViewSet(viewsets.ModelViewSet):
    queryset = Setoran.objects.all()
    serializer_class = SetoranSerializer

    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['mahasantri', 'kitab']

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
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]