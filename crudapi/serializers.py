# Serializers allow complex data such as querysets and 
# model instances to be converted to native Python datatypes 
# that can then be easily rendered into JSON, XML or other content types.

from rest_framework import serializers
from .models import Ne110MAdmin0Countries

# This is a serializer for our countries model
class Ne110MAdmin0CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ne110MAdmin0Countries
        fields = '__all__'
