from rest_framework import serializers

from .models import Tcc


class TccSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tcc
        exclude = ('created_date')
