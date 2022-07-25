from Setoran.models import Mahasantri, Ustadz, Kitab, Setoran
from rest_framework import serializers
from django.contrib.auth.models import User, Group
#from django.contrib.authtoken.models import Tokenproxy
from datetime import datetime


class UstadzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ustadz
        fields = '__all__'


class MahasantriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahasantri
        fields = '__all__'


class KitabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitab
        fields = '__all__'


class SetoranSerializer(serializers.ModelSerializer):
    date_created = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    nama_mahasantri = serializers.SerializerMethodField(read_only=True)
    hal_kitab = serializers.SerializerMethodField(read_only=True)

    #mahasantri = serializers.SerializerMethodField(write_only=True)
    #kitab = serializers.SerializerMethodField(write_only=True)

    class Meta:
        model = Setoran
        fields = ['id', 'mahasantri', 'kitab', 'date_created','nilai','ketengan', 'nama_mahasantri', 'hal_kitab', ]



    def get_nama_mahasantri(self, obj):
        return {
            "name": obj.mahasantri.name
        }

    def get_hal_kitab(self, obj):
        return {
            "halaman": obj.kitab.halaman,
            "awalan": obj.kitab.awalan
        }

    
###
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

#class CustomAuthTokenSerializer(serializers.HyperlinkedModelSerializer):
 #   class Meta:
  #      model = Token
   #     fields = '__all__'
