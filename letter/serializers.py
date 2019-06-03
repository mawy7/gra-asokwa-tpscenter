from rest_framework import serializers

from .models import *


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        exclude = ('name_of_taxpayer')
