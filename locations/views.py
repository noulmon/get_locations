from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from locations.models import Location
from locations.serializers import LocationSerializer


class LocationsListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            # All states are queried by pre-fetching(joining) the districts in it
            queryset = list(dict.fromkeys(Location.objects.values_list('state', flat=True)))
            # The queryset is then serialized to the required format
            serializer = LocationSerializer(queryset, many=True)

            return Response(
                {
                    'success': True,
                    'message': 'Location list successfully fetched',
                    'data': serializer.data,
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    'success': False,
                    'error': e.__str__(),
                },
                status=status.HTTP_403_FORBIDDEN
            )
