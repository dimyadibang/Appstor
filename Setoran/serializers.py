from Setoran.models import Mahasantri, Ustadz, Kitab, Setoran
from rest_framework import serializers
from django.contrib.auth.models import User, Group


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
    date_created = serializers.DateField(read_only=True, format="%Y-%m-%d")
    time_created = serializers.TimeField(read_only=True, format="%H:%M:%S")
    detail_mahasantri = serializers.SerializerMethodField(read_only=True)
    detail_kitab = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Setoran
        fields = ['id', 'mahasantri', 'kitab','nilai','catatan','lulus', 'date_created', 'time_created' ,'detail_mahasantri', 'detail_kitab', ]
     
    def get_detail_mahasantri(self, obj):
    
        return {
            "id": obj.mahasantri.id,
            "name": obj.mahasantri.name
        }

    def get_detail_kitab(self, obj):
        return {
            "id": obj.kitab.id,
            "halaman": obj.kitab.halaman,
            "awalan": obj.kitab.awalan
        }
    
    
class PostSetoranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setoran
        fields = ['id', 'mahasantri', 'kitab', 'date_created','nilai','catatan','lulus', ]

    def create(self, data):
        formsantri = data['mahasantri']
        formkitab = data['kitab']
        lulus = data['lulus']
        kitab_qs = Setoran.objects.filter(mahasantri=formsantri,kitab=formkitab,lulus=lulus)
        if kitab_qs.exists():
            raise serializers.ValidationError("Kalimat ini telah di setorkan")
        return data
    
    def validate_mahasantri(self, value):
        if value == None:
            raise serializers.ValidationError("Tidak Boleh Kosong")
        return value
    def validate_kitab(self, value):
        if value == None:
            raise serializers.ValidationError("Tidak Boleh Kosong")
        return value


class UpdateSetoranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setoran
        fields = ['id', 'mahasantri', 'kitab', 'date_created','nilai','catatan','lulus', ]

    def validate_mahasantri(self, value):
        if value == None:
            raise serializers.ValidationError("Tidak Boleh Kosong")
        return value
    def validate_kitab(self, value):
        if value == None:
            raise serializers.ValidationError("Tidak Boleh Kosong")
        return value

   
###
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


