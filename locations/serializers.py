from rest_framework import serializers

from locations.models import Location


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'pincode',)


class LocationSerializer(serializers.Serializer):
    def to_representation(self, instance):
        def get_districts(state):
            districts = Location.objects.filter(state=state)
            return DistrictSerializer(districts, many=True).data

        return {
            'state': instance,
            'districts': get_districts(instance)
        }
