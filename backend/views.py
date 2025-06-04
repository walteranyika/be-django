from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.models import People
from backend.serializers import PeopleSerializer


# Create your views here.
@api_view(['POST'])
def add_new_people(request):
    serializer = PeopleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_all_people(request):
    people = People.objects.all()
    serializer = PeopleSerializer(people, many=True)
    return Response(serializer.data)