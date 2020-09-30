from rest_framework import serializers

from locations.models import District, State


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name', 'pincode',)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

    def to_representation(self, instance):
        # The districts inside a state is serialized for required fields
        districts = DistrictSerializer(instance.districts, many=True).data
        return {
            'state': instance.name,
            'districts': districts
        }
