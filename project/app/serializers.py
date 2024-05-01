from rest_framework import serializers
from .models import *

class ReactSerializer(serializers.ModelSerializer):
    models = React
    fields = ['employee', 'department']