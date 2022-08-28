

from typing import Generic
from xml.dom import ValidationErr
from Setoran import serializers
from Setoran.models import Mahasantri, Ustadz, Kitab, Setoran
from Setoran.serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User, Group

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_framework import generics


class UstadzViewSet(viewsets.ModelViewSet):
    queryset = Ustadz.objects.all()
    serializer_class = UstadzSerializer

    #authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']


#class UstadzPhotoViewSet(viewsets.ModelViewSet):

    def post(self, request, format=None):
        try:
            # exist then update
            profile = Ustadz.objects.get(user=request.user)
            serializer = UstadzSerializer(ustadz, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Ustadz.DoesNotExist:
            # not exist then create
            serializer = UstadzSerializer(data=param)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class MahasantriViewSet(viewsets.ModelViewSet):
    queryset = Mahasantri.objects.all()
    serializer_class = MahasantriSerializer
    

class KitabViewSet(viewsets.ModelViewSet):
    queryset = Kitab.objects.all()
    serializer_class = KitabSerializer
    

class SetoranCreateAPIView(generics.CreateAPIView):
    queryset = Setoran.objects.all()
    serializer_class = PostSetoranSerializer
setoran_create_view = SetoranCreateAPIView.as_view()

class SetoranListAPIView(generics.ListAPIView):
    queryset = Setoran.objects.all()
    serializer_class = SetoranSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['mahasantri', 'kitab', 'lulus']

setoran_list_view = SetoranListAPIView.as_view()


class SetoranDetailAPIView(generics.RetrieveAPIView):
    queryset = Setoran.objects.all()
    serializer_class = SetoranSerializer

setoran_list_detail_view = SetoranDetailAPIView.as_view()


class SetoranUpdateAPIView(generics.UpdateAPIView):
    queryset = Setoran.objects.all()
    serializer_class = UpdateSetoranSerializer
    lookup_field = "pk"

setoran_detail_update = SetoranUpdateAPIView.as_view()

class SetoranDestroyAPIView(generics.DestroyAPIView):
    queryset = Setoran.objects.all()
    serializer_class = SetoranSerializer
    lookup_field = "pk"

setoran_detail_delete = SetoranDestroyAPIView.as_view()

class KitabAddListAPIView(generics.ListAPIView):
    queryset = Setoran.objects.all()
    serializer_class = SetoranSerializer

    queryset = Kitab.objects.all()
    serializer_class = KitabSerializer

setoran_add_view = KitabAddListAPIView.as_view()



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [authentication.TokenAuthentication]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,

        })


