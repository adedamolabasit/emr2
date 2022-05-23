from rest_framework import serializers
from .models import Test


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        depth=3
        exclude = ['id']
        field = ['name','doubt']

