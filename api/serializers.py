from rest_framework import serializers

from .models import PackageRelease, Project
from .pypi import version_exists, latest_version


class CommentSerializer(serializers.Serializer):
    class Meta:
        model = PackageRelease
        fields = ["name", "version"]
        extra_kwargs = {"version": {"required": True}}

def validate(self, data):
        #TODO
        return data

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "packages"]

    packages = PackageSerializer(many=True)

    def create(self, validated_data):


        
